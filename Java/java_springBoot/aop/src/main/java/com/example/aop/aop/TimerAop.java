package com.example.aop.aop;

import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Pointcut;
import org.springframework.stereotype.Component;
import org.springframework.util.StopWatch;

/*
 @Bean() VS @Component()
@Bean() : method에 붙어 bean에 등록
@Componenet() : 클래스 단위에 붙어 Bean 등록
@Configuration() : 하나의 클래스에 여러가지 Bean을 적용함

*/
@Aspect
@Component
public class TimerAop {

    @Pointcut("execution(* com.example.aop.controller..*.*(..))")
    private void cut(){}

    // 해당 패키지에 선언된 annotation이 선언된 클래스를 Pointcut하고 logging할거다!
    @Pointcut("@annotation(com.example.aop.annotation.Timer)")
    private void enableTimer(){}

    // Timer는 Before After로 전후를 못정함. 이떄 쓰는게 Around
    @Around("cut() && enableTimer()")
    public void around(ProceedingJoinPoint joinPoint) throws Throwable {
        StopWatch stopWatch = new StopWatch();
        stopWatch.start();

        Object result = joinPoint.proceed(); // 프로젝트 실행

        stopWatch.stop();

        System.out.println("total time : " + stopWatch.getTotalTimeSeconds());
    }

}
