# OAuth2

스프링은 OAuth2 에 대해 많은 기본 기능들을 제공합니다.

## CommonOAuth2Provider

아래 4개의 Provider 에 대해 기본 정보들을 제공합니다.

- GOOGLE : https://console.cloud.google.com/
- GITHUB : https://github.com/settings/applications/new
- FACEBOOK : https://developers.facebook.com/
- OKTA

> 위 사이트에서 웹 에플리케이션을 등록하고 클라이언트로 등록해야 함

### 내부 코드

- registrationId : 필수 입력 값
- registrationId를 가지고 redirect_url을 구성하게 됨
- 클라이언트를 등록할 때 필수적으로 입력해줘야 하는 부분 !

```java
/*
 * Copyright 2002-2020 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      https://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package org.springframework.security.config.oauth2.client;

/**
 * Common OAuth2 Providers that can be used to create
 * {@link org.springframework.security.oauth2.client.registration.ClientRegistration.Builder
 * builders} pre-configured with sensible defaults.
 *
 * @author Phillip Webb
 * @since 5.0
 */
public enum CommonOAuth2Provider {

	GOOGLE {

		@Override
		public Builder getBuilder(String registrationId) {
			ClientRegistration.Builder builder = getBuilder(registrationId, ClientAuthenticationMethod.BASIC,
					DEFAULT_REDIRECT_URL);
			builder.scope("openid", "profile", "email");
			builder.authorizationUri("https://accounts.google.com/o/oauth2/v2/auth");
			builder.tokenUri("https://www.googleapis.com/oauth2/v4/token");
			builder.jwkSetUri("https://www.googleapis.com/oauth2/v3/certs");
			builder.issuerUri("https://accounts.google.com");
			builder.userInfoUri("https://www.googleapis.com/oauth2/v3/userinfo");
			builder.userNameAttributeName(IdTokenClaimNames.SUB);
			builder.clientName("Google");
			return builder;
		}

	},

	GITHUB {

		@Override
		public Builder getBuilder(String registrationId) {
			ClientRegistration.Builder builder = getBuilder(registrationId, ClientAuthenticationMethod.BASIC,
					DEFAULT_REDIRECT_URL);
			builder.scope("read:user");
			builder.authorizationUri("https://github.com/login/oauth/authorize");
			builder.tokenUri("https://github.com/login/oauth/access_token");
			builder.userInfoUri("https://api.github.com/user");
			builder.userNameAttributeName("id");
			builder.clientName("GitHub");
			return builder;
		}

	},

	FACEBOOK {

		@Override
		public Builder getBuilder(String registrationId) {
			ClientRegistration.Builder builder = getBuilder(registrationId, ClientAuthenticationMethod.POST,
					DEFAULT_REDIRECT_URL);
			builder.scope("public_profile", "email");
			builder.authorizationUri("https://www.facebook.com/v2.8/dialog/oauth");
			builder.tokenUri("https://graph.facebook.com/v2.8/oauth/access_token");
			builder.userInfoUri("https://graph.facebook.com/me?fields=id,name,email");
			builder.userNameAttributeName("id");
			builder.clientName("Facebook");
			return builder;
		}

	},

	OKTA {

		@Override
		public Builder getBuilder(String registrationId) {
			ClientRegistration.Builder builder = getBuilder(registrationId, ClientAuthenticationMethod.BASIC,
					DEFAULT_REDIRECT_URL);
			builder.scope("openid", "profile", "email");
			builder.userNameAttributeName(IdTokenClaimNames.SUB);
			builder.clientName("Okta");
			return builder;
		}

	};

	private static final String DEFAULT_REDIRECT_URL = "{baseUrl}/{action}/oauth2/code/{registrationId}";

	protected final ClientRegistration.Builder getBuilder(String registrationId, ClientAuthenticationMethod method,
			String redirectUri) {
		ClientRegistration.Builder builder = ClientRegistration.withRegistrationId(registrationId);
		builder.clientAuthenticationMethod(method);
		builder.authorizationGrantType(AuthorizationGrantType.AUTHORIZATION_CODE);
		builder.redirectUri(redirectUri);
		return builder;
	}

	/**
	 * Create a new
	 * {@link org.springframework.security.oauth2.client.registration.ClientRegistration.Builder
	 * ClientRegistration.Builder} pre-configured with provider defaults.
	 * @param registrationId the registration-id used with the new builder
	 * @return a builder instance
	 */
	public abstract ClientRegistration.Builder getBuilder(String registrationId);

}


```

## 추가 가능한 OAuth2Provider ...

- naver : https://developers.naver.com/
- kakao : https://developers.kakao.com/

## OAuth2User

- facebook, naver, kakao
- OAuth2User : UserDetails 를 대체합니다.
- OAuth2UserService : UserDetailsService 를 대체합니다. 기본 구현체는 DefaultOAuth2UserService 입니다.

<img src="../images/fig-36-oauth2-service.png" width="500" style="max-width:500px;width:100%;" />

## sns회원가입 메커니즘

1. 인증 제공자는 서비스 서버를 OAuth2 서비스를 이용할 수 있는 대상으로 등록함
2. 서비스 이용자가 SNS 회원가입을 시도함
3. OAuth2 인증 제공자(리소스 서버)에서 서비스 이용자에게 **리소스 제공 동의**를 얻고, **서비스 이용자에세 key를 전달**
4. 서비스 이용자가 서비스 서버에 key 전달
5. 리소스 서버에 서비스 이용자의 리소스 요청
6. 서비스 이용자의 리소스를 통해 회원가입 진행

## OidcUser

- google
- OidcUser
- OAuth2 Provider을 기반으로 진 일보한 인증 방식
- OidcUserService : **OAuth2UserService 를 확장한 서비스**


# 구현

## 1. setting

### oAuth2 등록하기

- build.gradle
	- oauth2 library 불러오기

```gradle

apply from: "../web-common.gradle"

dependencies {
	
    implementation("$boot:spring-boot-starter-oauth2-client")

    implementation("com.h2database:h2")

    implementation(project(":comp-user-admin"))
}

```
<br>

- application.yml
	- client의 registration 정보 입력하기
	- 등록정보
		1. provider
		2. clientId
		3. clientSecret

```yml

server:
  port: 9061


spring:
  security:
    oauth2:
      client:
        registration:
          google: # 클라이언트 정보 등록하기
            client-id: 377825014181-2tpha7niq0hjar86e4j8h6dl0h8j1s3i.apps.googleusercontent.com
            client-secret: yyHXhXWBRrx3jyDWrhiSwzu8
#          facebook:
#            client-id: 1108041866346884
#            client-secret: f52f8eaab7cdd0272d37ab89e0335be1
#          kakao:
#            client-id: fa84d469d8038b6a422d1f9b2b6f9067
#            client-secert: RuubX7J4HuhrekWplEeu2FnlSMiCftHH
#            redirect-uri: '{baseUrl}/login/oauth2/code/{registrationId}'
#            authorization-grant-type: authorization_code
#            client-name: kakao
          naver:
            client-id: bkdZjYp4EfmqIkZaEtqi
            client-secret: YLHoiLkdSy
            redirect-uri: '{baseUrl}/login/oauth2/code/{registrationId}'
            authorization-grant-type: authorization_code
            client-name: naver
		# CommonOAuth2Provider에 등록되지 않은 provider는 별도로 등록해줘야 함
        provider:
#          kakao:
#            authorization-uri: https://kauth.kakao.com/oauth/authorize
#            token-uri: https://kauth.kakao.com/oauth/token
#            user-info-uri: https://kapi.kakao.com/v2/user/me
#            user-name-attribute: id
          naver:
            authorization-uri: https://nid.naver.com/oauth2.0/authorize
            token-uri: https://nid.naver.com/oauth2.0/token
            user-info-uri: https://openapi.naver.com/v1/nid/me
            user-name-attribute: response

```

## 2. 로그인 인증 설정

- PreAuthorize로 method security 과정을 거치게 됨
- WebSecurityConfigurerAdapter를 상속한 config에서 구현된 configure 메소드에 httpSecurity 인자가 전달죔
- 해당인자의 request 유저 정보를 확인 검증
- 검증되면 oauth2 login 처리함.


```java
package com.sp.fc.web.controller;


@RestController
public class HomeController {

    @PreAuthorize("isAuthenticated()")
    @GetMapping("/")
    public Object greeting(@AuthenticationPrincipal Object user){ // 로그인을 성공하면 OAuth2 로그인된 고객정보가 인자로 전달됨
        return user;
    }

    @PreAuthorize("isAuthenticated()")
    @GetMapping("/user")
    public SpUser greeting(@AuthenticationPrincipal SpUser user){
        return user;
    }
}

```
<br>

- `SnsLoginSecurityConfig`

```java
package com.sp.fc.web.config;

@EnableWebSecurity
@EnableGlobalMethodSecurity(prePostEnabled = true)
public class SnsLoginSecurityConfig extends WebSecurityConfigurerAdapter {


    @Autowired
    private SpUserService userService;

    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http
                .oauth2Login();
    }
}


```

## sns 로그인 사용자의 UserLoginService 구현하기

### `UserInfoEndPoint`

- OAuth2, Oidc 유저를 sns 사이트로부터 받았을 때 유저서비스를 처리해주는 곳
	- 예를 들어 해당 고객 정보가 db에 없다면 회원가입시키는 서비스를 처리할 수도 있음

```java
package com.sp.fc.web.config;

@EnableWebSecurity
@EnableGlobalMethodSecurity(prePostEnabled = true)
public class SnsLoginSecurityConfig extends WebSecurityConfigurerAdapter {


    @Autowired
    private SpUserService userService;

    @Autowired
    private SpOAuth2UserService oAuth2UserService;

    @Autowired
    private SpOidcUserService oidcUserService;

    @Bean
    PasswordEncoder passwordEncoder(){
        return NoOpPasswordEncoder.getInstance();
    }

    DaoAuthenticationProvider daoAuthenticationProvider;

    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http
//                .formLogin().and()
                .oauth2Login(
                        oauth2->
                                oauth2.userInfoEndpoint(userInfo->
									// 각각의 서비스를 세팅할 수 있음
                                    userInfo.userService(oAuth2UserService) // 각 서비스에서 loadUser를 통해 OAuthUser 객체로 변환됨
                                            .oidcUserService(oidcUserService)
                                )
									// userInfoEndPoint가 처리된 후 각각의 user 서비스가 끝나면 successHandler로 적용할 수 있음
                                        .successHandler(new AuthenticationSuccessHandler() {
											// AuthenticationSuccessHandler를 직접 구현
											// 인증이 성공한 상태에서 
                                            @Override
                                            public void onAuthenticationSuccess(
                                                    HttpServletRequest request,
                                                    HttpServletResponse response,
                                                    Authentication authentication
                                            ) throws IOException, ServletException {

                                                Object principal = authentication.getPrincipal();
												// principal 객체가 OidcUser의 하위 객체일 경우(google 유저) 별도 처리

                                                if(principal instanceof OAuth2User){
                                                    if(principal instanceof OidcUser){
                                                        // google
														// 전달받은 객체를  각 enumerater로 서버에서 사용할 수 있는 form으로 convert 하기
                                                        SpOauth2User googleUser = SpOauth2User.OAuth2Provider.google.convert((OAuth2User) principal);
														// db에 있다면 조회 없다면 생성
                                                        SpUser user = userService.loadUser(googleUser);
														// SecurityContextHolder에 생성된 유저의 principal과 authorities 입력하여 저장하기
                                                        SecurityContextHolder.getContext().setAuthentication(
                                                                new UsernamePasswordAuthenticationToken(user, "", user.getAuthorities())
                                                        );
                                                    }else{
                                                        // naver, or kakao, facebook
                                                        SpOauth2User naverUser = SpOauth2User.OAuth2Provider.naver.convert((OAuth2User) principal);
                                                        SpUser user = userService.loadUser(naverUser);
                                                        SecurityContextHolder.getContext().setAuthentication(
                                                                new UsernamePasswordAuthenticationToken(user, "", user.getAuthorities())
                                                        );
                                                    }
                                                    System.out.println(principal);
													// successUrl 지정
                                                    request.getRequestDispatcher("/").forward(request, response);
                                                }

                                            }
                                        })

//                        .and()
//                        .addFilterAfter(userTranslateFilter, OAuth2LoginAuthenticationFilter.class)
                )

                ;
    }
}



```

- SpOAuth2User
	- OAuth2Provider enumerate를 추가함
	- 각 사이트가 제공하는 폼에 따라 SpOAuth2User의 필드를 채워 return

```java
package com.sp.fc.user.domain;

@Data
@AllArgsConstructor
@NoArgsConstructor
@Builder
@Entity
@Table(name="sp_oauth2_user")
public class SpOauth2User {

    public static enum OAuth2Provider {
        google {
            public SpOauth2User convert(OAuth2User user){
                return SpOauth2User.builder()
                        .oauth2UserId(format("%s_%s", name(), user.getAttribute("sub")))
                        .provider(google)
                        .email(user.getAttribute("email"))
                        .name(user.getAttribute("name"))
                        .created(LocalDateTime.now())
                        .build();
            }
        },
        naver {
            public SpOauth2User convert(OAuth2User user){
                Map<String, Object> resp = user.getAttribute("response");
                return SpOauth2User.builder()
                        .oauth2UserId(format("%s_%s", name(), resp.get("id")))
                        .provider(naver)
                        .email(""+resp.get("email"))
                        .name(""+resp.get("name"))
                        .build();
            }
        };
        public abstract SpOauth2User convert(OAuth2User user);
    }

    @Id
    private String oauth2UserId;

    private Long userId;

    private String name;
    private String email;

    private OAuth2Provider provider;

    private LocalDateTime created;

}

```


- SpOAuth2UserService, SpOidcUserService
	- DefaultOAuth2UserService와 OidcUserService를 상속하여 loadUser 메서드 사용함

```java
package com.sp.fc.web.config;

@Service
public class SpOAuth2UserService extends DefaultOAuth2UserService {

    @Override
    public OAuth2User loadUser(OAuth2UserRequest userRequest) throws OAuth2AuthenticationException {
        return super.loadUser(userRequest);
    }

}
// ----------------------------------------------------------------------------------
package com.sp.fc.web.config;

@Service
public class SpOidcUserService extends OidcUserService {

    @Override
    public OidcUser loadUser(OidcUserRequest userRequest) throws OAuth2AuthenticationException {
        return super.loadUser(userRequest);
    }

}

```