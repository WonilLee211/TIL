# dependencies

1. spring web
2. lombok
3. H2 Database
4. spring boot JPA

# JPA

## 목차

1. jpa annotation
2. JpaRepository methods
3. query method

# error trouble shooting



## H2 database GenerationType.IDENTITY 오류

## 현상

- GeneratedType.IDENTITY 는 기본 키 생성을 데이터베이스에 위임한다.
- 즉, ID 값을 null로 하면 DB가 알아서 AUTO_INCREMENT 해주니깐 아래와 같은 오류가 나면 안되는데 나고있었다.

### 원인

- 알고봤더니 H2버전 문제로 나는 문제였다.

### 해결책

- application.properties 파일에 다음 내용을 추가합니다.

  - H2 2.xx 버전부터는 application.properties에 ;MODE=MySQL 추가해주면 된다.
  ```yml
    # Datasource 설정
    
    spring:datasource:url: jdbc:h2:mem://localhost/~/testdb;MODE=MYSQL
  ```

## Caused by: java.sql.SQLException: Access denied for user 'root'@'localhost' (using password: YES) 해결하기

### 현상

- spring batch작업을 위해 RDB 연동을 하는데, 아래와 같은 에러를 마주쳤다.

`Caused by: java.sql.SQLException: Access denied for user 'root'@'localhost' (using password: YES)`
- 당시 mysql을 로컬에 설치하고 application.yml은 아래와 같이 설정하였다.

### 원인

- 패스워드는 대문자, 소문자, 숫자, 특수문자를 포함한 암호 길이 8자 이상으로 설정해야 연결이 제대로 된다

### 해결

- MySQL workbatch에서 `alter user 'root'@'localhost' identified by '{바꿀 비밀번호}';` 명령어 실행


## data.sql이 초기화되지 않음 문제

### 현상

- MySQL을 연동할 때 data.sql이 초기화되지 않음
- sql이 제대로 실행되지 않는 문제

### 원인

- 스프링 버전 및 sql.init.mode 이슈
- 이 2.5.x 버전에서 나타나는 이슈로 정확한 버전이 어딘지는 알 수 없지만 후반 버전에서는 쿼리, 그것도 insert, delete 등의 트랜잭션 이슈를 의심하게 할 쿼리가 제대로 동작하지 않는다. 

### 해결

- v2.5.x 이상 설정: spring.sql.init.mode
- 위 버전 이하 설정 : spring.datasource.initialization-mode

```yml

# application.yml
spring:
  sql:
    init:
      mode: always

```

## LazyInitaializationException: .... could not initialize proxy - no session

### 현상

- 테스트코드 실행 중 에러 발생

### 헤결책

1. 테스트코드를 `@Transactional`로 묶기
2. 순환 참조를 방지하기 위해 relation field 