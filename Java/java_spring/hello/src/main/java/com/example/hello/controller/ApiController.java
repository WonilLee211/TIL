package com.example.hello.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController // 해당 class는 REST API 처리하는 controller임을 지정하는 데코레이터
@RequestMapping("/api") // URI를 지정해주는 Annotation
public class ApiController {
    @GetMapping("/hello") // http://localhost/api/hello url 매핑
    public String hell(){
        return "hello spring boot!";
    }
}
