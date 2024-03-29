package com.example.async.controller;

import com.example.async.Service.AsyncService;
import lombok.extern.slf4j.Slf4j;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.concurrent.CompletableFuture;


@Slf4j
@RestController
@RequestMapping("/api")
public class ApiController {


    private AsyncService asyncService;

    public ApiController(AsyncService asyncService) {
        this.asyncService = asyncService;
    }
    @GetMapping("/hello")
    public CompletableFuture hello(){
        log.info("completableFuture init");
        return asyncService.run();

    }


}
