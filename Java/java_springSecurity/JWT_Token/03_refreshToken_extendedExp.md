# Refresh Token

- Remember-me 토큰처럼 자동로그인을 하는데 사용합니다.
- 만료시간을 며칠 혹은 몇달로 줄 수 있습니다.
- 서버에 토큰을 저장하고 관리하는 것이 안전합니다.
- 이 경우, RememberMe 토큰을 관리했던 것처럼
  - `동시로그인을 허용하는 경우` : refreshToken 을 시리즈로 관리하는 방법이 있고,
  - `유저당 로그인을 한 디바이스로 제한하는 경우` : refresh token 과 access token 을 키로 사용해서 구현할 수 있습니다.
- 그 밖에 refresh 토큰을 허용할 경우, 보안에 취약한 점을 어떻게 보완할 것인지 고민해 보아야 합니다.

# JWT 서비스를 구현하기

1. 검증 결과 커스텀

```java
package com.sp.fc.web.config;

@Data
@AllArgsConstructor
@NoArgsConstructor
@Builder
public class VerifyResult {

    private boolean success;
    private String username;

}

```

<br> 

2. JWT 토큰을 발행하고 검증하는 유틸리티가 필요함

```java
package com.sp.fc.web.config;

/*
JWT 서비스를 구현하기
1. JWT 토큰을 발행하고 검증하는 유틸리티가 필요함
 */


public class JWTUtil {

    private static final Algorithm algorithm = Algorithm.HMAC256("wonil");
    private static final long AUTH_TIME = 20 * 60; // JWT expiration = 20분
    private static final long REFRESH_TIME = 60 * 60 * 24 * 7; // refresh token expiration : 일주일

    // authentication token, JWT 발행기
    public static String makeAuthToken(SpUser user){
        return JWT.create()
                .withSubject(user.getUsername())
                .withClaim("exp", Instant.now().getEpochSecond() + AUTH_TIME)
                .sign(algorithm);
    }

    // refresh token 발행기
    public static String makeRefreshToken(SpUser user){
        return JWT.create()
                .withSubject(user.getUsername())
                .withClaim("exp", Instant.now().getEpochSecond() + REFRESH_TIME)
                .sign(algorithm);
    }

    // 토큰 유효성 검사
    public static VerifyResult verify (String token){
        try{

            DecodedJWT verify = JWT.require(algorithm).build().verify(token);
            return VerifyResult.builder()
                    .success(true)
                    .username(verify.getSubject())
                    .build();

        }catch (Exception e){

            DecodedJWT decode = JWT.decode(token);
            return VerifyResult.builder()
                    .success(false)
                    .username(decode.getSubject())
                    .build();
        }

    }
}


```

<br>

## test 구현

### 1. controller
  - 메소드 실행 전 권한 검증이 필요함


```java
package com.sp.fc.web.controller;

@RestController
public class HomeController {

    @PreAuthorize("isAuthenticated()")
    @GetMapping("/greeting")
    public String greeting(){
        return "hello";
    }

}

```

### 2. MethodSecurity 사용하기 위해 SecurityConfig 설정 클래스 만들기

 - 인증&인가 API를 만들어서 보안성 높힘
 - `WebSecurityConfigurerAdapter` : 스프링 시큐리티의 웹 보안 기능 초기화 및 설정
 - `@EnableWebSecurity` : 웹보안 활성화를위한 annotation
   - @EnableWebSecurity 애노테이션을 WebSecurityconfigurerAdapter 를 상속하는 설정 객체에 붙혀주면 **SpringSecurityFilterChain에 등록된다.**
 - `@EnableGlobalMethodSecurity` : controller 메서드에 직접 롤을 부여할 수 있음
     - `prePostEnabled` : `@PreAuthorize` annotation을 사용 여부 결정 옵션

> ### 주의 csrf.disable
>  rest api를 이용한 서버라면, session 기반 인증과는 다르게 stateless하기 때문에 서버에 인증정보를 보관하지 않는다. rest api에서 client는 권한이 필요한 요청을 하기 위해서는 요청에 필요한 인증 정보를(OAuth2, jwt토큰 등)을 포함시켜야 한다. 따라서 서버에 인증정보를 저장하지 않기 때문에 굳이 불필요한 csrf 코드들을 작성할 필요가 없다.


### 인증을 위해 필요한 2가지 filter

1. `JWTLoginFilter` : 로그인 처리 필터
2. `JWTCheckFilter` : 요청마다 로그인 상태를 확인할 필터


```java


```


```java
package com.sp.fc.web.config;


@EnableWebSecurity // 웹보안 활성화를위한 annotation
@EnableGlobalMethodSecurity(prePostEnabled = true)
public class AdvancedSecurityConfig extends WebSecurityConfigurerAdapter {

}


```