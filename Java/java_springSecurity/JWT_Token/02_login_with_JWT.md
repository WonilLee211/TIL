# JWT 토큰 인증

## AccessToken

- 만료시간을 짧게 줍니다. 
- 은행권처럼 보안이 중요한 곳은 5분 내외를 주고 일반 사이트는 보통 세션 만료시간과 비슷한 `20분 정도`를 줍니다.
- 일반적으로 username 을 sub, 만료시간을 exp 에 넣고, 서명한 값을 달아서 사용합니다. 필요한 경우 authority 정보도 넣습니다.

## jjwt vs java-jwt

- test code

```java
package com.sp.fc.web;

public class JWTSimpleTest {

    // 토큰 파싱 & 프린트 함수
    private void printToken(String token){
        String[] tokens = token.split("\\.");
        System.out.println("header : " + new String(Base64.getDecoder().decode(tokens[0])));
        System.out.println("body : " + new String(Base64.getDecoder().decode(tokens[1])));
    }

    @DisplayName("1. jjwt 를 이용한 토큰 테스트")
    @Test
    void test_1(){
        String okta_token = Jwts.builder().addClaims(
                Map.of("name", "wonil", "price", 3000)
                ).signWith(SignatureAlgorithm.HS256, "wonil")
                .compact();
        System.out.println(okta_token);
//        eyJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoid29uaWwiLCJwcmljZSI6MzAwMH0.ByWerxDwfjufPe4Ih0x4TBw2p22ZnNhzuh4327R8Ddw
        printToken(okta_token);
//        header : {"alg":"HS256"}
//        body : {"name":"wonil","price":3000}

    }

    @DisplayName("2. java-jwt 를 이용한 토큰 테스트")
    @Test
    void test_2() {
        String oauth0 = JWT.create().withClaim("name", "wonil").withClaim("price", 3000)
                .sign(Algorithm.HMAC256("wonil"));

        System.out.println(oauth0);
//        eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwcmljZSI6MzAwMCwibmFtZSI6IndvbmlsIn0.2wsgTi4FGpCj-lRiW4yWVAxS8ClatTni7ADUNFgKOUs
        printToken(oauth0);
//        header : {"typ":"JWT","alg":"HS256"}
//        body : {"price":3000,"name":"wonil"}
    }

}
```

- 동작은 잘 됨

### 서로 다른 서버에서 다른 jwt 라이브러리를 통해 검증한다면?

- test code

```java
    @DisplayName("2. java-jwt 를 이용한 토큰 테스트")
    @Test
    void test_2() {

        

        String oauth0 = JWT.create().withClaim("name", "wonil").withClaim("price", 3000)
                .sign(Algorithm.HMAC256("wonil"));
        
        ...


        DecodedJWT verified =  JWT.require(Algorithm.HMAC256("wonil")).build().verify(oauth0);
        System.out.println(verified.getClaims());
//        {name="wonil", price=3000}

        // jjwt방식으로 java-jwt로 만들어진 토큰을 같은 키 값으로 verification 진행
        Jws<Claims> tokenInfo = Jwts.parser().setSigningKey("wonil").parseClaimsJws(oauth0);
        System.out.println(tokenInfo);

    }

```
- 에러 발생
  - `JWT sig  nature does not match locally computed signature. JWT validity cannot be asserted and should not be trusted.`
  - 키값이 같아보이지만 내부적으론 다름!

### 해결책

- **같은 key생성 방식과 같은 알고리즘으로 검증**한다면 다른 라이브러리에서 생성된 토큰이라도 **동일하게 검증 가능**

```java

    @DisplayName("2. java-jwt 를 이용한 토큰 테스트")
    @Test
    void test_2() {
        // okta에서 사용하는 키 값 만들어내는 방법
        // 같은 방식으로 생성된 키와 같은 알고리즘으로 검증하면 동일하게 인증됨
        byte[] SEC_KEY = DatatypeConverter.parseBase64Binary("wonil");

        String oauth0 = JWT.create().withClaim("name", "wonil").withClaim("price", 3000)
                .sign(Algorithm.HMAC256(SEC_KEY));

        ...

        DecodedJWT verified =  JWT.require(Algorithm.HMAC256(SEC_KEY)).build().verify(oauth0);
        System.out.println(verified.getClaims());


        Jws<Claims> tokenInfo = Jwts.parser().setSigningKey(SEC_KEY).parseClaimsJws(oauth0);
        System.out.println(tokenInfo);

    }


```

### 중요

- **JWT는 알고리즘과 key값이 동일하다면 어느 곳에서든 검증 가능한 토큰라는 것을 의미함**


## JWT 만료시간 테스트

- test code

```java
    @DisplayName("3. 만료시간 테스트")
    @Test
    void test_3() throws InterruptedException {
        final Algorithm AL = Algorithm.HMAC256("wonil");
        String token = JWT.create().withSubject("a1234")
                .withExpiresAt(new Date(System.currentTimeMillis() + 1000))

                .sign(AL);

        Thread.sleep(2000); // 토큰이 expired 되도록 설정
        DecodedJWT verified = JWT.require(AL).build().verify(token);
        System.out.println(verified.getClaims());
    }

// The Token has expired on Thu Dec 29 23:38:12 KST 2022.

```

- 토큰 expired

<br>

- withNotBefore 옵션

```java
    @DisplayName("3. 만료시간 테스트")
    @Test
    void test_3() throws InterruptedException {
        final Algorithm AL = Algorithm.HMAC256("wonil");
        String token = JWT.create().withSubject("a1234")
                .withNotBefore(new Date(System.currentTimeMillis() + 1000))
                .withExpiresAt(new Date(System.currentTimeMillis() + 3000))

                .sign(AL);

        DecodedJWT verified = JWT.require(AL).build().verify(token);
        System.out.println(verified.getClaims());
    }


```

- nbf 시간에 검증하려할 때 발생하는 에러
- `The Token can't be used before Thu Dec 29 23:41:16 KST 2022.`
  
  <br>

- nbf 1초, exp 3초 : 기준 시점에서 1초 동안 사용할 수 없고, 1초부터 3초까지 유효함

```java
    @DisplayName("3. 만료시간 테스트")
    @Test
    void test_3() throws InterruptedException {
        final Algorithm AL = Algorithm.HMAC256("wonil");
        String token = JWT.create().withSubject("a1234")
                .withNotBefore(new Date(System.currentTimeMillis() + 1000))
                .withExpiresAt(new Date(System.currentTimeMillis() + 3000))

                .sign(AL);

        Thread.sleep(3300); // 토큰이 expired 되도록 설정
        DecodedJWT verified = JWT.require(AL).build().verify(token);
        System.out.println(verified.getClaims());
//      >>> The Token has expired on Thu Dec 29 23:45:09 KST 2022.
    }



```

### 토큰이 유효하지 않을 때 토큰 내용이 필요한 경우

```java

    @DisplayName("3. 만료시간 테스트")
    @Test
    void test_3() throws InterruptedException {
        final Algorithm AL = Algorithm.HMAC256("wonil");
        String token = JWT.create().withSubject("a1234")
                .withNotBefore(new Date(System.currentTimeMillis() + 1000))
                .withExpiresAt(new Date(System.currentTimeMillis() + 3000))

                .sign(AL);

        try{
            DecodedJWT verified = JWT.require(AL).build().verify(token);
            System.out.println(verified.getClaims());
        } catch (Exception e){
            System.out.println("유효하지 않은 토큰입니다");
            DecodedJWT decode = JWT.decode(token);
            System.out.println(decode.getClaims());
        }
    }

```

- output

```
유효하지 않은 토큰입니다
{sub="a1234", nbf=1672325502, exp=1672325504}
```

- **주의**
  - java-jwt 라이브러리에서만 유효하지 않은 토큰에 대한 decode기능을 제공함
  - 이는 필요한 기능이기 때문에 java-jwt 라이브러리를 사용하는게 더 적절하다고 판단됨

