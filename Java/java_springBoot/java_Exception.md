# Exception 처리

Web Application 의 입장에서 바라 보았을때, 에러가 났을 때 내려줄 수 있는 방법은 많지 않다.

1. 에러 페이지
2.4XX Error or 5XX Error
3. Client가 200 외에 처리를 하지 못 할 때는 200을 내려주고 별도의 에러 Message 전달

## exception annotation

1. `@ControllerAdvice` : Global 예외 처리 및 특정 package / Controller 예외 처리

    - 옵션
        - `basePackages` : 특정한 위치에  발생하는 모든 에러를 잡는다는 의미

```java
package com.example.exception.advice;

@RestControllerAdvice(basePackages = "")
public class GlobalControllerAdvice {

    @ExceptionHandler(value=Exception.class) // value : 어떤 에러를 잡을 건지 작성하는 부분(Exception.class : 모든 예외를 의미)
    public ResponseEntity exception(Exception e){

        System.out.println("__________________________________");
        System.out.println(e.getClass().getName());
//        org.springframework.web.bind.MethodArgumentNotValidException

        System.out.println(e.getLocalizedMessage());



        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body("");

    }


    @ExceptionHandler(value= MethodArgumentNotValidException.class)
    public ResponseEntity methodArgumentNotValidException(MethodArgumentNotValidException e){

        return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(e.getMessage());

    }
}


```

2. `@ExceptionHandler` : 특정 Controller의 예외 처리


- 특정 ApiController에 국한시키기
    -  ApiController 클래스 내부에 ExceptionHandler 작성하기

```java
package com.example.exception.controller;

@RestController
@RequestMapping("/api/user")
public class ApiController {

    @GetMapping("")
    public User get(@RequestParam(required = false) String name, @RequestParam(required = false) Integer age){
        // required = false : 해당 매개변수가 없어도 동작하지만 null 할당됨
        User user = new User();
        user.setName(name);
        user.setAge(age);

        int a = 10 + age;


        return user;
    }

    @PostMapping("")
    public User post(@Valid @RequestBody User user){
        System.out.println(user);
        return user;
    }

    @ExceptionHandler(value= MethodArgumentNotValidException.class)
    public ResponseEntity methodArgumentNotValidException(MethodArgumentNotValidException e){

        return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(e.getMessage());

    }
}

```

