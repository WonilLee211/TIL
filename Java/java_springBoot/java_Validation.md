# Validation

- 특히 Java에서는 null 값에 대해서 접근하려고 할 때 null pointer exceptionO| 발생 함으로, 이러한 부분을 방지 하기 위해서 미리 검증을 하는 과정을 Validation 이라고 합니다.
- 예)
```java
public void run(String account Spring pwf int age){
    if(account== null || pw == null){ 
        return
    }
    if(age == 0){
        return
    }
}
```

## 단점

1. 검증해야 할 값이 많은 경우 코드의 길이가 길어진다
2. 구현에 따라서 달라 질 수 있지만 Service Logic과의 분리가 필요 하다.
3. 흩어져 있는 경우 어디에서 검증을 하는지 알기 어려우며, 재사용의 한계가 있다.
4. 구현에 따라 달라질 수 있지만, 검증 Logic이 변경 되는 경우 테스트 코드 등 참조하는 클래스에서 Logic이 변경되어야 하는 부분이 발생할 수 있다.

## validation annotation

1. `@Size` : 문자 길이 측정
2. `@NotNull` : null 불가
3. `@NotEmpty` : null, ""불가
4. `@NotBlank` : null, "", " " 불가
5. `@Past` : 과거 날짜
6. `@PastOrPresent` : 오늘이거나 과거날짜
7. `@Future` : 미래날짜
8. `@FutureOrPresent` : 오늘이거나 미래날짜
9. `@Pattern` : 정규식 적용
10. `@Max` : 최댓값
11. `@Min` : 최소값
12. `@AssertTrue/ False` : 별도 Logic 적용
13. `@Valid` : 해당 object validation 실행


l.gradle dependecies
    - `implementation(,,org.springframework.boot：pring-boot-starter-validation")`

2.  bean validation spec

    -  `https://beanvalidation.org/2.0-jsr80/`

3. 핸드폰 번호 정규식

    - `"^\\d{2,3}-\\d{3,4}-\\d{4}$"`


## basic validation in rest controller

```java

package com.example.validation.dto;

import javax.validation.constraints.Email;
import javax.validation.constraints.Max;
import javax.validation.constraints.NotBlank;
import javax.validation.constraints.Pattern;

public class User {
    @NotBlank
    private String name;

    @Max(value = 90)
    private int age;

    @Email // email validation field에 붙는 validation annotation
    private String email;

    @Pattern(regexp = "^\\d{2,3}-\\d{3,4}-\\d{4}$", message = "핸드폰 양식과 맞지 않습니다. 01x-xxx(x)-xxxx")
    private String phoneNumber;
    ...
}

```
-  `@Valid` : requestBody 내부 값의 유효성을 검사함
-  `BindingResult` : 유효성 검사 결과를 담음

```java
package com.example.validation.controller;


import com.example.validation.dto.User;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.BindingResult;
import org.springframework.validation.FieldError;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import javax.validation.Valid;

@RestController
@RequestMapping("/api")
public class ApiController {


    // @Valid : requestBody 내부 값의 유효성을 검사함
    // BindingResult : 유효성 검사 결과를 담음
    @PostMapping("/post")
    public ResponseEntity user(@Valid @RequestBody User user, BindingResult bindingResult){

        if(bindingResult.hasErrors()){
            StringBuilder sb = new StringBuilder();
            bindingResult.getAllErrors().forEach(objectError -> {

                FieldError field = (FieldError) objectError;
                String message = objectError.getDefaultMessage();

                System.out.println("field : " + field.getField());
                System.out.println(message);

                sb.append("field : " +field.getField());
                sb.append("\n");
                sb.append("message : " + message);
            });
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(sb.toString());

            // phoneNumber 필드 값 양식이 맞지 않게 요청보냈을 때 응답 값
                // field : phoneNumber
                // 핸드폰 양식과 맞지 않습니다. 01x-xxx(x)-xxxx

        }

         // ok logic

        System.out.println(user);
        return ResponseEntity.ok(user);
    }
}


```

## custom validation

- 피치 못할 예외 상황에서 유효성 검사를 위한 과정
- 예)
  - 날짜 입력 타입이 문자열일 때 기존의 validation annotation을 사용하지 못한다.
  - 이에 custom validation을 통해 입력값 유효성을 검사해야 함
- `@AssertTrue/False` : custom logic 적용

```java
package com.example.validation.dto;

public class User {

    ...

    @Size(min=6, max=6) // 너무 문자열 길이만 유효성 검사하는 약한 단계
    private String reqYearMonth; // yyyyMM

    @AssertTrue(message = "yyyyMM 형식에 맞지 않습니다.")
    public boolean isReqYearMonthValidation(){
        try {
            // DataTimeFormatter는 day까지 포함하기 때문에 전처리 해줘야 함
            LocalDate localDate = LocalDate.parse(getReqYearMonth() +"01", DateTimeFormatter.ofPattern("yyyyMMdd"));
        }catch (Exception e){
            System.out.println(e.toString());
            return false;
        }
        System.out.println(getReqYearMonth());
        return true;
    }
    ...
}


```

- custom logic이 적용되지만 재사용 불가능

### Reusable custom validation annotation

- `@ConstraintValidator` : 재사용이 가능한 custom logic 적용

1. 기존 annotation 참조하기

- `@Email`
```java
/*
 * Jakarta Bean Validation API
 *
 * License: Apache License, Version 2.0
 * See the license.txt file in the root directory or <http://www.apache.org/licenses/LICENSE-2.0>.
 */
package javax.validation.constraints;

/**
 * The string has to be a well-formed email address. Exact semantics of what makes up a valid
 * email address are left to Jakarta Bean Validation providers. Accepts {@code CharSequence}.
 * <p>
 * {@code null} elements are considered valid.
 *
 * @author Emmanuel Bernard
 * @author Hardy Ferentschik
 *
 * @since 2.0
 */
@Documented
@Constraint(validatedBy = { })
@Target({ METHOD, FIELD, ANNOTATION_TYPE, CONSTRUCTOR, PARAMETER, TYPE_USE })
@Retention(RUNTIME)
@Repeatable(List.class)
public @interface Email {

	String message() default "yyyyMM 형식에 맞지 않습니다.";

	Class<?>[] groups() default { };

	Class<? extends Payload>[] payload() default { };

	/**
	 * @return an additional regular expression the annotated element must match. The default
	 * is any string ('.*')
	 */
	String regexp() default ".*";

	/**
	 * @return used in combination with {@link #regexp()} in order to specify a regular
	 * expression option
	 */
	Pattern.Flag[] flags() default { };

	/**
	 * Defines several {@code @Email} constraints on the same element.
	 *
	 * @see Email
	 */
	@Target({ METHOD, FIELD, ANNOTATION_TYPE, CONSTRUCTOR, PARAMETER, TYPE_USE })
	@Retention(RUNTIME)
	@Documented
	public @interface List {
		Email[] value();
	}
}

```

- custom annotation default code

```java
package com.example.validation.annotation;

import javax.validation.Constraint;
import javax.validation.Payload;
import java.lang.annotation.Retention;
import java.lang.annotation.Target;

import static java.lang.annotation.ElementType.*;
import static java.lang.annotation.ElementType.TYPE_USE;
import static java.lang.annotation.RetentionPolicy.RUNTIME;

@Constraint(validatedBy = { })
@Target({ METHOD, FIELD, ANNOTATION_TYPE, CONSTRUCTOR, PARAMETER, TYPE_USE })
@Retention(RUNTIME)
public @interface YearMonth {

    String message() default "yyyyMM 형식에 맞지 않습니다.";

    Class<?>[] groups() default { };

    Class<? extends Payload>[] payload() default { };

    String pattern() default "yyyyMMdd";
}
//---------------------------------------------------------------
package com.example.validation.dto;

import com.example.validation.annotation.YearMonth;

import javax.validation.constraints.*;
import javax.xml.crypto.dsig.spec.XPathType;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;

public class User {
   ...

    @YearMonth
    private String reqYearMonth; // yyyyMM
   ...
}

```

- custom validation annotation 사용하는 validator 만들기

```java
package com.example.validation.validator;

public class YearMonthValidator implements ConstraintValidator<YearMonth, String> { // 검사 기준과 검사할 값

    private String pattern; // 초기에 확인할 값
    @Override
    public void initialize(YearMonth constraintAnnotation) {
        this.pattern = constraintAnnotation.pattern();

    }

    @Override
    public boolean isValid(String value, ConstraintValidatorContext context) {
        // yyyyMM
        try {
            // DataTimeFormatter는 day까지 포함하기 때문에 전처리 해줘야 함
            LocalDate localDate = LocalDate.parse(value +"01", DateTimeFormatter.ofPattern(this.pattern));
        }catch (Exception e){
            System.out.println(e.toString());
            return false;
        }
        return true;
    }
}

```

- **에러 발생**
  - annotation/YearMonth.java에 `@Constraint`안에 validator를 명시하지 않았음
  - `javax.validation.UnexpectedTypeException: HV000030: No validator could be found for constraint 'com.example.validation.annotation.YearMonth' validating type 'java.lang.String'. Check configuration for 'reqYearMonth'`


```java
package com.example.validation.annotation;

@Constraint(validatedBy = {YearMonthValidator.class}) // << 제작한  validator class넘겨주기
@Target({ METHOD, FIELD, ANNOTATION_TYPE, CONSTRUCTOR, PARAMETER, TYPE_USE })
@Retention(RUNTIME)
public @interface YearMonth {

    String message() default "yyyyMM 형식에 맞지 않습니다.";

    Class<?>[] groups() default { };

    Class<? extends Payload>[] payload() default { };

    String pattern() default "yyyyMMdd";

}

```
> 주의
> - class 안에 다른 객체가 있고 그 객체가 Object타입이라면 해당 클래스에 `@Valid`를 붙여야 함

```java
package com.example.validation.dto;

public class Car {
    @NotBlank
    private String name;

    @NotBlank
    @JsonProperty("car_number")
    private String carNumber;

    @NotBlank
    @JsonProperty("TYPE")
    private String type;
    ...
}

```
```java
package com.example.validation.dto;

public class User {
    @NotBlank
    private String name;
    @Max(value = 90)
    private int age;

    @Valid // << 내부에 Object를 가지고 있기 때문에 검사 대상자로 선언해줘야 함
    private List<Car> cars;
    ...
}

```
## Validation 모범사례

