package com.example.swagger.controller;


import com.example.swagger.dto.UserReq;
import com.example.swagger.dto.UserRes;
import io.swagger.annotations.*;
import org.springframework.web.bind.annotation.*;

@Api(tags={"API 정보를 제공하는 Controller"}) // tags : swagger-ui에서 컨트롤러 제목 설정
@RestController
@RequestMapping("/api")
public class ApiController {

    @GetMapping("/hello")
    public String hello(){
        return "hello";
    }

    @ApiImplicitParams({
                    @ApiImplicitParam(name = "x", value = "x 값", required = true, dataType = "int", paramType = "path"),
                    @ApiImplicitParam(name = "y", value = "y 값", required = true, dataType = "int", paramType = "query"),
    })
    @GetMapping("/plus")
    public int plus(@RequestParam int x, @RequestParam int y){
        return x + y;
    }

    @ApiResponse(code = 502, message = "사용자의 나이가 10살 이하일 때")
    @ApiOperation(value = "사용자의 이름과 나이를 RETURN하는 메서드")
    @GetMapping("/user")
    public UserRes user(UserReq userReq){
        return new UserRes(userReq.getName(), userReq.getAge());
    }

    @PostMapping("/user")
    public UserRes userPost(@RequestBody UserReq req){
        return new UserRes(req.getName(), req.getAge());
    }


}
