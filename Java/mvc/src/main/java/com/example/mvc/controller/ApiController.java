package com.example.mvc.controller;


import com.example.mvc.dto.UserRequest;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api")
public class ApiController {

    @GetMapping
    public UserRequest User(UserRequest request){
        return request;
    }
}
