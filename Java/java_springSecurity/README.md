# 스프링 부트 시큐리티

## 사이트 환경

- 배포 시,  서비스 안에는 서비스를 사용하는 User 들의 리소스(정보)들이 포함됨
- 관리자는 이들 리소스들을 위임받아 관리하는 것이기 때문에, 악의적인 사용자들로부터 **리소스를 잘 보호해야 하고, 효과적으로 관리**해 주어야 합니다.

<img src="./images/fig-0-site-securities.png" width="600" style="max-width:600px;width:100%;" />

### 스프링 부트의 security

- 리소스를 잘 보호할 수 있는 기본 메커니즘과 라이브러리를 제공

## 선수 지식

- Java : jdk 11 이상 (modern java 에 대해 알아야 함)
- spring boot : 스프링 애플리케이션 프레임워크
- gradle : 프로젝트 관리 및 빌드
- JUnit5(Jupyter)와 spring test : 기본적인 기능 테스트를 위해 필요함.
- Spring 관련 전반 지식 : Web MVC, RESTFul 서비스, Spring Data JPA, AOP, SpEL
- lombok : Getter/Setter/Builter 메소드 등 지원
- thymeleaf : 웹 프로그램을 지원함
- mysql : 데이터 테스트
- IntelliJ IDE

## 목차

1. Gradle 멀티 프로젝트 구성과 모듈 프로젝트 개발
2. Spring Security의 기본 구조
3. Spring Security 를 활용한 로그인 방법 (Authentication)
4. Spring Security 를 활용한 권한 체크 방법 (Authorization)
5. Ajax 와 OAuth2 인증 : ajax / OAuth2 인증 방식

