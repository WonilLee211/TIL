# Validation 모범사례

## API 요청 Validation과 exception form

### exception form 양식

```json
{
    "statusCode": "400 BAD_REQUEST",
    "requestUrl": "/api/user",
    "code": null,
    "message": "",
    "resultCode": "Fail",
    "errorList": [
        {
            "field": "age",
            "message": "1 이상이어야 합니다",
            "invalidValue": "0"
        },
        {
            "field": "name",
            "message": "크기가 1에서 10 사이여야 합니다",
            "invalidValue": ""
        },
        {
            "field": "name",
            "message": "공백일 수 없습니다",
            "invalidValue": ""
        }
    ]
}
```

## ApiController 설계

### `@Valid`

- 빈 검증기(Bean Validator)를 이용해 객체의 제약 조건을 검증하도록 지시하는 어노테이션
-  기본적으로 컨트롤러에서만 동작

### `@Validated

- 다른 계층에서 파라미터를 검증하기 위해서는 @Validated와 결합
- AOP 기반으로 메소드의 요청을 가로채서 유효성 검증을 진행
- 클래스 레벨에 선언하면 해당 클래스에 유효성 검증을 위한 AOP의 어드바이스 또는 인터셉터(MethodValidationInterceptor)가 등록됨
- 그리고 해당 클래스의 메소드들이 호출될 때 AOP의 포인트 컷으로써 요청을 가로채서 유효성 검증을 진행
- 이러한 이유로 컨트롤러, 서비스, 레포지토리 등 계층에 무관하게 스프링 빈이라면 유효성 검증을 진행할 수 있음

> 클래스에는 유효성 검증 AOP가 적용되도록 @Validated를, 검증을 진행할 메소드에는 @Valid를 선언해주어야 한다.
>> @Valid에 의한 예외는 MethodArgumentNotValidException이며, 
>> @Validated에 의한 예외는  ConstraintViolationException이다.

```java
package com.example.exception.controller;

@RestController
@RequestMapping("/api/user")
@Validated
public class ApiController {

    @GetMapping("")
    public User get(

            @NotBlank
            @Size(min=1, max=10)
            @RequestParam String name,

            @NotNull
            @Min(1)
            @RequestParam Integer age){
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
        System.out.println("in class");
        return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(e.getMessage());

    }
}
```

2. ApiControllerAdvise 설계

- 설계할 때 에러별로 디버깅을 거치며 해당 에러가 어떤 속성을 가지고 있는지 확인하면서 처리해야 함

```java
package com.example.exception.advice;

@RestControllerAdvice(basePackageClasses = ApiController.class)
public class ApiControllerAdvice {

    @ExceptionHandler(value=Exception.class) // value : 어떤 에러를 잡을 건지 작성하는 부분(Exception.class : 모든 예외를 의미)
    public ResponseEntity exception(Exception e){

        System.out.println(e.getClass().getName());
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body("");

    }


    @ExceptionHandler(value= MethodArgumentNotValidException.class)
    public ResponseEntity methodArgumentNotValidException(MethodArgumentNotValidException e, HttpServletRequest httpServletRequest){// HttpServletRequest : 현재의 request 가져올 수 있음

        BindingResult bindingResult = e.getBindingResult();
        List<Error> errorList = new ArrayList<>(); // 에러들 담을 곳

        bindingResult.getAllErrors().forEach(error -> {
            FieldError field = (FieldError) error;
            String fieldName = field.getField();
            String message = field.getDefaultMessage();
            String invalidValue = field.getRejectedValue().toString();

            Error errorMessage = new Error(); // Error 객체에 각 정보 입력
            errorMessage.setField(fieldName);
            errorMessage.setMessage(message);
            errorMessage.setInvalidValue(invalidValue);

            errorList.add(errorMessage);    // error 객체 errorList에 담기
        });

        ErrorResponse errorResponse = new ErrorResponse();
        errorResponse.setErrorList(errorList);
        errorResponse.setMessage("");
        errorResponse.setRequestUrl(httpServletRequest.getRequestURI());
        errorResponse.setStatusCode(HttpStatus.BAD_REQUEST.toString());
        errorResponse.setResultCode("Fail");

        return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(errorResponse);

    }

    // 인자는 받았는데 제약조건에 맞지않을 때 발생하는 에러
    @ExceptionHandler(value= ConstraintViolationException.class)
    public ResponseEntity ConstraintViolationException(ConstraintViolationException e, HttpServletRequest httpServletRequest){

        List<Error> errorList = new ArrayList<>(); // 에러들 담을 곳

        e.getConstraintViolations().forEach(error -> {

            Stream<Path.Node> stream = StreamSupport.stream(error.getPropertyPath().spliterator(), false);
            List<Path.Node> list = stream.collect(Collectors.toList());

            String fieldName = list.get(list.size() - 1).getName();
            String message = error.getMessage();
            String invalidValue = error.getInvalidValue().toString();


            Error errorMessage = new Error();
            errorMessage.setField(fieldName);
            errorMessage.setMessage(message);
            errorMessage.setInvalidValue(invalidValue);

            errorList.add(errorMessage);

        });

        ErrorResponse errorResponse = new ErrorResponse();
        errorResponse.setErrorList(errorList);
        errorResponse.setMessage("");
        errorResponse.setRequestUrl(httpServletRequest.getRequestURI());
        errorResponse.setStatusCode(HttpStatus.BAD_REQUEST.toString());
        errorResponse.setResultCode("Fail");

        return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(errorResponse);
    }


    // 요청과정에서 받아야하는 인자가 비어있을때 발생하는 에러
    @ExceptionHandler(value = MissingServletRequestParameterException.class)
    public ResponseEntity missingServletRequestParameterException(MissingServletRequestParameterException e, HttpServletRequest httpServletRequest){

        List<Error> errorList = new ArrayList<>(); // 에러들 담을 곳

        String fieldName = e.getParameterName();
        String message = e.getMessage();

        Error errorMessage = new Error();
        errorMessage.setField(fieldName);
        errorMessage.setMessage(message);

        ErrorResponse errorResponse = new ErrorResponse();
        errorResponse.setErrorList(errorList);
        errorResponse.setMessage("");
        errorResponse.setRequestUrl(httpServletRequest.getRequestURI());
        errorResponse.setStatusCode(HttpStatus.BAD_REQUEST.toString());
        errorResponse.setResultCode("Fail");

        return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(errorResponse);
    }
}

```

3. dto

- User

```java
package com.example.exception.dto;


public class User {

    @NotEmpty
    @Size(min=1, max=10)
    private String name;

    @Min(1)
    @NotNull
    private Integer age;
    ...
}

```

- Error

```java
package com.example.exception.dto;

public class Error {

    private String field;
    private String message;
    private String invalidValue;

   ...
}


```

- ErrorResponse

```java
package com.example.exception.dto;

// exception message form
public class ErrorResponse {

    String statusCode;
    String requestUrl;
    String code;
    String message;
    String resultCode;

    List<Error> errorList;

    ...
}


```