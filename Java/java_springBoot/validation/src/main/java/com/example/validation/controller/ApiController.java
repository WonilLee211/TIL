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
        }

         // ok logic

        System.out.println(user);
        return ResponseEntity.ok(user);
    }
}
