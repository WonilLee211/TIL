package com.example.hello.GetApiController;

import com.example.hello.dto.UserRequest;
import org.springframework.web.bind.annotation.*;

import java.util.Map;

@RestController
@RequestMapping("/api/get")
public class GetApiController {

    @GetMapping(path="/hello") // http://localhost:9090/api/get/hello
    public String getHello(){
        return "get Hello";
    }

    // 예전 방식
    @RequestMapping(path = "/hi", method = RequestMethod.GET) // get // http://localhost:9090/api/get/hi
    public String hi(){
        return "hi";
    }

    // http://localhost:9090/api/get/path-variable/{name}
    @GetMapping(path="/path-variable/{name}")
    public String pathVariable(@PathVariable String name){ // url에 변수 가져오는 방법
//    public String pathVariable(@PathVariable(name = "name") String pathName){ // pathVariable name과 매개변수의 이름을 달리해야 할 때
        System.out.println("PathVariable : " + name);
//        System.out.println("PathVariable : " + pathName);
        return name;
    }

    // 쿼리 파라미터
    // search?q=intellij
    // &oq=intellij
    // &aqs=chrome.0.69i59l6j69i60j69i61.5038j0j7
    // &sourceid=chrome
    // &ie=UTF-8

    // http://localhost:9090/api/get/query-param?user=steve&email=steve@gmail.com&age=30

    // query parameter 받아오는 방법 1
    @GetMapping(path="/query-param")
    public String queryParam(@RequestParam Map<String, String> queryParam) { // query parameter 연결시키는 annotation

        StringBuilder sb = new StringBuilder();

        // entrySet() : Map자료형에서 key, value값이 모둔 필요한 경우 사용
        queryParam.entrySet().forEach(entry -> {
            System.out.println(entry.getKey());
            System.out.println(entry.getValue());
            System.out.println("\n");

            sb.append(entry.getKey() + " + " + entry.getValue() + "\n" );

        });
        return sb.toString();
    }
    // query parameter 받아오는 방법 2
    @GetMapping("/query-param02")
    public String queryParam02(
            @RequestParam String user,
            @RequestParam String email,
            @RequestParam int age
    ){
        System.out.println(user);
        System.out.println(email);
        System.out.println(age);

        return user + " " + email + " " + age;
    }

    // query parameter 받아오는 방법 3 (가장 많이 쓰는 방법)
    // dto 폴더에 UserRequest 선언
    @GetMapping("query-param03")
    public String queryParam03(UserRequest userRequest){
        System.out.println(userRequest.getUser());
        System.out.println(userRequest.getEmail());
        System.out.println(userRequest.getAge());

        return userRequest.getUser() + " " + userRequest.getEmail() + " " + userRequest.getAge();

    }
}
