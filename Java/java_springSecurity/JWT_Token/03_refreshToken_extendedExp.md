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
    - AUTH_TIME을 짧게 유지하고 REFRESH_TIME 내에 토큰이 재발행되는지 확인하기

```java
package com.sp.fc.web.config;

/*
JWT 서비스를 구현하기
1. JWT 토큰을 발행하고 검증하는 유틸리티가 필요함
 */


public class JWTUtil {
    // 동일한 알고리즘과 서명을 가지고 테스트
    private static final Algorithm algorithm = Algorithm.HMAC256("wonil");
    private static final long AUTH_TIME = 2; // JWT expiration = 2초
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

    // 토큰 유효성 검사_ 토큰 검증 성공 여부 및 유저 이름을 가진 verifyResult return
    public static VerifyResult verify (String token){
        try{

            // 토큰 유효성 검사 
            DecodedJWT verify = JWT.require(algorithm).build().verify(token);

            // 유효성 검사 성공 시 코드
            return VerifyResult.builder()
                    .success(true)
                    .username(verify.getSubject())
                    .build();

        }catch (Exception e){

            // 토큰 유효성 실패 시 코드
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

- 토큰이 잘 유통되는지 확인

### 1. controller

- 메소드 실행 전 권한 검증이 필요함
- 인증조건 : 로그인 여부


```java
package com.sp.fc.web.controller;

@RestController
public class HomeController {

    @PreAuthorize("isAuthenticated()") // 인증조건 : 로그인 여부
    @GetMapping("/greeting")
    public String greeting(){
        return "hello";
    }

}

```

- MethodSecurity 사용하고 filter chain을 커스텀하기 위해 SecurityConfig 설정 클래스 만들어야 함


### 2. `SecurityConfig extends WebSecurityConfigurerAdapter`

- 인증&인가 API를 만들어서 보안성 높힘
- `WebSecurityConfigurerAdapter` : 스프링 시큐리티의 웹 보안 기능 초기화 및 설정

    - `configure(HttpSecurity httpSecurity)`
        - 웹 보안의 filter chain을 커스텀할 수 있음
    
- `@EnableWebSecurity` : 웹보안 활성화를위한 annotation
    - @EnableWebSecurity 애노테이션을 WebSecurityconfigurerAdapter 를 상속하는 설정 객체에 붙혀주면 **SpringSecurityFilterChain에 등록된다.**
- `@EnableGlobalMethodSecurity` : controller 메서드에 직접 롤을 부여할 수 있음
    - `prePostEnabled` : `@PreAuthorize` annotation을 사용 여부 결정 옵션





> ### 주의 csrf.disable
>  rest api를 이용한 서버라면, session 기반 인증과는 다르게 stateless하기 때문에 서버에 인증정보를 보관하지 않는다. rest api에서 client는 권한이 필요한 요청을 하기 위해서는 요청에 필요한 인증 정보를(OAuth2, jwt토큰 등)을 포함시켜야 한다. 따라서 서버에 인증정보를 저장하지 않기 때문에 굳이 불필요한 csrf 코드들을 작성할 필요가 없다.

<br>

```java
package com.sp.fc.web.config;

@EnableWebSecurity
@EnableGlobalMethodSecurity(prePostEnabled = true)
public class AdvancedSecurityConfig extends WebSecurityConfigurerAdapter {

    @Autowired
    private SpUserService userService;

    @Bean
    PasswordEncoder passwordEncoder(){
        return NoOpPasswordEncoder.getInstance();
    }

    @Override
    protected void configure(HttpSecurity http) throws Exception {
        // 로그인할 때 적용될 필터
        JWTLoginFilter loginFilter = new JWTLoginFilter(authenticationManager(), userService);
        // 로그인된 토큰을 request마다 검증해줄 필터
        JWTCheckFilter checkFilter = new JWTCheckFilter(authenticationManager(), userService);
        
        http
                .csrf().disable()
                .sessionManagement(session->
                        session.sessionCreationPolicy(SessionCreationPolicy.STATELESS)
                )
                // 필터들 적용시키기. 구현한 필터를 필터 체인의 특정 위치에 입력시킨다는 의미
                .addFilterAt(loginFilter, UsernamePasswordAuthenticationFilter.class)
                .addFilterAt(checkFilter, BasicAuthenticationFilter.class)
                ;

    }
}

```

### 인증을 위해 필요한 2가지 filter를 만들어야 함

1. `JWTLoginFilter` : 로그인 처리 필터

    - 사용자가 유효한 사용자임을 증명한 다음 authentication을 발행해줘야 하는 역할
    - `UsernamePasswordAuthenticationFilter`를 상속받아서 구현해도 됨. 역할이 비슷하기 때문에
    
        - authenticationManager를 받는 생성자를 만들어야 함
            - 유저 검증을 authenticationManager에게 위임함
        - attemptAuthentication 함수에서 사용자 인증을 처리하게 됨

    - **로직**

        1. `JWTLoginFilter`의 `attemptAuthentication` 메서드로 넘어옴
        2. token을 만듦
        3. AuthenticationManager에게 token을 검증해달라고 요청을 보냄
        4. AuthenticationProvider를 통해서 UserDetailService를 상속한 SpUserService에게 token의 password를 검증 요청함
            - SpUserService는 userRepository에서 계정정보를 조회하여 검증
        5. UserLoginForm에 refresh token이 있다면 토큰 갱신 요청임
            1. refresh token이 유효하다면, 토큰을 재갱신함
            2. authenticationManager에 위임하지 않고 직접 토큰 생성 후 발급
            3. refresh token이 유효하지 않다면 throw TokenExpiredException("")

        6. 로그인을 성공하면 successfulAuthentication 메서드로 request가 전달됨
            1. 전달되는 인자로 authResult에 principal이 담겨있음
            2. header의 context 타입을 json value로 정하고 해당 정보를 response에 writeValueAsBytes.
            
<br>

```java

package com.sp.fc.web.config;

public class JWTLoginFilter extends UsernamePasswordAuthenticationFilter {

    private ObjectMapper objectMapper = new ObjectMapper();
    private SpUserService userService;

    public JWTLoginFilter(AuthenticationManager authenticationManager, SpUserService userService) {
        super(authenticationManager);
        this.userService = userService;
        setFilterProcessesUrl("/login"); // 꼭 필요한건 아니지만 명시해주기
    }

    // 로그인 요청 시 request가 JWTLoginFilter를 만나 attemptAuthencation으로 오게 됨
    @SneakyThrows
    @Override
    public Authentication attemptAuthentication(
            HttpServletRequest request,
            HttpServletResponse response) throws AuthenticationException
    {
        // deserialize
        UserLoginForm userLogin = objectMapper.readValue(request.getInputStream(), UserLoginForm.class);
        // 로그아웃 상태였을 경우
        if(userLogin.getRefreshToken() == null){
            UsernamePasswordAuthenticationToken token = new UsernamePasswordAuthenticationToken(
                    userLogin.getUsername(), userLogin.getPassword(), null);

            // AuthentcationManager에게 token을 검증해달라고 요청을 보냄
            // AuthenticationProvider를 통해서 UserDetailService를 상속한 SpUserService에게 token의 password를 검증 요청함
            // SpUserService는 userRepository에서 계정정보를 조회하여 검증
            return getAuthenticationManager().authenticate(token);
        }
        // 리프레쉬 토큰이 있다는 뜻은 토큰을 갱신해달라는 의미
        else {
            VerifyResult verify = JWTUtil.verify(userLogin.getRefreshToken());
            // freshToken이 유효하다면 
            if(verify.isSuccess()){
                // 이번엔 authenticationManager에게 login을 위임하지 않고 직접 토큰 만들기
                SpUser user = (SpUser) userService.loadUserByUsername(verify.getUsername());
                // principal과 authorities를 넣어 토큰 생성
                return new UsernamePasswordAuthenticationToken(
                        user, user.getAuthorities()
                );

            }else {
                throw new TokenExpiredException("refresh token is expired");
            }
        }
        // user details...
    }

    // 로그인을 성공하면 successfulAuthentication 메서드로 request가 전달됨
    @Override
    protected void successfulAuthentication(
            HttpServletRequest request,
            HttpServletResponse response,
            FilterChain chain,
            Authentication authResult) throws IOException, ServletException
    {
    //     로그인을 성공하면 successfulAuthentication 메서드로 request가 전달됨
    //         1. 전달되는 인자로 authResult에 principal이 담겨있음
        SpUser user = (SpUser) authResult.getPrincipal();
        // response에 auth-token, refresh-token 담아주기. 
        response.setHeader("auth_token", JWTUtil.makeAuthToken(user));
        response.setHeader("refresh_token", JWTUtil.makeRefreshToken(user));
    //         2. header의 context 타입을 json value로 정하고 해당 정보를 response에 writeValueAsBytes.
        response.setHeader(HttpHeaders.CONTENT_TYPE, MediaType.APPLICATION_JSON_VALUE);
        response.getOutputStream().write(objectMapper.writeValueAsBytes(user));
    }
}

```
<br>

2. `JWTCheckFilter` : 요청마다 로그인 상태를 확인할 필터

    - 토큰을 검사해서 SecurityContextHolder 내에 user의 principal를 채워주는 역할
    - BasicAuthenticationFilter가 비슷한 역할을 하기 때문에 상속받아서 구현하기
    - JWTLoginFilter와 달리 직접 사용자 정보를 검증해야 하기 때문에 사용자 정보를 가져올 UserService가 필요함

    - **로직**
        1. 두번째 request부터 JWTCheckFilter를 거치게 됨
        2. doFilterInternal 메서드로 request 전달됨
        3. request에서 HttpHeader의 AUTHORIZATION에 담겨있는 Bearer 토큰을 조사함
        4. Bearer가 없거나 Bearer 토큰이 아닌 경우 그냥 흘려보내줘야 함
            - 검증이 필요하지 않은 경우가 있을 수 있고, 다음 로직에서 다시 로그인을 해야하는 경우 일 수도 있기 때문
        5. Bearer 토큰이 있는 경우, token을 검증
        6. 토큰이 검증됐다면 토큰을 직접 만들어서 갱신시켜서 SecurityContextHolder에 넣기
        7. 토큰이 검증 실패했다면 AuthenticationException 발생


```java

package com.sp.fc.web.config;

public class JWTCheckFilter extends BasicAuthenticationFilter {

    private SpUserService userService;

    public JWTCheckFilter(AuthenticationManager authenticationManager, SpUserService userService) {
        super(authenticationManager);
        this.userService = userService;
    }

    @Override
    protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain chain) throws IOException, ServletException {
        String bearer = request.getHeader(HttpHeaders.AUTHORIZATION);

        //Bearer가 없거나 Bearer 토큰이 아닌 경우 그냥 흘려보내줘야 함
        if(bearer == null || !bearer.startsWith("Bearer ")){
            chain.doFilter(request, response);
            return;
        }

        // Bearer 토큰이 있는 경우, token을 검증
        String token = bearer.substring("Bearer ".length());
        
        VerifyResult result = JWTUtil.verify(token);
        if(result.isSuccess()){
            //토큰이 검증됐다면 토큰을 직접 만들어서 갱신시켜서 SecurityContextHolder에 넣기
            SpUser user = (SpUser) userService.loadUserByUsername(result.getUsername());
            UsernamePasswordAuthenticationToken userToken = new UsernamePasswordAuthenticationToken(
                    user.getUsername(), null, user.getAuthorities()
            );
            SecurityContextHolder.getContext().setAuthentication(userToken);
            chain.doFilter(request, response); // filter chain 통행시킴

        }else{
            //토큰이 검증 실패했다면 AuthenticationException 발생
            throw new AuthenticationException("Token is not valid");
        }
    }

}

```
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
- test1 code

    1. client 로그인 시도
    2. post method로 username, password를 전달해야 함
        - UserLoginForm
            ```java
            package com.sp.fc.web.config;

            @Data
            @AllArgsConstructor
            @NoArgsConstructor
            @Builder
            public class UserLoginForm {

                private String username;
                private String password;
                private String refreshToken;

            }

            ```
    3. request를 날리면 filter chain을 타고 가던 request가 `JWTLoginFilter`를 만남
    4. token을 발행받은 후 get 요청 - 두번째 request
    5. JWTCheckFilter를 타게 됨
    6. 이 후 요청 결과값 확인

- TokenBox

```java
package com.sp.fc.web;

@Data
@AllArgsConstructor
@NoArgsConstructor
@Builder
public class TokenBox {

    private String authToken;
    private String refreshToken;

}

```

```java

package com.sp.fc.web;

public class JWTRequestTest extends WebIntegrationTest {


    @Autowired
    private SpUserRepository userRepository;

    @Autowired
    private SpUserService userService;

    // 테스트를 위한 유저 등록해두기
    @BeforeEach
    void before(){
        userRepository.deleteAll(); // 사용하기전 항상 clear한 후 사용해야 함

        // 유저 계정에 필수 정보를 사전에 입력해두기
        SpUser user = userService.save(SpUser.builder()
                .email("user1")
                .password("1111")
                .enabled(true)
                .build());
        userService.addAuthority(user.getUserId(), "ROLE_USER");
    }
    
    // 사용자 로그인 요청 후 발급받은 토큰 반환하는 메서드(안전하지 않은 방법)
    private TokenBox getToken(){

        RestTemplate client = new RestTemplate();

        HttpEntity<UserLoginForm> body = new HttpEntity<>(
                UserLoginForm.builder().username("user1").password("1111").build()
        );

        // request를 날리면 filter chain을 타고 가던 request가 JWTLoginFilter를 만남
        ResponseEntity<SpUser> resp1 = client.exchange(uri("/login"), HttpMethod.POST, body, SpUser.class);
        // 두가지 토근으 담을 값을 반환해줌
        return TokenBox.builder()
                .authToken(resp1.getHeaders().get("auth_token").get(0))
                .refreshToken(resp1.getHeaders().get("refresh_token").get(0))
                .build();

    }

    // 토큰 갱신 요청 메서드
    private TokenBox refreshToken(String refreshToken){

        RestTemplate client = new RestTemplate();

        HttpEntity<UserLoginForm> body = new HttpEntity<>(
                UserLoginForm.builder().refreshToken(refreshToken).build()
        );

        ResponseEntity<SpUser> resp1 = client.exchange(uri("/login"), HttpMethod.POST, body, SpUser.class);
        return TokenBox.builder()
                .authToken(resp1.getHeaders().get("auth_token").get(0))
                .refreshToken(resp1.getHeaders().get("refresh_token").get(0))
                .build();

    }


    @DisplayName("1. hello 메시지를 받아온다... ")
    @Test
    void test_1(){

        TokenBox token = getToken(); // auth_token, refresh_token이 담겨있음

        RestTemplate client = new RestTemplate();
        HttpHeaders header = new HttpHeaders();
        header.add(HttpHeaders.AUTHORIZATION, "Bearer " + token); // Bearer : 서버쪽에서 필요한 양식
        HttpEntity body = new HttpEntity<>(null, header);

        ResponseEntity<String> resp2 = client.exchange(uri("/greeting"), HttpMethod.GET, body, String.class);

        assertEquals("hello", resp2.getBody());

    }


}
```

<br>

- test2 코드

1. 로직
    1. refreshToken만을 UserLoginForm에 담아서 Login 요청보내기
    2. JWTLoginFilter를 타게 됨
    3. 

```java
package com.sp.fc.web;

public class JWTRequestTest extends WebIntegrationTest {


    @Autowired
    private SpUserRepository userRepository;

    @Autowired
    private SpUserService userService;

    @BeforeEach
    void before(){
        userRepository.deleteAll();

        SpUser user = userService.save(SpUser.builder()
                .email("user1")
                .password("1111")
                .enabled(true)
                .build());
        userService.addAuthority(user.getUserId(), "ROLE_USER");
    }

    private TokenBox getToken(){

        RestTemplate client = new RestTemplate();

        HttpEntity<UserLoginForm> body = new HttpEntity<>(
                UserLoginForm.builder().username("user1").password("1111").build()
        );

        ResponseEntity<SpUser> resp1 = client.exchange(uri("/login"), HttpMethod.POST, body, SpUser.class);
        return TokenBox.builder()
                .authToken(resp1.getHeaders().get("auth_token").get(0))
                .refreshToken(resp1.getHeaders().get("refresh_token").get(0))
                .build();

    }

    // 토큰 갱신 요청 메서드
    private TokenBox refreshToken(String refreshToken){

        RestTemplate client = new RestTemplate();
        // userLoginForm에 refreshToken만 담아서 로그인 보내기
        HttpEntity<UserLoginForm> body = new HttpEntity<>(
                UserLoginForm.builder().refreshToken(refreshToken).build()
        );

        ResponseEntity<SpUser> resp1 = client.exchange(uri("/login"), HttpMethod.POST, body, SpUser.class);
        return TokenBox.builder()
                .authToken(resp1.getHeaders().get("auth_token").get(0))
                .refreshToken(resp1.getHeaders().get("refresh_token").get(0))
                .build();
    }


    @DisplayName("2. 토큰 만료 테스트")
    @Test
    void test_2() throws InterruptedException {
        TokenBox token = getToken();


        // AUTH_TIME을 지나도록 설정
        Thread.sleep(3000);
        HttpHeaders header = new HttpHeaders();
        header.add(HttpHeaders.AUTHORIZATION, "Bearer " + token.getAuthToken());

        RestTemplate client = new RestTemplate();
        // 서버쪽 exception을 받게 됨
        assertThrows(Exception.class, ()->{
            HttpEntity body = new HttpEntity<>(null, header);
            ResponseEntity<String> resp2 = client.exchange(uri("/greeting"), HttpMethod.GET, body, String.class);
        });

        // exception이 발생하면 refresh token 요청을 보냄
        token = refreshToken(token.getRefreshToken());
        // 다시 header를 만들고
        HttpHeaders header2 = new HttpHeaders();
        header2.add(HttpHeaders.AUTHORIZATION, "Bearer " + token.getAuthToken());
        HttpEntity body = new HttpEntity<>(null, header2);
        // resource 재요청
        ResponseEntity<String> resp3 = client.exchange(uri("/greeting"), HttpMethod.GET, body, String.class);

        assertEquals("hello", resp3.getBody());
    }




}


```