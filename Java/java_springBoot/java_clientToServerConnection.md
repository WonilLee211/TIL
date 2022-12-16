# Client to Server 연결

1. client(port : 8080)
   
```java
package com.example.client.controller;

@RestController
@RequestMapping("/api/client")
public class APiController {

    @Autowired
    private final RestTemplateService restTemplateService;

    public APiController(RestTemplateService restTemplateService) {
        this.restTemplateService = restTemplateService;
    }


    @GetMapping("/hello")
    public String getHello(){
        return restTemplateService.hello();
    }
}

```
```java
package com.example.client.service;

@Service
public class RestTemplateService {
    // http://localhost:9090/api/server/hello
    // response

    public String hello(){
        URI url = UriComponentsBuilder
                .fromUriString("http://localhost:9090")
                .path("/api/server/hello")
                .encode()
                .build()
                .toUri();
        System.out.println(url.toString());

        RestTemplate restTemplate = new RestTemplate();
        String result = restTemplate.getForObject(url, String.class);

        return result;

    }
}
```

2. server(port : 9090)

```java
package com.example.server.controller;

@RestController
@RequestMapping("/api/server")
public class ServerApiController {

    @GetMapping("/hello")
    public String hello(){
        return "server hello";
    }
}


```

## RestTemplate을 통한 client-Server json주고받기

- RestTemlate 라이브러리를 통해 다른 서버로 요청-응답을 받음

### GET method

1. client
- 외부에서 요청이 들어오면 client에서 restTemplateService의 메서드 실행
- 

```java
package com.example.client.controller;

@RestController
@RequestMapping("/api/client")
public class APiController {

    @Autowired
    private final RestTemplateService restTemplateService;

    public APiController(RestTemplateService restTemplateService) {
        this.restTemplateService = restTemplateService;
    }


    @GetMapping("/hello")
    public UserResponse getHello(){
        return restTemplateService.hello();
    }
}
```

- 응답 json template

```java
package com.example.client.dto;


public class UserResponse {
    private String name;
    private int age;
}

```

- RestTemplateService를 통해 서버의 특정 메서드, hello를 실행시켜 json을 받아모
  - `getForEntity`

```java
package com.example.client.service;

@Service
public class RestTemplateService {

    // 연결할 서버의 메서드 URI : http://localhost:9090/api/server/hello
    // response

    public UserResponse hello(){
        URI uri = UriComponentsBuilder
                .fromUriString("http://localhost:9090")
                .path("/api/server/hello")
                .encode()
                .build()
                .toUri();
        System.out.println(uri.toString());

        RestTemplate restTemplate = new RestTemplate();
        ResponseEntity<UserResponse> result = restTemplate.getForEntity(uri, UserResponse.class);

        System.out.println(result.getStatusCode());
        System.out.println(result.getBody());
        return result.getBody();

    }
}

```

2. server

```java
package com.example.server.controller;

@RestController
@RequestMapping("/api/server")
public class ServerApiController {

    @GetMapping("/hello")
    public User hello(){
        User user = new User();
        user.setName("steve");
        user.setAge(10);
        return user;
    }
}

```

```java
package com.example.server.dto;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class User {
    private String name;
    private int age;
}

```

### get method with queryParam

1. client

```java
package com.example.client.service;

@Service
public class RestTemplateService {
    // http://localhost:9090/api/server/hello
    // response

    public UserResponse hello(){
        URI uri = UriComponentsBuilder
                .fromUriString("http://localhost:9090")
                .path("/api/server/hello")
                .queryParam("name","steve")
                .queryParam("age",  10)
                .encode()
                .build()
                .toUri();
        System.out.println(uri.toString());

        RestTemplate restTemplate = new RestTemplate();
        ResponseEntity<UserResponse> result = restTemplate.getForEntity(uri, UserResponse.class);

        System.out.println(result.getStatusCode());
        System.out.println(result.getBody());
        return result.getBody();

    }
}

```
2. server

```java
package com.example.server.controller;

@RestController
@RequestMapping("/api/server")
public class ServerApiController {

    @GetMapping("/hello")
    public User hello(@RequestParam String name, @RequestParam int age){
        User user = new User();
        user.setName(name);
        user.setAge(age);
        return user;
    }
}


```

### POST method

1. client
   
```java
package com.example.client.service;

@Service
public class RestTemplateService {

    ...

    public UserResponse post(){
        //http://localhost:9090/api/server/user/{userId}/name/{userName}
        // 1. uri만들기
        URI uri = UriComponentsBuilder
                .fromUriString("http://localhost:9090")
                .path("/api/server/user/{userId}/name/{userName}")
                .encode() // uri를 safe하게 만드는 역할
                .build()
                .expand(100, "steve")
                .toUri();
        System.out.println(uri);

        // 2. 요청보낼 데이터 만들기
        // http body -> object -> object mapper -> json -> rest template -> http body json
        // 요청보낼 양식
        UserRequest req = new UserRequest();
        req.setName("steve");
        req.setAge(100);

        // 3. 요청보내기
        RestTemplate restTemplate = new RestTemplate();
        ResponseEntity<UserResponse> response = restTemplate.postForEntity(uri, req, UserResponse.class); // 보낼 곳의 uri, 보낼 정보, 받은 데이터 형태
        // 4. 데이터 받기
        System.out.println(response.getStatusCode());
        System.out.println(response.getHeaders());
        System.out.println(response.getBody());

        return response.getBody();

        // http://localhost:9090/api/server/user/100/name/steve
        // 200 OK
        // [Content-Type:"application/json", Transfer-Encoding:"chunked", Date:"Fri, 16 Dec 2022 16:07:17 GMT", Keep-Alive:"timeout=60", Connection:"keep-alive"]
        // UserResponse{name='steve', age=100}
    }
}

```

2. server

```java
package com.example.server.controller;

@Slf4j
@RestController
@RequestMapping("/api/server")
public class ServerApiController {
    
    ...

    @PostMapping("/user/{userId}/name/{userName}")
    public User post(@RequestBody User user, @PathVariable int userId, @PathVariable String userName){
        log.info("userId : {}, UserName : {}", userId, userName);
        log.info("client req : {}", user);
        return user;
    }
}

```


### POST method with Header

- 만든 uri에  RequestEntity를 이용하여 header 추가하기
- restTemplate.exchange() 메서드 사용하여 서버에 요청보내기

1. client

```java
package com.example.client.service;

@Service
public class RestTemplateService {
    ...

    public UserResponse exchange(){
        URI uri = UriComponentsBuilder
                .fromUriString("http://localhost:9090")
                .path("/api/server/user/{userId}/name/{userName}")
                .encode() // uri를 safe하게 만드는 역할
                .build()
                .expand(100, "steve")
                .toUri();
        System.out.println(uri);


        // 2. 요청보낼 데이터 만들기
        // http body -> object -> object mapper -> json -> rest template -> http body json
        // 요청보낼 양식
        UserRequest req = new UserRequest();
        req.setName("steve");
        req.setAge(100);

        RequestEntity<UserRequest> requestEntity = RequestEntity
                .post(uri)
                .contentType(MediaType.APPLICATION_JSON)
                .header("X-authorization", "abcd")
                .header("custom-header", "fffff")
                .body(req);

        // 3. 헤더 실어서 요청보내기
        RestTemplate restTemplate = new RestTemplate();
        ResponseEntity<UserResponse> response = restTemplate.exchange(requestEntity, UserResponse.class);

        return response.getBody();
    }
}

```

2. server

- `@RequestHeader("fieldName")`로 매개변수 받기

```java
package com.example.server.controller;

@Slf4j
@RestController
@RequestMapping("/api/server")
public class ServerApiController {

    @PostMapping("/user/{userId}/name/{userName}")
    public User exchange(@RequestBody User user,
                     @PathVariable int userId,
                     @PathVariable String userName,
                     @RequestHeader("x-authorization") String authorization,
                     @RequestHeader("custom-header") String customHeader
    ){
        log.info("userId : {}, UserName : {}", userId, userName);
        log.info("authorization : {}, custom : {}", authorization, customHeader);
        log.info("client req : {}", user);
        return user;
    }
}

```

### json 디자인하기

- 상황에 따라  json의 특정 필드에 담기는 값들이 변경되는 상황일 때 맞춰서 통신할 수 있도록 json 설계

```json
{
  "header": {
    "response_code": ""
  },
  "body": {
    "name": "spring boot",
    "age": 1024
  }
}

```

1. client

- Req dto 설계
  - 계속 바뀌는 부분은 generic type으로 선언하기

```java
package com.example.client.dto;

public class Req<T> { 
    private Header header; // 상황에 따라 입력되는 데이터가 달라진다.

    private T resBody; // Generic type으로 받아오기


    public static class Header{
        private String responseCode;

        ...
    }
    ...
}

```

- genericRestTemplateService 설계

  - **주의**  : generic type에서는 class를 붙일 수 없음
  - ParameterizedTypeReference : 이를 해결하기 위해 사용하는 클래스


```java

package com.example.client.service;

@Service
public class RestTemplateService {
    ...

    public Req<UserResponse> genericExchange(){

        URI uri = UriComponentsBuilder
                .fromUriString("http://localhost:9090")
                .path("/api/server/user/{userId}/name/{userName}")
                .encode() // uri를 safe하게 만드는 역할
                .build()
                .expand(100, "steve")
                .toUri();
        System.out.println(uri);


        // 2. 요청보낼 데이터 만들기
        // http body -> object -> object mapper -> json -> rest template -> http body json

        // 요청보낼 양식
        UserRequest userRequest = new UserRequest();
        userRequest.setName("steve");
        userRequest.setAge(100);

        Req req = new Req();
        req.setHeader(new Req.Header());
        req.setResBody(userRequest);

        RequestEntity<Req<UserRequest>> requestEntity = RequestEntity
                .post(uri)
                .contentType(MediaType.APPLICATION_JSON)
                .header("X-authorization", "abcd")
                .header("custom-header", "fffff")
                .body(req);

        RestTemplate restTemplate = new RestTemplate();

//        ResponseEntity<Req<UserResponse>> response
//                = restTemplate.exchange(requestEntity, Req<UserResponse>.class); // 에러
        // generic type에서는 class를 붙일 수 없음

        // ParameterizedTypeReference : 이때 사용하는 클래스
        ResponseEntity<Req<UserResponse>> response =
                restTemplate.exchange(requestEntity, new ParameterizedTypeReference<Req<UserResponse>>(){});

        return response.getBody();

    }
}

```

2. server

- Req dto 설계

```java
package com.example.server.dto;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class Req<T> {

    private Header header;
    private T resBody;

    @Data
    @NoArgsConstructor
    @AllArgsConstructor
    public static class Header{
        private String responseCode;
    }
}

```

- ServerApiController
    - requestBody에 담겨있는 정보  Req 양식에 맞춰 입력 후 반환
  
```java
package com.example.server.controller;

import com.example.server.dto.Req;
import com.example.server.dto.User;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.HttpEntity;
import org.springframework.web.bind.annotation.*;

@Slf4j
@RestController
@RequestMapping("/api/server")
public class ServerApiController {

    @GetMapping("/hello")
    public User hello(@RequestParam String name, @RequestParam int age){
        User user = new User();
        user.setName(name);
        user.setAge(age);
        return user;
    }

    @PostMapping("/user/{userId}/name/{userName}")
    public Req<User> exchange(
                              @RequestBody Req<User> user,
                              @PathVariable int userId,
                              @PathVariable String userName,
                              @RequestHeader("x-authorization") String authorization,
                              @RequestHeader("custom-header") String customHeader
    ){
        log.info("userId : {}, UserName : {}", userId, userName);
        log.info("authorization : {}, custom : {}", authorization, customHeader);
        log.info("client req : {}", user);

        Req<User> response = new Req<>();
        response.setHeader(new Req.Header());
        response.setResBody(user.getResBody());

        return response;
    }
}

```

- response

```json
{
    "header": {
        "responseCode": null
    },
    "resBody": {
        "name": "steve",
        "age": 100
    }
}

```