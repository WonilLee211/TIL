# Swagger

- 개발한 REST API를 편리하게 문서화해주고 이를 통해서 관리 및 제 3의 사용자가 편리하게 API를 호출해보고 테스트할 수 있는 프로젝트
- spring boot에서는 간단하게 springfox-boot-starter를 gradle dependencies에 추가함으로 사용할 수 있다.
다만 주의할 점은 운영환경과 같은 외부에 노출되면 안되는 곳에 사용할 때 주의해야 한다.

## swagger annotation

1. `@Api` : 클래스를 스웨거의 리소스로 표시
2. `@ApiOperation` : 특정 경로의 오퍼레이션 HTTP 메소드 설명
3. `@ApiParam` : 오퍼레이션 파라미터에 메타데이터 설명
4. `@ApiResponse` : 오퍼레이션 응답 지정
5. `@ApiModelProperty` : 모델의 속성 데이터를 설명
6. `@ApiImplicitParam` : 메소드 단위의 오퍼레이션 파라미터를 설명
7. `@ApiImplicitParam`


### 주의

- version missmatch
  - Spring boot 2.6버전 이후에 spring.mvc.pathmatch.matching-strategy 값이 ant_apth_matcher에서 path_pattern_parser로 변경되면서 몇몇 라이브러리(swagger포함)에 오류가 발생함. 

> 해결책
>  - application.properties에 코드 추가
>  - `spring.mvc.pathmatch.matching-strategy=ant_path_matcher`

- http://localhost:8080/swagger-ui/ 에서 api 확인

----


## RequestParameter description

### 1. `@ApiParam`

- 매개 변수에 직접 달기

```java
package com.example.swagger.controller;

@Api(tags={"API 정보를 제공하는 Controller"}) // tags : swagger-ui에서 컨트롤러 제목 설정
@RestController
@RequestMapping("/api")
public class ApiController {

    @GetMapping("/plus")
    public int plus(
            @ApiParam(value = "x값")
            @RequestParam int x,

            @ApiParam(value = "y값")
            @RequestParam int y){

        return x + y;
    }

    @ApiResponse(code = 502, message = "사용자의 나이가 10살 이하일 때")
    @ApiOperation(value = "사용자의 이름과 나이를 RETURN하는 메서드")
    @GetMapping("/user")
    public UserRes user(UserReq userReq){
        return new UserRes(userReq.getName(), userReq.getAge());
    }

    @PostMapping("/user")
    public UserRes userPost(@RequestBody UserReq req){
        return new UserRes(req.getName(), req.getAge());
    }
}

```

```java
package com.example.swagger.dto;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class UserReq {

    @ApiModelProperty(value = "사용자의 이름", example = "steve", required = true)
    private String name;
    @ApiModelProperty(value = "사용자의 나이", example = "10", required = true)
    private int age;

}

```

### 2. `@ApiImplicitParams`

- method에 달기


```java
package com.example.swagger.controller;


@Api(tags={"API 정보를 제공하는 Controller"}) // tags : swagger-ui에서 컨트롤러 제목 설정
@RestController
@RequestMapping("/api")
public class ApiController {


    @ApiImplicitParams({
                    @ApiImplicitParam(name = "x", value = "x 값", required = true, dataType = "int", paramType = "path"),
                    @ApiImplicitParam(name = "y", value = "y 값", required = true, dataType = "int", paramType = "query"),
    })
    @GetMapping("/plus")
    public int plus(@RequestParam int x, @RequestParam int y){
        return x + y;
    }
    ...

}

```