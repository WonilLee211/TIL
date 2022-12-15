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
