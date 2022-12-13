package com.example.post.controller;

import com.example.post.dto.User;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class PageController {

    @RequestMapping("/main")
    public String main(){
        return "main.html";
    }

    //ResponseEntity
    @ResponseBody // 객체를 반환할 때 리소스를 찾지 않고 리스폰스바디를 만들어서 보내겠다는 annotation
    @GetMapping("/user")
    public User user(){
        // 타입 명시할 때 이름이 길면 추후헤 불편함. 그런한 불편함을 해소. java 11버전부터 제공
        var user = new User();
        user.setName("steve");
        user.setAddress("패스트 캠퍼스");

        return user;
    }
//    {
//        "name": "steve",
//            "age": 0,
//            "phone_number": null,
//            "address": "패스트 캠퍼스"
//    }

    // int 타입 Default 반환값 : 0
    // null을 반환하고 싶다면 Integeer 타입 사용
}
