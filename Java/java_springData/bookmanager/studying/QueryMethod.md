# QueryMethod 활용

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