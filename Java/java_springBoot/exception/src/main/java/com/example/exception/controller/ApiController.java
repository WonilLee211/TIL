package com.example.exception.controller;

import com.example.exception.dto.User;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.MethodArgumentNotValidException;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;
import javax.validation.constraints.Min;
import javax.validation.constraints.NotBlank;
import javax.validation.constraints.NotNull;
import javax.validation.constraints.Size;

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
