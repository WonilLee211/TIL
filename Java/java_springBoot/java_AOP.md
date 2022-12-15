# AOP(Aspect Oriented Programming)

- **관점지향 프로그램**
- 스프링 어플리케이션은 대부분 특별한 경우를 제외하고는 MVC 웹 어플리케이션에서는 Web Layer, Business Layer, Data Layer 로 정의

    - Web Layer: REST API를 제공하며, Client 중심의 로직 적용
    - Business Layer: 내부 정책에 따른 logic를 개발하며, 주로 해당 부분을 개발 
    - Data Layer: 데이터 베이스 및 외부와의 연동을 처리

## 활용 방법

1. Method Parameter Log
2. 실행시간 Log
3. Parameter Encode


## 주요 annotation

- `@ Aspect` :  자바에서 널리 사용하는 AOP 프레임워크에 포함되며, AOP를 정의하는 class에 할당
- `@Pointcut` : 기능을 어디에 적용시킬지, 메소드, annotation 등 AOP를 적용시킬 지점을 설정
- `@Before` :  메소드를 실행하기 전
- `@After` : 메소드가 성공적으로 실행 후, 예외가 발생하더라도 실행
- `@AfterReturning` : 메소드 호출 성공 실행 시(Not Throws)
- `@AfterThrowing` : 메소드 호출 실패 예외 발생(Throws)
- `@Around` : Before / after  모두 제어

## 실습 1. log 찍기

- `@Pointcut("execution()")

```java
package com.example.aop.controller;

import com.example.aop.dto.User;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api")
public class RestApiController {

    @GetMapping("/get/{id}")
    public String get(@PathVariable Long id, @RequestParam String name) {
        System.out.println("get method");
        System.out.println("get method : " + id);
        System.out.println("get method : " + name);

        return id + " " + name;
    }

    @PostMapping("/post")
    public User post(@RequestBody User user){
        System.out.println("post method : " + user);
        return user;
    }
}
```

```java
package com.example.aop.aop;

import org.aspectj.lang.JoinPoint;
import org.aspectj.lang.annotation.AfterReturning;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;
import org.aspectj.lang.annotation.Pointcut;
import org.aspectj.lang.reflect.MethodSignature;
import org.springframework.stereotype.Component;

import java.lang.reflect.Method;

@Aspect
@Component
public class ParameterAop {

    @Pointcut("execution(* com.example.aop.controller..*.*(..))")
    private void cut(){}

    @Before("cut()") // @Pointcut에 있는 메소드가 실행되기 전에 실행
    public void before(JoinPoint joinPoint){// 들어가는 지점에 대한 정보를 가지고 있는 객체

        MethodSignature methodSignature = (MethodSignature) joinPoint.getSignature();
        Method method = methodSignature.getMethod();
        System.out.println(method.getName());

        Object[] args = joinPoint.getArgs();

        for(Object obj : args) {
            System.out.println("type : " + obj.getClass().getSimpleName());
            System.out.println("value : " + obj);
        }
    }

    @AfterReturning(value = "cut()", returning = "returnObj") // @Pointcut에 있는 메소드의 반환이 완료된 후
    public void afterReturn(JoinPoint joinPoint, Object returnObj){
        System.out.println("return obj : ");
        System.out.println(returnObj);
    }
}


// post
// type : User
// value : User{id='user01', pw='pw01', email='steve@gmail.com'}
// post method : User{id='user01', pw='pw01', email='steve@gmail.com'}
// return obj : 
// User{id='user01', pw='pw01', email='steve@gmail.com'}
```
### @Bean() VS @Component()
- @Bean() : method에 붙어 bean에 등록
- @Componenet() : 클래스 단위에 붙어 Bean 등록
- @Configuration() : 하나의 클래스에 여러가지 Bean을 적용함


## 실습 2. PC status logging

- annotation customizing을 통해 해당 annotation이 설정된 메소드만 기록되도록 하기

1. annotation 만들기

```java

package com.example.aop.aop;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

@Target({ElementType.TYPE, ElementType.METHOD})
@Retention(RetentionPolicy.RUNTIME)
public @interface Timer {}

```

- 제작한 annotationd인 `@Timer`가 위치를 잡을 수 있도록 aop클래스 메서드에 `@Around` 붙여주기
  
```java
package com.example.aop.aop;

import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Pointcut;
import org.springframework.stereotype.Component;
import org.springframework.util.StopWatch;


@Aspect
@Component
public class TimerAop {

    @Pointcut("execution(* com.example.aop.controller..*.*(..))")
    private void cut(){}

    // 해당 패키지에 선언된 annotation이 선언된 클래스를 Pointcut하고 logging할거다!
    @Pointcut("@annotation(com.example.aop.annotation.Timer)")
    private void enableTimer(){}

    // Timer는 Before After로 위치 못정함. 이때 쓰는게 Around
    @Around("cut() && enableTimer()")
    public void around(ProceedingJoinPoint joinPoint) throws Throwable {
        StopWatch stopWatch = new StopWatch();
        stopWatch.start();

        Object result = joinPoint.proceed();
        stopWatch.stop();

        System.out.println("total time : " + stopWatch.getTotalTimeSeconds());
    }

}

```

- controller에 메소드에 제작한 annotation 붙임
  
```java

package com.example.aop.controller;

import com.example.aop.aop.Timer;
import com.example.aop.dto.User;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api")
public class RestApiController {
    
    ...
    
    @Timer // 직접 만든 annotation
    @DeleteMapping("/delete")
    public void delete() throws InterruptedException {

        // db logic
        Thread.sleep(1000 * 2); // 2초 있다가 종료되도록 설정
    }
}

```

- 외부에서 암호화된 필드나 파일이 들어올 때 AOP layer에서 복호화해서 들어오게 할 수 있음
- 또는 자료를 조작할 수 있음

## 메서드 입출력 데이터 변경하기

- 메서드가 실행되기 전 특정 데이터를 decoding
- 메서드가 반환될 때 특정 데이터를 encoding


### @Decode annotation 생성

```java
package com.example.aop.annotation;

public @interface Decode {}

```

### DecodeAop 설계

```java

package com.example.aop.aop;

import com.example.aop.dto.User;
import org.aspectj.lang.JoinPoint;
import org.aspectj.lang.annotation.AfterReturning;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;
import org.aspectj.lang.annotation.Pointcut;
import org.springframework.stereotype.Component;

import java.io.UnsupportedEncodingException;
import java.util.Base64;

@Aspect
@Component
public class DecodeAop {
    @Pointcut("execution(* com.example.aop.controller..*.*(..))")
    private void cut(){}

    @Pointcut("@annotation(com.example.aop.annotation.Decode)")
    private void enableDecode(){}

    @Before("cut() && enableDecode()") // 메서드가 실행이 될 때
    public void before(JoinPoint joinPoint) throws UnsupportedEncodingException {
        Object[] args = joinPoint.getArgs();

        for(Object arg : args){ // 메서드의 인자들 중에
            if(arg instanceof User){ // 내가 원하는 유저라는 클래스가 있으면
                User user = User.class.cast(arg); // User클래스로 형변환
                String base64Email = user.getEmail();
                // Decoding by Base64
                String email = new String(Base64.getDecoder().decode(base64Email), "UTF-8");
                user.setEmail(email); // inserting decoded data
            }
        }
    }
    @AfterReturning(value = "cut() && enableDecode()", returning = "returnObj" )
    public void afterReturn(JoinPoint joinPoint, Object returnObj){
        if(returnObj instanceof User){
            User user = User.class.cast(returnObj); // User클래스로 형변환
            String email = user.getEmail(); // get the decoded email Data
            // encoding the Decoded email
            String base64Email = Base64.getEncoder().encodeToString(email.getBytes());
            user.setEmail(base64Email); // inserting the encoded data
        }

    }
}

```

### DecodeAop 입히기

```java
package com.example.aop.controller;

import com.example.aop.annotation.Decode;
import com.example.aop.annotation.Timer;
import com.example.aop.dto.User;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api")
public class RestApiController {
    ...

    @Decode
    @PutMapping("/put")
    public User put(@RequestBody User user){
        // 메서드가 실행되기 전에는 encoded data를 Decoding해서 출력
        System.out.println("put");
        System.out.println(user);
        // 값이 외부로 반환될 때는 다시 encoding 형태로 출력
        return user;
    }
}

```