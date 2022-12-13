package com.example.post.controller;

import com.example.post.dto.PostRequestDto;
import org.springframework.web.bind.annotation.*;

import java.util.Map;

@RestController
@RequestMapping("/api")
public class PostApiController {
    @PostMapping("/post")
    public void post(@RequestBody Map<String, Object> requestMap){ // 바디에 보내지는 데이터 매핑하는 annotation

        requestMap.forEach((key, value) -> {
            System.out.println("key : " + key);
            System.out.println("value : " + value);

        });
    }
//    key : account
//    value : user01
//    key : email
//    value : steve@gmail.com
//    key : address
//    value : 패스트캠퍼스
//    key : password
//    value : pw01

    @PostMapping("/post-dto")
    public void post(@RequestBody PostRequestDto postRequestDto){
        System.out.println(postRequestDto.toString());
    }
//    PostRequestDto{account='user01', email='steve@gmail.com', address='패스트캠퍼스', password='pw01'}
//    PostRequestDto{account='user01', email='steve@gmail.com', address='패스트캠퍼스', password='pw01', phoneNumber='01012345678'}
    // 카멜 케이스로 변경됨
//    PostRequestDto{account='user01', email='steve@gmail.com', address='패스트캠퍼스', password='pw01', phoneNumber='01012345678', OTP='132345'}


}
