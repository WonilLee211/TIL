## 목차

1. queryMethod naming rules
2. queryMethod를 통한 paging과 sort 구현

# QueryMethod 활용

- logical predicate keyword로 orm 작성
- 코드 가독성을 높이기 위한 다양한 키워드 사용


# keyword

Table 8. Query subject keywords

| Keyword | Description |
| --- | --- |
| find…By, read…By, get…By, query…By, search…By, stream…By | General query method returning typically the repository type, a Collection or Streamable subtype or a result wrapper such as Page, GeoResults or any other store-specific result wrapper. Can be used as findBy…, findMyDomainTypeBy… or in combination with additional keywords. |
| exists…By | Exists projection, returning typically a boolean result. |
| count…By | Count projection returning a numeric result. |
| delete…By, remove…By | Delete query method returning either no result (void) or the delete count. |
| …First<number>…, …Top<number>… | Limit the query results to the first <number> of results. This keyword can occur in any place of the subject between find (and the other keywords) and by. |
| …Distinct… | Use a distinct query to return only unique results. Consult the store-specific documentation whether that feature is supported. This keyword can occur in any place of the subject between find (and the other keywords) and by. |

<br>

Table 9. Query predicate keywords

| Logical keyword | Keyword expressions |
| --- | --- |
| AND | And |
| OR | Or |
| AFTER | After, IsAfter |
| BEFORE | Before, IsBefore |
| CONTAINING | Containing, IsContaining, Contains |
| BETWEEN | Between, IsBetween |
| ENDING_WITH | EndingWith, IsEndingWith, EndsWith |
| EXISTS | Exists |
| FALSE | False, IsFalse |
| GREATER_THAN | GreaterThan, IsGreaterThan |
| GREATER_THAN_EQUALS | GreaterThanEqual, IsGreaterThanEqual |
| IN | In, IsIn |
| IS | Is, Equals, (or no keyword) |
| IS_EMPTY | IsEmpty, Empty |
| IS_NOT_EMPTY | IsNotEmpty, NotEmpty |
| IS_NOT_NULL | NotNull, IsNotNull |
| IS_NULL | Null, IsNull |
| LESS_THAN | LessThan, IsLessThan |
| LESS_THAN_EQUAL | LessThanEqual, IsLessThanEqual |
| LIKE | Like, IsLike |
| NEAR | Near, IsNear |
| NOT | Not, IsNot |
| NOT_IN | NotIn, IsNotIn |
| NOT_LIKE | NotLike, IsNotLike |
| REGEX | Regex, MatchesRegex, Matches |
| STARTING_WITH | StartingWith, IsStartingWith, StartsWith |
| TRUE | True, IsTrue |
| WITHIN | Within, IsWithin |


<br>

Table 11. Query return types


| Return type | Description |
| --- | --- |
| void | Denotes no return value. |
| Primitives | Java primitives. |
| Wrapper types | Java wrapper types. |
| T | A unique entity. Expects the query method to return one result at most. If no result is found, null is returned. More than one result triggers an IncorrectResultSizeDataAccessException. |
| Iterator<T> | An Iterator. |
| Collection<T> | A Collection. |
| List<T> | A List. |
| Optional<T> | A Java 8 or Guava Optional. Expects the query method to return one result at most. If no result is found, Optional.empty() or Optional.absent() is returned. More than one result triggers an IncorrectResultSizeDataAccessException. |
| Option<T> | Either a Scala or Vavr Option type. Semantically the same behavior as Java 8’s Optional, described earlier. |
| Stream<T> | A Java 8 Stream. |
| Streamable<T> | A convenience extension of Iterable that directy exposes methods to stream, map and filter results, concatenate them etc. |
| Types that implement Streamable and take a Streamable constructor or factory method argument | Types that expose a constructor or ….of(…)/….valueOf(…) factory method taking a Streamable as argument. See https://docs.spring.io/spring-data/jpa/docs/current/reference/html/#repositories.collections-and-iterables.streamable-wrapper for details. |
| Vavr Seq, List, Map, Set | Vavr collection types. See https://docs.spring.io/spring-data/jpa/docs/current/reference/html/#repositories.collections-and-iterables.vavr for details. |
| Future<T> | A Future. Expects a method to be annotated with @Async and requires Spring’s asynchronous method execution capability to be enabled. |
| CompletableFuture<T> | A Java 8 CompletableFuture. Expects a method to be annotated with @Async and requires Spring’s asynchronous method execution capability to be enabled. |
| Slice<T> | A sized chunk of data with an indication of whether there is more data available. Requires a Pageable method parameter. |
| Page<T> | A Slice with additional information, such as the total number of results. Requires a Pageable method parameter. |
| GeoResult<T> | A result entry with additional information, such as the distance to a reference location. |
| GeoResults<T> | A list of GeoResult<T> with additional information, such as the average distance to a reference location. |
| GeoPage<T> | A Page with GeoResult<T>, such as the average distance to a reference location. |
| Mono<T> | A Project Reactor Mono emitting zero or one element using reactive repositories. Expects the query method to return one result at most. If no result is found, Mono.empty() is returned. More than one result triggers an IncorrectResultSizeDataAccessException. |
| Flux<T> | A Project Reactor Flux emitting zero, one, or many elements using reactive repositories. Queries returning Flux can emit also an infinite number of elements. |
| Single<T> | A RxJava Single emitting a single element using reactive repositories. Expects the query method to return one result at most. If no result is found, Mono.empty() is returned. More than one result triggers an IncorrectResultSizeDataAccessException. |
| Maybe<T> | A RxJava Maybe emitting zero or one element using reactive repositories. Expects the query method to return one result at most. If no result is found, Mono.empty() is returned. More than one result triggers an IncorrectResultSizeDataAccessException. |
| Flowable<T> | A RxJava Flowable emitting zero, one, or many elements using reactive repositories. Queries returning Flowable can emit also an infinite number of elements. |


# select query 만들기

## read 기능

```java
package com.jpa.fedeleo.bookmanager.repository;

public interface UserTableRepository extends JpaRepository<UserTable, Long> {
    List<UserTable> findByName(String name);

    UserTable findByEmail(String email);
    UserTable getByEmail(String email);
    UserTable readByEmail(String email);
    UserTable queryByEmail(String email);
    UserTable searchByEmail(String email);
    UserTable streamByEmail(String email);
    UserTable findUserByEmail(String email);

}
```

```java
package com.jpa.fedeleo.bookmanager.repository;

@SpringBootTest
class UserTableRepositoryTest {

    @Autowired
    private UserTableRepository userTableRepository;

    @Test
    void select(){
        System.out.println(userTableRepository.findByName("dennis"));

        System.out.println("findByEmail : " + userTableRepository.findByEmail("martin@fastcampus.com"));
        System.out.println("getByEmail : " + userTableRepository.getByEmail("martin@fastcampus.com"));
        System.out.println("searchByEmail : " + userTableRepository.searchByEmail("martin@fastcampus.com"));
        System.out.println("readByEmail : " + userTableRepository.readByEmail("martin@fastcampus.com"));
        System.out.println("queryByEmail : " + userTableRepository.queryByEmail("martin@fastcampus.com"));
        System.out.println("streamByEmail : " + userTableRepository.streamByEmail("martin@fastcampus.com"));
        System.out.println("findUserByEmail : " + userTableRepository.findUserByEmail("martin@fastcampus.com"));
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
        usertable0_.name=?
[UserTable(id=2, name=dennis, email=dennis@fastcampus.com, createdAt=2022-12-21T02:50:08.976435, updatedAt=2022-12-21T02:50:08.976435)]

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
findByEmail : UserTable(id=1, name=martin, email=martin@fastcampus.com, createdAt=2022-12-21T02:50:08.972447, updatedAt=2022-12-21T02:50:08.972447)

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
getByEmail : UserTable(id=1, name=martin, email=martin@fastcampus.com, createdAt=2022-12-21T02:50:08.972447, updatedAt=2022-12-21T02:50:08.972447)

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
searchByEmail : UserTable(id=1, name=martin, email=martin@fastcampus.com, createdAt=2022-12-21T02:50:08.972447, updatedAt=2022-12-21T02:50:08.972447)

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
readByEmail : UserTable(id=1, name=martin, email=martin@fastcampus.com, createdAt=2022-12-21T02:50:08.972447, updatedAt=2022-12-21T02:50:08.972447)

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
queryByEmail : UserTable(id=1, name=martin, email=martin@fastcampus.com, createdAt=2022-12-21T02:50:08.972447, updatedAt=2022-12-21T02:50:08.972447)

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
streamByEmail : UserTable(id=1, name=martin, email=martin@fastcampus.com, createdAt=2022-12-21T02:50:08.972447, updatedAt=2022-12-21T02:50:08.972447)

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
findUserByEmail : UserTable(id=1, name=martin, email=martin@fastcampus.com, createdAt=2022-12-21T02:50:08.972447, updatedAt=2022-12-21T02:50:08.972447)

```

- 모두 같은 query가 실행됨
- 개발자가 가독성이 좋다고 판단되는 접두어로 작성하면 됨
- `findUserByEmail`에서 User 키워드는 내부적으로 무시됨
    - 어떤 문자열을 작성해도 무시된다는 뜻

### findTopByName()

```java
package com.jpa.fedeleo.bookmanager.repository;

public interface UserTableRepository extends JpaRepository<UserTable, Long> {
    UserTable findFirstByName(String name);
    UserTable findTopByName(String name );

}

```

- 같은 결과

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
        usertable0_.name=? limit ?

-- findTopByName : UserTable(id=1, name=martin, email=martin@fastcampus.com, createdAt=2022-12-21T17:44:43.660882, updatedAt=2022-12-21T17:44:43.660882)

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
        usertable0_.name=? limit ?
-- findFirstByName : UserTable(id=1, name=martin, email=martin@fastcampus.com, createdAt=2022-12-21T17:44:43.660882, updatedAt=2022-12-21T17:44:43.660882)

```

### findTop{number}ByName()

- 조건에 만족하는 레코드 여러개 찾아오기
- 반환 타입을 리스트로 설정해야 함

```java
package com.jpa.fedeleo.bookmanager.repository;


public interface UserTableRepository extends JpaRepository<UserTable, Long> {

    List<UserTable> findFirst2ByName(String name);
    List<UserTable> findTop2ByName(String name);

}

package com.jpa.fedeleo.bookmanager.repository;

@SpringBootTest
class UserTableRepositoryTest {

    @Autowired
    private UserTableRepository userTableRepository;

    @Test
    void select(){
/       System.out.println("findFirst2ByName : " + userTableRepository.findFirst2ByName("martin"));
        System.out.println("findTop2ByName : " + userTableRepository.findTop2ByName("martin"));
    }
}
```

## And, Or

```java
package com.jpa.fedeleo.bookmanager.repository;

public interface UserTableRepository extends JpaRepository<UserTable, Long> {

    List<UserTable> findByEmailAndName(String email, String name);
    List<UserTable> findByEmailOrName(String email, String name);


}

package com.jpa.fedeleo.bookmanager.repository;

@SpringBootTest
class UserTableRepositoryTest {

    @Autowired
    private UserTableRepository userTableRepository;

    @Test
    void select(){
        System.out.println("findByEmailAndName : " + userTableRepository.findByEmailAndName("martin@fastcampus.com", "martin"));
        System.out.println("findByEmailOrName : " + userTableRepository.findByEmailOrName("martin@fastcampus.com", "dennis"));

    }
}

```

- where절에 and, or 조건을 볼 수 있음

```SQL

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

-- findByEmailAndName : [UserTable(id=1, name=martin, email=martin@fastcampus.com, createdAt=2022-12-21T18:08:20.828788, updatedAt=2022-12-21T18:08:20.828788)]


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
        or usertable0_.name=?
-- findByEmailOrName : [UserTable(id=1, name=martin, email=martin@fastcampus.com, createdAt=2022-12-21T18:11:22.070325, updatedAt=2022-12-21T18:11:22.070325), UserTable(id=2, name=dennis, email=dennis@fastcampus.com, createdAt=2022-12-21T18:11:22.073317, updatedAt=2022-12-21T18:11:22.073317)]

```

## 대소 비교 연산자

### 1. after, before


```java

List<UserTable> findByCreatedAtAfter(LocalDateTime yesterday);
List<UserTable> findByIdAfter(Long id);

// ---

System.out.println("findByCreatedAtAfter : " + userTableRepository.findByCreatedAtAfter(LocalDateTime.now()));
System.out.println("findByIdAfter : " + userTableRepository.findByIdAfter(4L));

```

- 대소 조건을 볼 수 있음

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
        usertable0_.created_at>?

-- findByCreatedAtAfter : []

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
        usertable0_.id>?

-- findByIdAfter : [UserTable(id=5, name=martin, email=martin@another.com, createdAt=2022-12-21T18:20:57.871057, updatedAt=2022-12-21T18:20:57.871057)]


```

<br>

### greater/less than , equal

- 좀 더 범용적인 키워드
- **주의**
  - greaterThanEqual 키워드는 after키워드에서는 없는 범위

```java
List<UserTable> findByCreatedAtGreaterThan(LocalDateTime yesterday);
List<UserTable> findByIdGreaterThan(Long id);
List<UserTable> findByIdGreaterThanEqual(Long id);

// ------
System.out.println("findByCreatedGreaterThan : " + userTableRepository.findByCreatedAtGreaterThan(LocalDateTime.now()));
System.out.println("findByIdGreaterThan : " + userTableRepository.findByIdGreaterThan(4L));
        System.out.println("findByIdGreaterThanEqual : " + userTableRepository.findByIdGreaterThanEqual(4L));


```
- after 키워드와 동일한 결과

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
        usertable0_.created_at>?

-- findByCreatedGreaterThan : []

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
        usertable0_.id>?

-- findByIdGreaterThan : [UserTable(id=5, name=martin, email=martin@another.com, createdAt=2022-12-21T18:25:47.042341, updatedAt=2022-12-21T18:25:47.042341)]

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
        usertable0_.id>=?
-- findByIdGreaterThanEqual : [UserTable(id=4, name=james, email=james@slowcampus.com, createdAt=2022-12-21T18:30:12.759521, updatedAt=2022-12-21T18:30:12.759521), UserTable(id=5, name=martin, email=martin@another.com, createdAt=2022-12-21T18:30:12.759521, updatedAt=2022-12-21T18:30:12.759521)]


```

### between

- 조건 양끝 값을 포함한 결과를 조회
- == `findBy...GreaterThanEqualAnd...LessThanEqual()`
- 쿼리 상의 논리 오류는 디버깅이 어렵기 때문에 주의해야 함

```java

List<UserTable> findByCreatedAtBetween(LocalDateTime yesterday, LocalDateTime tomorrow);
List<UserTable> findByIdBetween(Long id1, Long id2);

System.out.println("findByCreatedBetween : " + userTableRepository.findByCreatedAtBetween(LocalDateTime.now().minusDays(1L), LocalDateTime.now().plusDays(1L)));
System.out.println("findByIdBetween : " + userTableRepository.findByIdBetween(1L, 3L));


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
        usertable0_.created_at between ? and ?

-- findByCreatedBetween : [UserTable(id=1, name=martin, email=martin@fastcampus.com, createdAt=2022-12-21T18:36:22.313645, updatedAt=2022-12-21T18:36:22.313645), UserTable(id=2, name=dennis, email=dennis@fastcampus.com, createdAt=2022-12-21T18:36:22.315639, updatedAt=2022-12-21T18:36:22.315639), UserTable(id=3, name=sophia, email=sophia@slowcampus.com, createdAt=2022-12-21T18:36:22.316636, updatedAt=2022-12-21T18:36:22.316636), UserTable(id=4, name=james, email=james@slowcampus.com, createdAt=2022-12-21T18:36:22.316636, updatedAt=2022-12-21T18:36:22.316636), UserTable(id=5, name=martin, email=martin@another.com, createdAt=2022-12-21T18:36:22.316636, updatedAt=2022-12-21T18:36:22.316636)]

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
        usertable0_.id between ? and ?

-- findByIdBetween : [UserTable(id=1, name=martin, email=martin@fastcampus.com, createdAt=2022-12-21T18:36:22.313645, updatedAt=2022-12-21T18:36:22.313645), UserTable(id=2, name=dennis, email=dennis@fastcampus.com, createdAt=2022-12-21T18:36:22.315639, updatedAt=2022-12-21T18:36:22.315639), UserTable(id=3, name=sophia, email=sophia@slowcampus.com, createdAt=2022-12-21T18:36:22.316636, updatedAt=2022-12-21T18:36:22.316636)]

```

### isNonNull

- 조회 대상이 null이 아닌 경우 조회
```java
    List<UserTable> findByIdIsNotNull();

    System.out.println("findByIdIsNotNull : " + userTableRepository.findByIdIsNotNull());


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
        usertable0_.id is not null

-- findByIdIsNotNull : [UserTable(id=1, name=martin, email=martin@fastcampus.com, createdAt=2022-12-21T20:57:42.949206, updatedAt=2022-12-21T20:57:42.949206), UserTable(id=2, name=dennis, email=dennis@fastcampus.com, createdAt=2022-12-21T20:57:42.952199, updatedAt=2022-12-21T20:57:42.952199), UserTable(id=3, name=sophia, email=sophia@slowcampus.com, createdAt=2022-12-21T20:57:42.952199, updatedAt=2022-12-21T20:57:42.952199), UserTable(id=4, name=james, email=james@slowcampus.com, createdAt=2022-12-21T20:57:42.953195, updatedAt=2022-12-21T20:57:42.953195), UserTable(id=5, name=martin, email=martin@another.com, createdAt=2022-12-21T20:57:42.953195, updatedAt=2022-12-21T20:57:42.953195)]

```

### isNotEmpty

- 문자열의 notEmpty가 아닌 **collection의 notEmpty를 검사하는 것에 대해 주의 !**
- sql확인하기
 
1. 1:N 관계 entity 생성
   
```java
package com.jpa.fedeleo.bookmanager.domain;

import javax.persistence.*;

@Entity
public class Address {
    @Id
    private Long id;
}


```

2. UserTable과 참조

```java
package com.jpa.fedeleo.bookmanager.domain;

@Data
@Entity // 객체를 entity로 선언. 내부에 primaery key 선언이 필수
@Builder
@NoArgsConstructor
@AllArgsConstructor
@RequiredArgsConstructor
public class UserTable {
    
    ...

    @OneToMany(fetch= FetchType.EAGER)
    private List<Address> address;

}

// -----

System.out.println("findByIdIsNotEmpty : " + userTableRepository.findByAddressIsNotEmpty());

```
```sql
Hibernate: 
    select
        usertable0_.id as id1_1_,
        usertable0_.created_at as created_2_1_,
        usertable0_.email as email3_1_,
        usertable0_.name as name4_1_,
        usertable0_.updated_at as updated_5_1_ 
    from
        user_table usertable0_ 
    where
        exists (
            select
                address2_.id 
            from
                user_table_address address1_,
                address address2_ 
            where
                usertable0_.id=address1_.user_table_id 
                and address1_.address_id=address2_.id
        )


-- findByIdIsNotEmpty : []

```
- sql구문을 보면 서브쿼리를 사용해서 조회하는 것을 볼 수 있음
- ~실제로 많이 사용하지 않는 키워드~

<br>

### In

- in 절에 들어가는 리스트의 원소가 많아지면 성능 이슈 발생
- 사용 전 성늠 확인 요


```java
    List<UserTable> findByNameIn(List<String> names);

    System.out.println("findByIdIn : " + userTableRepository.findByNameIn(Lists.newArrayList("martin", "dennis")));

```

```sql
Hibernate: 
    select
        usertable0_.id as id1_1_,
        usertable0_.created_at as created_2_1_,
        usertable0_.email as email3_1_,
        usertable0_.name as name4_1_,
        usertable0_.updated_at as updated_5_1_ 
    from
        user_table usertable0_ 
    where
        usertable0_.name in (
            ? , ?
        )

-- findByIdIn : [UserTable(id=1, name=martin, email=martin@fastcampus.com, createdAt=2022-12-21T21:22:18.802482, updatedAt=2022-12-21T21:22:18.802482), UserTable(id=2, name=dennis, email=dennis@fastcampus.com, createdAt=2022-12-21T21:22:18.804478, updatedAt=2022-12-21T21:22:18.804478), UserTable(id=5, name=martin, email=martin@another.com, createdAt=2022-12-21T21:22:18.805475, updatedAt=2022-12-21T21:22:18.805475)]


```

### starting with, EndingWith, contains, Like

- 문자열 검색 지원
- like 절 사용
- 가독성을 위해 like절을 wrapping하여 다양한 키워드 제공
  - `spring Data jpa`는 코드 가독성을 중요시하는 library

```java
    List<UserTable> findByNameStartingWith(String name);
    List<UserTable> findByNameEndingWith(String name);
    List<UserTable> findByNameContains(String name);
    List<UserTable> findByNameLike(String name);


//-------------------

    System.out.println("findByNameStartingWith : " + userTableRepository.findByNameStartingWith("mar"));
    System.out.println("findByNameEndingWith : " + userTableRepository.findByNameEndingWith("tin"));
    System.out.println("findByNameContains : " + userTableRepository.findByNameContains("art"));
    System.out.println("findByNameLike : " + userTableRepository.findByNameLike("%art%"));




```
```sql

Hibernate: 
    select
        usertable0_.id as id1_1_,
        usertable0_.created_at as created_2_1_,
        usertable0_.email as email3_1_,
        usertable0_.name as name4_1_,
        usertable0_.updated_at as updated_5_1_ 
    from
        user_table usertable0_ 
    where
        usertable0_.name like ? escape ?
-- findByNameStartingWith : [UserTable(id=1, name=martin, email=martin@fastcampus.com, createdAt=2022-12-21T21:30:40.430860, updatedAt=2022-12-21T21:30:40.430860), UserTable(id=5, name=martin, email=martin@another.com, createdAt=2022-12-21T21:30:40.434852, updatedAt=2022-12-21T21:30:40.434852)]
Hibernate: 
    select
        usertable0_.id as id1_1_,
        usertable0_.created_at as created_2_1_,
        usertable0_.email as email3_1_,
        usertable0_.name as name4_1_,
        usertable0_.updated_at as updated_5_1_ 
    from
        user_table usertable0_ 
    where
        usertable0_.name like ? escape ?
-- findByNameEndingWith : [UserTable(id=1, name=martin, email=martin@fastcampus.com, createdAt=2022-12-21T21:30:40.430860, updatedAt=2022-12-21T21:30:40.430860), UserTable(id=5, name=martin, email=martin@another.com, createdAt=2022-12-21T21:30:40.434852, updatedAt=2022-12-21T21:30:40.434852)]
Hibernate: 
    select
        usertable0_.id as id1_1_,
        usertable0_.created_at as created_2_1_,
        usertable0_.email as email3_1_,
        usertable0_.name as name4_1_,
        usertable0_.updated_at as updated_5_1_ 
    from
        user_table usertable0_ 
    where
        usertable0_.name like ? escape ?
-- findByNameContains : [UserTable(id=1, name=martin, email=martin@fastcampus.com, createdAt=2022-12-21T21:30:40.430860, updatedAt=2022-12-21T21:30:40.430860), UserTable(id=5, name=martin, email=martin@another.com, createdAt=2022-12-21T21:30:40.434852, updatedAt=2022-12-21T21:30:40.434852)]

Hibernate: 
    select
        usertable0_.id as id1_1_,
        usertable0_.created_at as created_2_1_,
        usertable0_.email as email3_1_,
        usertable0_.name as name4_1_,
        usertable0_.updated_at as updated_5_1_ 
    from
        user_table usertable0_ 
    where
        usertable0_.name like ? escape ?
-- findByNameLike : [UserTable(id=1, name=martin, email=martin@fastcampus.com, createdAt=2022-12-21T21:34:45.921552, updatedAt=2022-12-21T21:34:45.921552), UserTable(id=5, name=martin, email=martin@another.com, createdAt=2022-12-21T21:34:45.925509, updatedAt=2022-12-21T21:34:45.925509)]

```

### is, nonKeyword, equals

- 모두 같은 결과 반환
- 가독성을 높이는 코드

```java
    Set<UserTable> findUserByNameIs(String name);
    Set<UserTable> findUserByName(String name);
    Set<UserTable> findUserByNameEquals(String name);

    // -----------------------

    System.out.println("findUserByNameIs : " + userTableRepository.findUserByNameIs("martin"));
    System.out.println("findUserByName : " + userTableRepository.findUserByName("martin"));
    System.out.println("findUserByNameEqual : " + userTableRepository.findUserByNameEquals("martin"));

```

```sql
Hibernate: 
    select
        usertable0_.id as id1_1_,
        usertable0_.created_at as created_2_1_,
        usertable0_.email as email3_1_,
        usertable0_.name as name4_1_,
        usertable0_.updated_at as updated_5_1_ 
    from
        user_table usertable0_ 
    where
        usertable0_.name=?
-- findUserByNameIs : [UserTable(id=1, name=martin, email=martin@fastcampus.com, createdAt=2022-12-21T21:46:07.920241, updatedAt=2022-12-21T21:46:07.920241), UserTable(id=5, name=martin, email=martin@another.com, createdAt=2022-12-21T21:46:07.923235, updatedAt=2022-12-21T21:46:07.923235)]

Hibernate: 
    select
        usertable0_.id as id1_1_,
        usertable0_.created_at as created_2_1_,
        usertable0_.email as email3_1_,
        usertable0_.name as name4_1_,
        usertable0_.updated_at as updated_5_1_ 
    from
        user_table usertable0_ 
    where
        usertable0_.name=?
-- findUserByName : [UserTable(id=1, name=martin, email=martin@fastcampus.com, createdAt=2022-12-21T21:46:07.920241, updatedAt=2022-12-21T21:46:07.920241), UserTable(id=5, name=martin, email=martin@another.com, createdAt=2022-12-21T21:46:07.923235, updatedAt=2022-12-21T21:46:07.923235)]

Hibernate: 
    select
        usertable0_.id as id1_1_,
        usertable0_.created_at as created_2_1_,
        usertable0_.email as email3_1_,
        usertable0_.name as name4_1_,
        usertable0_.updated_at as updated_5_1_ 
    from
        user_table usertable0_ 
    where
        usertable0_.name=?
-- findUserByNameEqual : [UserTable(id=1, name=martin, email=martin@fastcampus.com, createdAt=2022-12-21T21:46:07.920241, updatedAt=2022-12-21T21:46:07.920241), UserTable(id=5, name=martin, email=martin@another.com, createdAt=2022-12-21T21:46:07.923235, updatedAt=2022-12-21T21:46:07.923235)]


```

## 2. ueryMethod를 통한 paging과 sort 구현

### 키워드를 이용한 sorting

```java
    List<UserTable> findTop1ByName(String name);
    List<UserTable> findTop1ByNameOrderByIdDesc(String name);
    List<UserTable> findFirstByNameOrderByIdDescEmailAsc(String name);

    //---------------------------
    System.out.println("findTop1ByName : " + userTableRepository.findTop1ByName("martin"));
    System.out.println("findTop1ByNameOrderByIdDesc : " + userTableRepository.findTop1ByNameOrderByIdDesc("martin"));
    System.out.println("findFirstByNameOrderByIdDescEmailAsc : " + userTableRepository.findFirstByNameOrderByIdDescEmailAsc("martin"));

```

```sql

Hibernate: 
    select
        usertable0_.id as id1_1_,
        usertable0_.created_at as created_2_1_,
        usertable0_.email as email3_1_,
        usertable0_.name as name4_1_,
        usertable0_.updated_at as updated_5_1_ 
    from
        user_table usertable0_ 
    where
        usertable0_.name=? limit ?
-- findTop1ByName : [UserTable(id=1, name=martin, email=martin@fastcampus.com, createdAt=2022-12-21T22:02:53.952966, updatedAt=2022-12-21T22:02:53.952966)]

Hibernate: 
    select
        usertable0_.id as id1_1_,
        usertable0_.created_at as created_2_1_,
        usertable0_.email as email3_1_,
        usertable0_.name as name4_1_,
        usertable0_.updated_at as updated_5_1_ 
    from
        user_table usertable0_ 
    where
        usertable0_.name=? 
    order by
        usertable0_.id desc limit ?
-- findTop1ByNameOrderByIdDesc : [UserTable(id=5, name=martin, email=martin@another.com, createdAt=2022-12-21T22:02:53.963938, updatedAt=2022-12-21T22:02:53.963938)]

Hibernate: 
    select
        usertable0_.id as id1_1_,
        usertable0_.created_at as created_2_1_,
        usertable0_.email as email3_1_,
        usertable0_.name as name4_1_,
        usertable0_.updated_at as updated_5_1_ 
    from
        user_table usertable0_ 
    where
        usertable0_.name=? 
    order by
        usertable0_.id desc,
        usertable0_.email asc limit ?
-- findFirstByNameOrderByIdDescEmailAsc : [UserTable(id=5, name=martin, email=martin@another.com, createdAt=2022-12-21T22:23:44.666843, updatedAt=2022-12-21T22:23:44.666843)]

```

### parameter를 활용한 sorting


```java

    List<UserTable> findByName(String name, Sort sort);

    //-----------------------
    System.out.println("findByName(String name, Sort sort) : " + userTableRepository.findByName("martin", Sort.by(Sort.Order.desc("id"))));
    
```
```sql

Hibernate: 
    select
        usertable0_.id as id1_1_,
        usertable0_.created_at as created_2_1_,
        usertable0_.email as email3_1_,
        usertable0_.name as name4_1_,
        usertable0_.updated_at as updated_5_1_ 
    from
        user_table usertable0_ 
    where
        usertable0_.name=? 
    order by
        usertable0_.id desc

-- findByName(String name, Sort sort) : [UserTable(id=5, name=martin, email=martin@another.com, createdAt=2022-12-22T00:37:25.226473, updatedAt=2022-12-22T00:37:25.226473), UserTable(id=1, name=martin, email=martin@fastcampus.com, createdAt=2022-12-22T00:37:25.223479, updatedAt=2022-12-22T00:37:25.223479)]


```
  
- 코드의 가독성 측면에서 메서드가 계속 길어지는 것보다 좋음
- 매개변수로 Order클래스를 필요한 정렬에 따라 커스텀해서 전달할 수 있음

    ```java
        System.out.println("findByName(String name, Sort sort) : " + userTableRepository.findByName("martin", getSort()));

        private Sort getSort(){
        return Sort.by(
                Sort.Order.desc("id"),
                Sort.Order.asc("email"),
                Sort.Order.desc("createdAt"),
                Sort.Order.asc("updatedAt")

        )}


    ```

### pageable 클래스를 이용한 sort

- `Page` 클래스
  - `Slice` 클래스를 상속받음
    - 데이터 묶음의 일부 덩어리를 의미함
    - 현재 slice에 대한 값을 처리하는 메서드 제공
  - `getTotalPages()`, `getTotalElements()`, `empty()` 메서드 제공
  - 전체 레코드에 대한 값을 처리하는 메서드 제공
    - 즉, **전체 레코드에 대한 값 처리, 일부에 대한 레코드 값 처리 메서드를 가지고 있음**
  - 응답 값

- `Pageable` 클래스
  - 요청 값
  - `Page` 클래스와 메서드가 유사함

```java
    Page<UserTable> findByName(String name, Pageable pageable);
    // --------------------
    System.out.println("findByName(String name, Pageable pageable) : " + userTableRepository.findByName("martin", PageRequest.of(0, 1, Sort.by(Sort.Order.desc("id")))).getContent());
```

```sql
Hibernate: 
    select
        usertable0_.id as id1_1_,
        usertable0_.created_at as created_2_1_,
        usertable0_.email as email3_1_,
        usertable0_.name as name4_1_,
        usertable0_.updated_at as updated_5_1_ 
    from
        user_table usertable0_ 
    where
        usertable0_.name=? 
    order by
        usertable0_.id desc limit ?

Hibernate: -- getContent() 메서드에 대한 query
    select
        count(usertable0_.id) as col_0_0_ 
    from
        user_table usertable0_ 
    where
        usertable0_.name=?

-- findByName(String name, Pageable pageable) : [UserTable(id=5, name=martin, email=martin@another.com, createdAt=2022-12-22T01:30:19.994463, updatedAt=2022-12-22T01:30:19.994463)]


```
