package com.example.exception.advice;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.MethodArgumentNotValidException;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;



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
        System.out.println("out of class");
        return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(e.getMessage());

    }
}
