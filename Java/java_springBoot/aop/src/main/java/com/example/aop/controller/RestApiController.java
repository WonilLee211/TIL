package com.example.aop.controller;

import com.example.aop.annotation.Decode;
import com.example.aop.annotation.Timer;
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

    @Timer // 직접 만든 annotation
    @DeleteMapping("/delete")
    public void delete() throws InterruptedException {

        // db logic
        Thread.sleep(1000 * 2); // 2초 있다가 종료되도록 설정
    }

    @Decode // 메서드 실행 전과 반환될 때 인자의 특정 데이터 값 변경
    @PutMapping("/put")
    public User put(@RequestBody User user){
        // 메서드가 실행되기 전에는 encoded data를 Decoding해서 출력
        System.out.println("put");
        System.out.println(user);
        // 값이 외부로 반환될 때는 다시 encoding 형태로 출력
        return user;
    }
}

