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

error trouble shooting



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

