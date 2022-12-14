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

## 실습

### log 찍기

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