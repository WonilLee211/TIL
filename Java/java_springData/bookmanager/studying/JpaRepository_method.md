


# 2. JpaRepository methods(extends PagingAndSortingRepository)

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

-- UserTable(id=3, name=sophia, email=sophia@slowcampus.com, createdAt=2022-12-20T01:58:03.564743, updatedAt=2022-12-20T01:58:03.564743)
-- UserTable(id=1, name=martin, email=martin@fastcampus.com, createdAt=2022-12-20T01:58:03.558758, updatedAt=2022-12-20T01:58:03.558758)
-- UserTable(id=5, name=martin, email=martin@another.com, createdAt=2022-12-20T01:58:03.566742, updatedAt=2022-12-20T01:58:03.566742)
-- UserTable(id=4, name=james, email=james@slowcampus.com, createdAt=2022-12-20T01:58:03.564743, updatedAt=2022-12-20T01:58:03.564743)
-- UserTable(id=2, name=dennis, email=dennis@fastcampus.com, createdAt=2022-12-20T01:58:03.563744, updatedAt=2022-12-20T01:58:03.563744)

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

-- UserTable(id=1, name=martin, email=martin@fastcampus.com, createdAt=2022-12-20T02:05:17.727162, updatedAt=2022-12-20T02:05:17.727162)
-- UserTable(id=3, name=sophia, email=sophia@slowcampus.com, createdAt=2022-12-20T02:05:17.732150, updatedAt=2022-12-20T02:05:17.732150)
-- UserTable(id=5, name=martin, email=martin@another.com, createdAt=2022-12-20T02:05:17.738132, updatedAt=2022-12-20T02:05:17.738132)

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


-- UserTable(id=1, name=martin, email=martin@fastcampus.com, createdAt=2022-12-20T02:11:08.645533, updatedAt=2022-12-20T02:11:08.645533)
-- UserTable(id=2, name=dennis, email=dennis@fastcampus.com, createdAt=2022-12-20T02:11:08.651518, updatedAt=2022-12-20T02:11:08.651518)
-- UserTable(id=3, name=sophia, email=sophia@slowcampus.com, createdAt=2022-12-20T02:11:08.657506, updatedAt=2022-12-20T02:11:08.657506)
-- UserTable(id=4, name=james, email=james@slowcampus.com, createdAt=2022-12-20T02:11:08.657506, updatedAt=2022-12-20T02:11:08.657506)
-- UserTable(id=5, name=martin, email=martin@another.com, createdAt=2022-12-20T02:11:08.659496, updatedAt=2022-12-20T02:11:08.659496)
-- UserTable(id=6, name=jack, email=jack@fastcampus.com, createdAt=null, updatedAt=null)
-- UserTable(id=7, name=steve, email=steve@fastcampus.com, createdAt=null, updatedAt=null)

```

### 5.findById()

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

-- Optional[UserTable(id=1, name=martin, email=martin@fastcampus.com, createdAt=2022-12-20T02:16:44.501135, updatedAt=2022-12-20T02:16:44.501135)]

```

### 6. count()

```java
    long count = userTableRepository.count();
    System.out.println(count);
```
```sql

Hibernate: 
    select
        count(*) as col_0_0_ 
    from
        user_table usertable0_


-- 5
```

### 7. existsById()

- 실제로 `COUNT_QUERY_STRING`을 참조함
    - select count(~) from ~


```java
boolean exists = userTableRepository.existsById(1L);

```
```sql
Hibernate: 
    select
        count(*) as col_0_0_ 
    from
        user_table usertable0_ 
    where
        usertable0_.id=?

-- true

```

### 8. delete()

- delete 내부에 null을 넣으면 문제가 생김
- 아래 코드는 select 문이 한번 더 실행됨
```java
userTableRepository.delete(userTableRepository.findById(1L).orElse(null));
userTableRepository.findAll().forEach(System.out::println);

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
Hibernate: 
    delete 
    from
        user_table 
    where
        id=?
Hibernate: 
    select
        usertable0_.id as id1_0_,
        usertable0_.created_at as created_2_0_,
        usertable0_.email as email3_0_,
        usertable0_.name as name4_0_,
        usertable0_.updated_at as updated_5_0_ 
    from
        user_table usertable0_
-- UserTable(id=2, name=dennis, email=dennis@fastcampus.com, createdAt=2022-12-20T23:21:01.205266, updatedAt=2022-12-20T23:21:01.205266)
-- UserTable(id=3, name=sophia, email=sophia@slowcampus.com, createdAt=2022-12-20T23:21:01.205266, updatedAt=2022-12-20T23:21:01.205266)
-- UserTable(id=4, name=james, email=james@slowcampus.com, createdAt=2022-12-20T23:21:01.208257, updatedAt=2022-12-20T23:21:01.208257)
-- UserTable(id=5, name=martin, email=martin@another.com, createdAt=2022-12-20T23:21:01.209252, updatedAt=2022-12-20T23:21:01.209252)

```

- orm 수정

```java
userTableRepository.deleteById(1L);
userTableRepository.findAll().forEach(System.out::println);


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
Hibernate: 
    delete 
    from
        user_table 
    where
        id=?
Hibernate: 
    select
        usertable0_.id as id1_0_,
        usertable0_.created_at as created_2_0_,
        usertable0_.email as email3_0_,
        usertable0_.name as name4_0_,
        usertable0_.updated_at as updated_5_0_ 
    from
        user_table usertable0_

-- UserTable(id=2, name=dennis, email=dennis@fastcampus.com, createdAt=2022-12-21T00:37:06.599084, updatedAt=2022-12-21T00:37:06.599084)
-- UserTable(id=3, name=sophia, email=sophia@slowcampus.com, createdAt=2022-12-21T00:37:06.600077, updatedAt=2022-12-21T00:37:06.600077)
-- UserTable(id=4, name=james, email=james@slowcampus.com, createdAt=2022-12-21T00:37:06.601076, updatedAt=2022-12-21T00:37:06.601076)
-- UserTable(id=5, name=martin, email=martin@another.com, createdAt=2022-12-21T00:37:06.601076, updatedAt=2022-12-21T00:37:06.601076)

```

### 9. deleteAll()

- 전체 조회 후 delete 5회 실행
- 성능 이슈가 발생할 것임

```java
userTableRepository.deleteAll();
userTableRepository.findAll().forEach(System.out::println);

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
Hibernate: 
    delete 
    from
        user_table 
    where
        id=?
Hibernate: 
    delete 
    from
        user_table 
    where
        id=?
Hibernate: 
    delete 
    from
        user_table 
    where
        id=?
Hibernate: 
    delete 
    from
        user_table 
    where
        id=?
Hibernate: 
    delete 
    from
        user_table 
    where
        id=?
Hibernate: 
    select
        usertable0_.id as id1_0_,
        usertable0_.created_at as created_2_0_,
        usertable0_.email as email3_0_,
        usertable0_.name as name4_0_,
        usertable0_.updated_at as updated_5_0_ 
    from
        user_table usertable0_

```

### 10. deleteAllInBatch()

- select 문이 전혀 없음

```java

userTableRepository.deleteAllInBatch();
userTableRepository.findAll().forEach(System.out::println);
```
```sql
Hibernate: 
    delete 
    from
        user_table

Hibernate: 
    select
        usertable0_.id as id1_0_,
        usertable0_.created_at as created_2_0_,
        usertable0_.email as email3_0_,
        usertable0_.name as name4_0_,
        usertable0_.updated_at as updated_5_0_ 
    from
        user_table usertable0_


```

### 11. paging

```java
Page<UserTable> users = userTableRepository.findAll(PageRequest.of(1, 3)); // 가져올 페이지 번호, 레코드 개수
System.out.println("page : " + users);
System.out.println("totalElements : " + users.getTotalElements()); // 현재 총 레코드 수
System.out.println("totalPages : " + users.getTotalPages()); // 현재 총 페이지 수
System.out.println("numberOfElements : " + users.getNumberOfElements()); // 현재 가져온 레코드 수
System.out.println("sort : " + users.getSort()); // 설정한 정렬 정보
System.out.println("size : " + users.getSize()); // 페이징할 때 나누는 크기

users.getContent().forEach(System.out::println); // 유저 정보가져오기
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
        user_table usertable0_ limit ? offset ?


-- page : Page 2 of 2 containing com.jpa.fedeleo.bookmanager.domain.UserTable instances
-- totalElements : 5
-- totalPages : 2
-- numberOfElements : 2
-- sort : UNSORTED
-- size : 3
-- UserTable(id=4, name=james, email=james@slowcampus.com, createdAt=2022-12-21T00:57:51.672797, updatedAt=2022-12-21T00:57:51.672797)
-- UserTable(id=5, name=martin, email=martin@another.com, createdAt=2022-12-21T00:57:51.672797, updatedAt=2022-12-21T00:57:51.672797)

```

### QBE, queryByExample

- entity를 example로 만들고 matcher를 추가하여 선언할 쿼리를 만드는 방법
- `ExampleMatcher` : Example 클래스가 조회 조건을 만들때 좀더 유연하게 만들어주는 역할
- `GenericPropertyMatchers` 클래스의 메서드와 함께 사용하여 sql에서 like 구문을 사용할 수 있음
    - startsWith(), contains(), endsWith(), equals() 등
- 하지만 문자열만 사용할 수 있다는 점이나 example에 제한이 있다는 한계점이 있기 때문에 복잡한 쿼리는 다른 방식을 사용함


```java
// name 필드는 무시하고 email 필드만 주어진 값이 매칭하는지 확인
ExampleMatcher matcher = ExampleMatcher.matching()
        .withIgnorePaths("name")
        .withMatcher("email", endsWith());
// name핃드는 무시, email 필드가 fastcampus.com으로 끝나는 레코드 매칭
Example<UserTable> example = Example.of(new UserTable("ma", "fastcampus.com"), matcher);

userTableRepository.findAll(example).forEach(System.out::println);

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
        usertable0_.email like ? escape ?

-- UserTable(id=1, name=martin, email=martin@fastcampus.com, createdAt=2022-12-21T01:09:18.019393, updatedAt=2022-12-21T01:09:18.019393)
-- UserTable(id=2, name=dennis, email=dennis@fastcampus.com, createdAt=2022-12-21T01:09:18.026373, updatedAt=2022-12-21T01:09:18.026373)
```

- ExampleMatcher가 없다면, exact match 발생

```java
Example<UserTable> example = Example.of(new UserTable("ma", "fastcampus.com"));

userTableRepository.findAll(example).forEach(System.out::println);
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
        usertable0_.email=? 
        and usertable0_.name=?


```

- 다른 예시

```java
        UserTable user = new UserTable();
        user.setEmail("slow");

        ExampleMatcher matcher = ExampleMatcher.matching()
                .withMatcher("email", contains());

        Example<UserTable> example = Example.of(user, matcher);
        
        userTableRepository.findAll(example).forEach(System.out::println);
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
        usertable0_.email like ? escape ?
-- UserTable(id=3, name=sophia, email=sophia@slowcampus.com, createdAt=2022-12-21T01:32:45.241605, updatedAt=2022-12-21T01:32:45.241605)
-- UserTable(id=4, name=james, email=james@slowcampus.com, createdAt=2022-12-21T01:32:45.241605, updatedAt=2022-12-21T01:32:45.241605)


```

# 3. SimpleJpaRepository 분석

## update 기능 구현

- save()메서드가 상황에 따라 insert 문을 실행시키고, update문을 실행시킴

```java

userTableRepository.save(new UserTable("david", "david@fastcumpus.com"));

UserTable user = userTableRepository.findById(1L).orElse(null);
user.setEmail("martin-updated@fastcampus.com");
userTableRepository.save(user);
```
```sql
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
Hibernate: 
    update
        user_table 
    set
        created_at=?,
        email=?,
        name=?,
        updated_at=? 
    where
        id=?

```
## 내부 동작 분석

### save()

- `SimpleJpaRepository`
    - `JpaRepositoryImplementation<T, ID>` 를 구현하고 있음

    - `JpaRepositoryImplementation<T, ID>`클래스는 `JpaRepository<T, ID>`를 상속받고 있음
    - 즉, 사용하고 있는 JpaRespository의 메서드들은 SimpleJpaRepository에서 기본적으로 구현체를 제공하고 있음

    - `save()`
        1. 인자 null 체크
        2. `EntityManager.isNew()`를 사용해서 entity 생성 및 수정 작업 확인
        3. new라면 `EntityManager.persist()`
        4. 수정이라면 `EntityManager.merge()` 실행

```java
// SimpleJpaRespostory

	@Transactional
	@Override
	public <S extends T> S save(S entity) {

		Assert.notNull(entity, "Entity must not be null.");

		if (entityInformation.isNew(entity)) {
			em.persist(entity);
			return entity;
		} else {
			return em.merge(entity);
		}
	}
```

- `isNew()`
    -  getId(); 메서드를 활용하고 있음

```java
// AbstractPersistable<ID>

/**
 * Must be {@link Transient} in order to ensure that no JPA provider complains because of a missing setter.
 *
 * @see org.springframework.data.domain.Persistable#isNew()
 */
@Transient // DATAJPA-622
@Override
public boolean isNew() {
    return null == getId();
}

```


### saveAndFlush()

```java
	/*
	 * (non-Javadoc)
	 * @see org.springframework.data.jpa.repository.JpaRepository#saveAndFlush(java.lang.Object)
	 */
	@Transactional
	@Override
	public <S extends T> S saveAndFlush(S entity) {

		S result = save(entity);
		flush();

		return result;
	}

```

### saveAll()

- for문에 따라 save 메서드가 여러번 발생하기 때문에 insert 쿼리가 여러 번 선언됨

```java
	/*
	 * (non-Javadoc)
	 * @see org.springframework.data.jpa.repository.JpaRepository#save(java.lang.Iterable)
	 */
	@Transactional
	@Override
	public <S extends T> List<S> saveAll(Iterable<S> entities) {

		Assert.notNull(entities, "Entities must not be null!");

		List<S> result = new ArrayList<>();

		for (S entity : entities) {
			result.add(save(entity));
		}

		return result;
	}
```

### existsById()

- 결국 count query를 사용해서 조회함
    - `getExistsQueryString` -> `COUNT_QUERY_STRING = "select count(%s) from %s x";`

```java

	/*
	* (non-Javadoc)
	* @see org.springframework.data.repository.CrudRepository#existsById(java.io.Serializable)
	*/
	@Override
	public boolean existsById(ID id) {

		Assert.notNull(id, ID_MUST_NOT_BE_NULL);

		if (entityInformation.getIdAttribute() == null) {
			return findById(id).isPresent();
		}

		String placeholder = provider.getCountQueryPlaceholder();
		String entityName = entityInformation.getEntityName();
		Iterable<String> idAttributeNames = entityInformation.getIdAttributeNames();
		String existsQuery = QueryUtils.getExistsQueryString(entityName, placeholder, idAttributeNames);

		TypedQuery<Long> query = em.createQuery(existsQuery, Long.class);

		if (!entityInformation.hasCompositeId()) {
			query.setParameter(idAttributeNames.iterator().next(), id);
			return query.getSingleResult() == 1L;
		}

		for (String idAttributeName : idAttributeNames) {

			Object idAttributeValue = entityInformation.getCompositeIdAttributeValue(id, idAttributeName);

			boolean complexIdParameterValueDiscovered = idAttributeValue != null
					&& !query.getParameter(idAttributeName).getParameterType().isAssignableFrom(idAttributeValue.getClass());

			if (complexIdParameterValueDiscovered) {

				// fall-back to findById(id) which does the proper mapping for the parameter.
				return findById(id).isPresent();
			}

			query.setParameter(idAttributeName, idAttributeValue);
		}

		return query.getSingleResult() == 1L;
	}
```





