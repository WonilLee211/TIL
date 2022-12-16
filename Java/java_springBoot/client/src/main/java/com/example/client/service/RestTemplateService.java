package com.example.client.service;

import com.example.client.dto.Req;
import com.example.client.dto.UserRequest;
import com.example.client.dto.UserResponse;
import org.springframework.core.ParameterizedTypeReference;
import org.springframework.http.MediaType;
import org.springframework.http.RequestEntity;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;
import org.springframework.web.util.UriComponentsBuilder;

import java.net.URI;

@Service
public class RestTemplateService {
    // http://localhost:9090/api/server/hello
    // response

    public UserResponse hello(){
        URI uri = UriComponentsBuilder
                .fromUriString("http://localhost:9090")
                .path("/api/server/hello")
                .queryParam("name","steve")
                .queryParam("age",  10)
                .encode()
                .build()
                .toUri();
        System.out.println(uri.toString());

        RestTemplate restTemplate = new RestTemplate();
        ResponseEntity<UserResponse> result = restTemplate.getForEntity(uri, UserResponse.class);

        System.out.println(result.getStatusCode());
        System.out.println(result.getBody());
        return result.getBody();

    }

    public void post(){
        //http://localhost:9090/api/server/user/{userId}/name/{userName}
        // 1. uri만들기
        URI uri = UriComponentsBuilder
                .fromUriString("http://localhost:9090")
                .path("/api/server/user/{userId}/name/{userName}")
                .encode() // uri를 safe하게 만드는 역할
                .build()
                .expand(100, "steve")
                .toUri();
        System.out.println(uri);


        // 2. 요청보낼 데이터 만들기
        // http body -> object -> object mapper -> json -> rest template -> http body json
        // 요청보낼 양식
        UserRequest req = new UserRequest();
        req.setName("steve");
        req.setAge(100);

        // 3. 요청보내기
        RestTemplate restTemplate = new RestTemplate();
        ResponseEntity<String> response = restTemplate.postForEntity(uri, req, String.class); // 보낼 곳의 uri, 보낼 정보, 받은 데이터 형태
        // 4. 데이터 받기
        System.out.println(response.getStatusCode());
        System.out.println(response.getHeaders());
        System.out.println(response.getBody());

//        return response.getBody();

    }


    public UserResponse exchange(){
        URI uri = UriComponentsBuilder
                .fromUriString("http://localhost:9090")
                .path("/api/server/user/{userId}/name/{userName}")
                .encode() // uri를 safe하게 만드는 역할
                .build()
                .expand(100, "steve")
                .toUri();
        System.out.println(uri);


        // 2. 요청보낼 데이터 만들기
        // http body -> object -> object mapper -> json -> rest template -> http body json
        // 요청보낼 양식
        UserRequest req = new UserRequest();
        req.setName("steve");
        req.setAge(100);

        RequestEntity<UserRequest> requestEntity = RequestEntity
                .post(uri)
                .contentType(MediaType.APPLICATION_JSON)
                .header("X-authorization", "abcd")
                .header("custom-header", "fffff")
                .body(req);

        // 3. 헤더 실어서 요청보내기
        RestTemplate restTemplate = new RestTemplate();
        ResponseEntity<UserResponse> response = restTemplate.exchange(requestEntity, UserResponse.class);

        return response.getBody();
    }

    public Req<UserResponse> genericExchange(){

        URI uri = UriComponentsBuilder
                .fromUriString("http://localhost:9090")
                .path("/api/server/user/{userId}/name/{userName}")
                .encode() // uri를 safe하게 만드는 역할
                .build()
                .expand(100, "steve")
                .toUri();
        System.out.println(uri);


        // 2. 요청보낼 데이터 만들기
        // http body -> object -> object mapper -> json -> rest template -> http body json


        // 요청보낼 양식
        UserRequest userRequest = new UserRequest();
        userRequest.setName("steve");
        userRequest.setAge(100);

        Req req = new Req();
        req.setHeader(new Req.Header());
        req.setResBody(userRequest);


        RequestEntity<Req<UserRequest>> requestEntity = RequestEntity
                .post(uri)
                .contentType(MediaType.APPLICATION_JSON)
                .header("X-authorization", "abcd")
                .header("custom-header", "fffff")
                .body(req);

        RestTemplate restTemplate = new RestTemplate();

//        ResponseEntity<Req<UserResponse>> response
//                = restTemplate.exchange(requestEntity, Req<UserResponse>.class); // 에러
        // generic type에서는 class를 붙일 수 없음

        // ParameterizedTypeReference : 이때 사용하는 클래스
        ResponseEntity<Req<UserResponse>> response =
                restTemplate.exchange(requestEntity, new ParameterizedTypeReference<Req<UserResponse>>(){});

        return response.getBody();

    }
}
