## dependencies

1. spring web
2. lombok
3. H2 Database
4. spring boot JPA

# JPA

## annotation

### `@Entity`

-  객체를 entity로 선언. 
- 내부에 primaery key 선언이 필수
   - `@Id` : pk
   - `@GeneratedValue` : autoincrement


## JpaRepository methods(extends PagingAndSortingRepository)

1. `findAll` : 성능 이슈로 많이 사용하지 않음
2. `findAll(Sort sort)` : 찾은 데이터 정렬 기능
3. `findAllById(Iterable<ID> ids)` : 찾을 id들 리스트로 받아서 찾기(in 연산)
4. `flush()` : jpa context에 가지고 있는 값을 db에반영하도록 하는 메서드
    - `save`를 실행하면 jpa context에 저장됨
5. `saveAndFlush(S entity)`
6. `deleteInBatch(Iterable<T> entities)` : 엔티티 리스트를 받아서 한번에 지움
    - Deletes the given entities in a batch which means it will create a single query. This kind of operation leaves JPAs first level cache and the database out of sync. 
7. `deleteAllInBatch(Iterable<T> entities)` : 조건없이 해당 테이블을 통째로 삭제
    - 거의 안씀

### PagingAndSortingRepository

8. `findAll(Pageable pageable)` : 에 정의되어 있음

### CrudRepository

9 `save(S entity)` : 엔티티 저장
    - `saveAll()
10. `findById(ID id)` 
11. `existsById(ID id)`
12.`count()` : paging할 때 사용
13. `delete(T entity)`

### Repository(최상위 repositroy)

- jpa에 있는 도메인 레포지토리라는 것을 알려주기 위한 역할
- 메서드 정의 없음

...

## 실습

### 준비

- resources폴더 하위에 data.sql 파일을 생성하면 프로그램이 실행될 때 함께 로딩함

- resources/data.sql

```sql
 call next value for hibernate_sequence;
insert into user_table (`id`, `name`, `email`, `created_at`, `updated_at`) values (1, 'martin', 'martin@fastcampus.com', now(), now());

 call next value for hibernate_sequence;
insert into user_table (`id`, `name`, `email`, `created_at`, `updated_at`) values (2, 'dennis', 'dennis@fastcampus.com', now(), now());

 call next value for hibernate_sequence;
insert into user_table (`id`, `name`, `email`, `created_at`, `updated_at`) values (3, 'sophia', 'sophia@slowcampus.com', now(), now());

 call next value for hibernate_sequence;
insert into user_table (`id`, `name`, `email`, `created_at`, `updated_at`) values (4, 'james', 'james@slowcampus.com', now(), now());

 call next value for hibernate_sequence;
insert into user_table (`id`, `name`, `email`, `created_at`, `updated_at`) values (5, 'martin', 'martin@another.com', now(), now());
```

### 1. log setting

```yml

spring:
  h2:
    console:
      enabled: true
  jpa:
    show-sql: true # sql 명령들이 실제 db에서 어떻게 동작하는지 log 출력
    properties:
      hibernate:
        format_sql: true # query를 포맷에 맞춰서 출력
    defer-datasource-initialization: true
```
### 2. 이름 내림차순 정렬 출력

```java
package com.jpa.fedeleo.bookmanager.repository;


@SpringBootTest
class UserTableRepositoryTest {

    @Autowired
    private UserTableRepository userTableRepository;

    @Test
    void crud(){
        List<UserTable> users = userTableRepository.findAll(Sort.by(Sort.Direction.DESC, "name"));

        users.forEach(System.out::println);
    }
}


```
- output

```sql
Hibernate: 
    select
        usertable0_.id as id1_0_,
        usertable0_.created_at as created_2_0_,
        usertable0_.email as email3_0_,
        usertable0_.name as name4_0_,
        usertable0_.updated_at as updated_5_0_ 
    from
        user_table usertable0_ 
    order by
        usertable0_.name desc

UserTable(id=3, name=sophia, email=sophia@slowcampus.com, createdAt=2022-12-20T01:58:03.564743, updatedAt=2022-12-20T01:58:03.564743)
UserTable(id=1, name=martin, email=martin@fastcampus.com, createdAt=2022-12-20T01:58:03.558758, updatedAt=2022-12-20T01:58:03.558758)
UserTable(id=5, name=martin, email=martin@another.com, createdAt=2022-12-20T01:58:03.566742, updatedAt=2022-12-20T01:58:03.566742)
UserTable(id=4, name=james, email=james@slowcampus.com, createdAt=2022-12-20T01:58:03.564743, updatedAt=2022-12-20T01:58:03.564743)
UserTable(id=2, name=dennis, email=dennis@fastcampus.com, createdAt=2022-12-20T01:58:03.563744, updatedAt=2022-12-20T01:58:03.563744)

```
### 3. 일부 데이터 조회
```java
package com.jpa.fedeleo.bookmanager.repository;

@SpringBootTest
class UserTableRepositoryTest {

    @Autowired
    private UserTableRepository userTableRepository;

    @Test
    void crud(){

        List<UserTable> users = userTableRepository.findAllById(Lists.newArrayList(1L, 3L, 5L));

        users.forEach(System.out::println);
    }
}
```

```sql
Hibernate: 
    select
        usertable0_.id as id1_0_,
        usertable0_.created_at as created_2_0_,
        usertable0_.email as email3_0_,
        usertable0_.name as name4_0_,
        usertable0_.updated_at as updated_5_0_ 
    from
        user_table usertable0_ 
    where
        usertable0_.id in (
            ? , ? , ?
        )

UserTable(id=1, name=martin, email=martin@fastcampus.com, createdAt=2022-12-20T02:05:17.727162, updatedAt=2022-12-20T02:05:17.727162)
UserTable(id=3, name=sophia, email=sophia@slowcampus.com, createdAt=2022-12-20T02:05:17.732150, updatedAt=2022-12-20T02:05:17.732150)
UserTable(id=5, name=martin, email=martin@another.com, createdAt=2022-12-20T02:05:17.738132, updatedAt=2022-12-20T02:05:17.738132)

```

### 4. 여러 정보 저장

```java
package com.jpa.fedeleo.bookmanager.repository;

@SpringBootTest
class UserTableRepositoryTest {

    @Autowired
    private UserTableRepository userTableRepository;

    @Test
    void crud(){

        UserTable user1 = new UserTable("jack", "jack@fastcampus.com");
        UserTable user2 = new UserTable("steve", "steve@fastcampus.com");

        userTableRepository.saveAll(Lists.newArrayList(user1, user2));

        List<UserTable> users = userTableRepository.findAll();
        users.forEach(System.out::println);

    }
}
```
```sql
Hibernate: 
    call next value for hibernate_sequence
Hibernate: 
    call next value for hibernate_sequence
Hibernate: 
    insert 
    into
        user_table
        (created_at, email, name, updated_at, id) 
    values
        (?, ?, ?, ?, ?)
Hibernate: 
    insert 
    into
        user_table
        (created_at, email, name, updated_at, id) 
    values
        (?, ?, ?, ?, ?)
Hibernate: 
    select
        usertable0_.id as id1_0_,
        usertable0_.created_at as created_2_0_,
        usertable0_.email as email3_0_,
        usertable0_.name as name4_0_,
        usertable0_.updated_at as updated_5_0_ 
    from
        user_table usertable0_


UserTable(id=1, name=martin, email=martin@fastcampus.com, createdAt=2022-12-20T02:11:08.645533, updatedAt=2022-12-20T02:11:08.645533)
UserTable(id=2, name=dennis, email=dennis@fastcampus.com, createdAt=2022-12-20T02:11:08.651518, updatedAt=2022-12-20T02:11:08.651518)
UserTable(id=3, name=sophia, email=sophia@slowcampus.com, createdAt=2022-12-20T02:11:08.657506, updatedAt=2022-12-20T02:11:08.657506)
UserTable(id=4, name=james, email=james@slowcampus.com, createdAt=2022-12-20T02:11:08.657506, updatedAt=2022-12-20T02:11:08.657506)
UserTable(id=5, name=martin, email=martin@another.com, createdAt=2022-12-20T02:11:08.659496, updatedAt=2022-12-20T02:11:08.659496)
UserTable(id=6, name=jack, email=jack@fastcampus.com, createdAt=null, updatedAt=null)
UserTable(id=7, name=steve, email=steve@fastcampus.com, createdAt=null, updatedAt=null)

```

### findById

- null에러를 방지하기 위해 return되는 객체가 `Optional` 타입으로 한 번 wrapped
- entity manager에서 find() 함수를 사용해서 직접 entity객체를 가져옴
    - Eager 방식(즉시로딩)
    - `getOne()`은 지연 로딩.(deprecated)

```java
package com.jpa.fedeleo.bookmanager.repository;

@SpringBootTest
class UserTableRepositoryTest {

    @Autowired
    private UserTableRepository userTableRepository;

    @Test
    void crud(){

        Optional<UserTable> user = userTableRepository.findById(1L);

        // UserTable user = userTableRepository.findById(1L).orElse(null);

        System.out.println(user);

    }
}
```

```sql
Hibernate: 
    select
        usertable0_.id as id1_0_0_,
        usertable0_.created_at as created_2_0_0_,
        usertable0_.email as email3_0_0_,
        usertable0_.name as name4_0_0_,
        usertable0_.updated_at as updated_5_0_0_ 
    from
        user_table usertable0_ 
    where
        usertable0_.id=?

```
```       
Optional[UserTable(id=1, name=martin, email=martin@fastcampus.com, createdAt=2022-12-20T02:16:44.501135, updatedAt=2022-12-20T02:16:44.501135)]

```

## error  trouble shooting

- User class 테스트 진행 과정에서 `Caused by: org.h2.jdbc.JdbcSQLSyntaxErrorException: Syntax error in SQL statement "drop table if exists [*]user CASCADE "; expected "identifier"; SQL statement:`
 발생
- 구글링읕 통해 공통적인 원인이 identifier, 예약어 문제였다.
- 그래서 User class를 UserTable로 변경해서 retry했더니 에러 해결.
- User는 예약어가 아닌데, 어떤 문제였는지 근본 원인이 뭐였을까..


### Hibernate 초기화 전 data.sql 먼저 실행되어 발생하는 오류

오류 내용

```
Caused by: org.springframework.beans.factory.BeanCreationException: Error creating bean with name 'dataSourceScriptDatabaseInitializer' defined in class path resource [org/springframework/boot/autoconfigure/sql/init/DataSourceInitializationConfiguration.class]: Invocation of init method failed; nested exception is org.springframework.jdbc.datasource.init.ScriptStatementFailedException: Failed to execute SQL script statement #1 of URL [file:/C:/Users/shbae/IdeaProjects/fastcampus/build/resources/main/data.sql]: call next value for hibernate_sequence; nested exception is org.h2.jdbc.JdbcSQLSyntaxErrorException: Sequence "HIBERNATE_SEQUENCE" not found; SQL statement:
call next value for hibernate_sequence [90036-200]~
```

- 위 오류는 Hibernate가 초기화되기 전에 data.sql이 먼저 실행되어서 발생하는 오류

- 해결방법  
    - application 설정파일에 `spring.jpa.defer-datasource-initialization: true`로 설정