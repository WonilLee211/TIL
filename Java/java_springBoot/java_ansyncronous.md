# 비동기

1. 어플리케이션에 `@EnableAsync` 달기

2. AsyncService

```java
package com.example.async.Service;

@Service
public class AsyncService {

    @Async // 해당 메소드가 끝날때까지 기다리지 않음
    public void hello() {

        for (int i = 0; i < 10; i++) {
            try {
                Thread.sleep(2000);
                System.out.println("Thread sleep");

            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

    }
}

```

3. ApiController

```java
package com.example.async.controller;

@RestController
@RequestMapping("/api")
public class ApiController {


    private AsyncService asyncService;

    public ApiController(AsyncService asyncService) {
        this.asyncService = asyncService;
    }
    @GetMapping("/hello")
    public String hello(){
        asyncService.hello();
        System.out.println("method end");
        return "hello";
    }
}

// method end
// Thread sleep
// Thread sleep
// Thread sleep
// Thread sleep
// Thread sleep
// Thread sleep
// Thread sleep
// Thread sleep
// Thread sleep
// Thread sleep
```

- ApiController에서 hello메소드가 끝날때 까지 기다리지 않고 비동기 수행


## 추가학습

```java
package com.example.async.config;

@Configuration
public class AppConfig {

    @Bean("async-thread")
    public Executor asyncThread(){
        ThreadPoolTaskExecutor threadPoolTaskExecutor = new ThreadPoolTaskExecutor();
        threadPoolTaskExecutor.setMaxPoolSize(100);
        threadPoolTaskExecutor.setCorePoolSize(10);
        threadPoolTaskExecutor.setQueueCapacity(10);
        threadPoolTaskExecutor.setThreadNamePrefix("Async~");
        return threadPoolTaskExecutor;
    }
}


```
```java
package com.example.async.controller;

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


```
```java

package com.example.async.Service;

@Slf4j
@Service
public class AsyncService {

    @Async("async-thread")
    public CompletableFuture run(){
        return new AsyncResult(hello()).completable();
    }

    @Async // 해당 메소드가 끝날때까지 기다리지 않음
    public String hello() {

        for (int i = 0; i < 10; i++) {
            try {
                Thread.sleep(2000);

                log.info("Thread sleep");

            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        return "async hello";
    }
}

```
 
```java
package com.example.async;

@SpringBootApplication
@EnableAsync
public class AsyncApplication {
	public static void main(String[] args) {
		SpringApplication.run(AsyncApplication.class, args);
	}

}

```