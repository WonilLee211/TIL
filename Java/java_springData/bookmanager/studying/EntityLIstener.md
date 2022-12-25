# Entity Listener

# JPA에서 제공하는 7가지 Listener

## 목적

- entity 내부에 listener를 추가함으로써 객체의 정보 변화를 감시할 때 사용
- 무분별한 테스트코드 증가를 방지함

1. `@PrePersist`
2. `@PreUpdate`
3. `@PreRemove`
4. `@PostPersist`
5. `@PostUpdate`
6. `@PostRemove`
7. `@PostLoad`

## 1. `@PrePersist`

- insert메서드가 실행되기 전에 실행
- Auditing할 때 많이 사용함

## 2. `@PreUpdate`

- merge메서드가 실행되기 전에 실행

## 3. `@PreRemove`

- delete 메서드가 호출되기 전에 실행

## 4. `@PostPersist`

- insert메서드가 실행된 후 실행
- Auditing할 때 많이 사용함

## 5. `@PostUpdate`

- merge메서드가 실행된 후 실행

## 6. `@PostRemove`

- delete 메서드가 호출된 후 실행

## 7. `@PostLoad`

- select메서드가 실행된 이 후에 실행


```java
package com.jpa.fedeleo.bookmanager.domain;

@Data
@Entity // 객체를 entity로 선언. 내부에 primaery key 선언이 필수
@Builder
@NoArgsConstructor
@AllArgsConstructor
@RequiredArgsConstructor
@Table(indexes = {@Index(columnList = "name")}, uniqueConstraints = {@UniqueConstraint(columnNames = {"email"})})
public class UserTable {

    @Id // pk
    @GeneratedValue // autoincrement,
    private Long id;
    @NonNull
    private String name;
    @NonNull
    private String email;
    @Column(updatable = false)
    private LocalDateTime createdAt;
    @Column(insertable = false)
    private LocalDateTime updatedAt;
    @Enumerated(value = EnumType.STRING)
    private Gender gender;

    @PrePersist
    public void prePersist(){
        System.out.println(">>> prePersist");
    }

    @PostPersist
    public void postPersist(){
        System.out.println(">>> postPersist");
    }
    @PreUpdate
    public void PreUpdate(){
        System.out.println(">>> PreUpdate");
    }

    @PostUpdate
    public void PostUpdate(){
        System.out.println(">>> PostUpdate");
    }

    @PreRemove
    public void PreRemove(){
        System.out.println(">>> PreRemove");
    }

    @PostRemove
    public void PostRemove(){
        System.out.println(">>> PostRemove");
    }

    @PostLoad
    public void PostLoad(){
        System.out.println(">>> PostLoad");
    }

}
//------------------------------------
package com.jpa.fedeleo.bookmanager.repository;

@SpringBootTest
class UserTableRepositoryTest {

    @Autowired
    private UserTableRepository userTableRepository;

    ...

    @Test
    void Listener(){
        UserTable user = new UserTable();
        user.setName("martin");
        user.setEmail("martin@naver.com");

        userTableRepository.save(user);

        UserTable user2 = userTableRepository.findById(4L).orElseThrow(RuntimeException::new);
        user2.setName("marrrrrtin");

        userTableRepository.save(user2);
        userTableRepository.deleteById(4L);

    }
}

```

```sql

>>> prePersist

Hibernate: 
    call next value for hibernate_sequence
Hibernate: 
    insert 
    into
        user_table
        (created_at, email, gender, name, id) 
    values
        (?, ?, ?, ?, ?)

>>> postPersist

Hibernate: 
    select
        usertable0_.id as id1_1_0_,
        usertable0_.created_at as created_2_1_0_,
        usertable0_.email as email3_1_0_,
        usertable0_.gender as gender4_1_0_,
        usertable0_.name as name5_1_0_,
        usertable0_.updated_at as updated_6_1_0_ 
    from
        user_table usertable0_ 
    where
        usertable0_.id=?

>>> PostLoad

Hibernate: 
    select
        usertable0_.id as id1_1_0_,
        usertable0_.created_at as created_2_1_0_,
        usertable0_.email as email3_1_0_,
        usertable0_.gender as gender4_1_0_,
        usertable0_.name as name5_1_0_,
        usertable0_.updated_at as updated_6_1_0_ 
    from
        user_table usertable0_ 
    where
        usertable0_.id=?

>>> PostLoad
>>> PreUpdate

Hibernate: 
    update
        user_table 
    set
        email=?,
        gender=?,
        name=?,
        updated_at=? 
    where
        id=?

>>> PostUpdate

Hibernate: 
    select
        usertable0_.id as id1_1_0_,
        usertable0_.created_at as created_2_1_0_,
        usertable0_.email as email3_1_0_,
        usertable0_.gender as gender4_1_0_,
        usertable0_.name as name5_1_0_,
        usertable0_.updated_at as updated_6_1_0_ 
    from
        user_table usertable0_ 
    where
        usertable0_.id=?

>>> PostLoad
>>> PreRemove

Hibernate: 
    delete 
    from
        user_table 
    where
        id=?
>>> PostRemove

```
## 2. 리스너 활용

### 1. 클래스 내부 리스너

```java

package com.jpa.fedeleo.bookmanager.domain;

@Data
@Entity // 객체를 entity로 선언. 내부에 primaery key 선언이 필수
@Builder
@NoArgsConstructor
@AllArgsConstructor
@RequiredArgsConstructor
//@Table(indexes = {@Index(columnList = "name")}, uniqueConstraints = {@UniqueConstraint(columnNames = {"email"})})
public class UserTable {

    ...

    @PrePersist
    public void prePersist(){
        this.createdAt = LocalDateTime.now();
        this.updatedAt = LocalDateTime.now();

    }

    @PreUpdate
    public void PreUpdate(){
        this.updatedAt = LocalDateTime.now();
    }

}

```

### 2. 추상화된 EntityListener

- `@EntityListener`

- 추상화 수준 높이기

-  반복되는 메서드를 인터페이스로 만들기

```JAVA
package com.jpa.fedeleo.bookmanager.domain;

public interface Auditable {
    LocalDateTime getCreatedAt();
    LocalDateTime getUpdatedAt();

    void setCreatedAt(LocalDateTime createdAt);
    void setUpdatedAt(LocalDateTime updatedAt);
}

```

- `Auditable` 인터페이스의 메서드를 이용하는 엔터티 리스너

```java
package com.jpa.fedeleo.bookmanager.domain;

public class MyEntityListener {

    @PrePersist
    public void prePersist(Object o){
        if(o instanceof Auditable){
            ((Auditable) o).setCreatedAt(LocalDateTime.now());
            ((Auditable) o).setUpdatedAt(LocalDateTime.now());
        }
    }
    @PreUpdate
    public void preUpdate(Object o){
        if(o instanceof Auditable){
            ((Auditable) o).setUpdatedAt(LocalDateTime.now());
        }
    }
}

```

- `@EntityListener`로 MyEntityListener 등록
- `Auditable`인터페이스 구현을 통해 객체에서 메서드 사용할 수 있도록 함

```java
package com.jpa.fedeleo.bookmanager.domain;

@Entity
@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
@EntityListeners(value = MyEntityListener.class)
public class Book implements Auditable{
    @Id
    @GeneratedValue
    private Long id;

    private String name;

    private String author;

    private LocalDateTime createdAt;

    private LocalDateTime updatedAt;

}

// ------------------
package com.jpa.fedeleo.bookmanager.domain;

@Data
@Entity
@Builder
@NoArgsConstructor
@AllArgsConstructor
@RequiredArgsConstructor
@EntityListeners(value = MyEntityListener.class)
public class UserTable implements Auditable{

    @Id
    @GeneratedValue
    private Long id;
    @NonNull
    private String name;
    @NonNull
    private String email;
    @Column(updatable = false)
    private LocalDateTime createdAt;
    @Column(insertable = false)
    private LocalDateTime updatedAt;
    @Enumerated(value = EnumType.STRING)
    private Gender gender;
}

```

### 3. 객체의 생성 수정 history 저장하는 listener

- UserTable 객체의 생성 수정 history 저장하는 repository

```java
package com.jpa.fedeleo.bookmanager.repository;

public interface UserHistoryRepository extends JpaRepository<UserHistory, Long> {
}

```

- UserHistory 

```java
package com.jpa.fedeleo.bookmanager.domain;

@Entity
@NoArgsConstructor
@Data
@EntityListeners(value = MyEntityListener.class)
public class UserHistory implements Auditable{
    @Id
    @GeneratedValue
    private Long id;

    private Long UserId;

    private String name;

    private String email;

    private LocalDateTime createdAt;

    private LocalDateTime updatedAt;
}
```

> 주의 
>  - entityListener클래스는 spring bean을 주입받지 못함
>  - nullPointException 발생
>>> ApplicationContextAware 인터페이스를 구현하여 Bean을 받을 수 있는 메서드를 구현해야 함

```java
package com.jpa.fedeleo.bookmanager.support;

@Component
public class BeanUtils implements ApplicationContextAware {

    private static ApplicationContext applicationContext;
    @Override
    public void setApplicationContext(ApplicationContext applicationContext) throws BeansException {
        BeanUtils.applicationContext = applicationContext;

    }

    public static <T> T getBean(Class<T> clazz){
        return applicationContext.getBean(clazz);
    }
}

```

- BeanUtils을 이용하여 Bean인 UserHistoryRepository를 EntityListener에서 사용하기
  
```java
package com.jpa.fedeleo.bookmanager.domain;

//@Component
public class UserEntityListener {

//    entityListener클래스는 spring bean을 주입받지 못함
//    @Autowired
//    private UserHistoryRepository userHistoryRepository;

    @PrePersist
    @PreUpdate
    public void prePersistAndPreUpdate(Object o){
        // BeanUtils을 이용하여 Bean인 UserHistoryRepository를 EntityListener에서 사용하기
        UserHistoryRepository userHistoryRepository = BeanUtils.getBean(UserHistoryRepository.class);
        
        UserTable user = (UserTable) o;

        UserHistory userHistory = new UserHistory();
        userHistory.setUserId(user.getId());
        userHistory.setName(user.getName());
        userHistory.setEmail(user.getEmail());

        userHistoryRepository.save(userHistory);

    }
}
```

- 객체에 entityListener 등록

```java
package com.jpa.fedeleo.bookmanager.domain;

import lombok.*;

import javax.persistence.*;
import java.time.LocalDateTime;
import java.util.List;

@Data
@Entity // 객체를 entity로 선언. 내부에 primaery key 선언이 필수
@Builder
@NoArgsConstructor
@AllArgsConstructor
@RequiredArgsConstructor
@EntityListeners(value = {MyEntityListener.class, UserEntityListener.class})
public class UserTable implements Auditable{

    @Id // pk
    @GeneratedValue // autoincrement,
    private Long id;
    @NonNull
    private String name;
    @NonNull
    private String email;
    @Column(updatable = false)
    private LocalDateTime createdAt;
    @Column(insertable = false)
    private LocalDateTime updatedAt;
    @Enumerated(value = EnumType.STRING)
    private Gender gender;

}
```

### 4. spring jpa 기본 Listener

- 애플리케이션에 `@EnableJpaAuditing` 달기

```java

package com.jpa.fedeleo.bookmanager;

@SpringBootApplication
@EnableJpaAuditing
public class BookmanagerApplication {

	public static void main(String[] args) {
		SpringApplication.run(BookmanagerApplication.class, args);
	}
}

```

- EntityListeners에 `AuditingEntityListener` 클래스 추가
- 각 필드에 `@CreatedDate`, `@LastModifiedDate` 추가

```java
package com.jpa.fedeleo.bookmanager.domain;

@Data
@Entity
@Builder
@NoArgsConstructor
@AllArgsConstructor
@RequiredArgsConstructor
@EntityListeners(value = {AuditingEntityListener.class, UserEntityListener.class})
public class UserTable implements Auditable{

    ...

    @Column(updatable = false)
    @CreatedDate
    private LocalDateTime createdAt;

    @Column(insertable = false)
    @LastModifiedDate
    private LocalDateTime updatedAt;

}
// -------------------------------------------------------------

package com.jpa.fedeleo.bookmanager.domain;

@Entity
@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
@EntityListeners(value = AuditingEntityListener.class)
public class Book implements Auditable{

    ...
    @CreatedDate
    private LocalDateTime createdAt;

    @LastModifiedDate
    private LocalDateTime updatedAt;

}
//------------------------------------------------------
package com.jpa.fedeleo.bookmanager.domain;

@Entity
@NoArgsConstructor
@Data
@EntityListeners(value = AuditingEntityListener.class)
public class UserHistory implements Auditable{
    ...

    @CreatedDate
    private LocalDateTime createdAt;

    @LastModifiedDate
    private LocalDateTime updatedAt;

}

```

> `AuditingEntityListener`
> - `@LastModifiedBy`/ `@CreatedBy` 등
>  예 
    ```java

    package org.springframework.data.annotation;

    ...

    @Retention(RetentionPolicy.RUNTIME)
    @Target(value = { FIELD, METHOD, ANNOTATION_TYPE })
    public @interface CreatedBy {
    }
    ```

## 실전형 refactoring

### `@MappedSuperclass`

![mappedSuperClass](img/mappedSuperClass.png)

- 상속광계 매핑이 아니다.
- MappedSuperclass가 선언되어 있는 클래스는 엔티티가 아니다. 당연히 테이블과 매핑도 안된다.
- 단순히 부모 클래스를 상속 받는 자식 클래스에 매핑 정보만 제공한다.
- 조회, 검색이 불가하다. 부모 타입으로 조회하는 것이 불가능하다는 이야기.(em.find(BaseEntity) 불가능)
- 직접 생성해서 사용할 일이 없으므로 추상 클래스로 만드는 것을 권장한다.
- 테이블과 관계가 없고, 단순히 엔티티가 공통으로 사용하는 매핑 정보를 모으는 역할을 한다.
- 주로 등록일, 수정일, 등록자, 수정자 같은 전체 엔티티에서 공통으로 적용하는 정보를 모을 때 사용한다.

```java

package com.jpa.fedeleo.bookmanager.domain;

@Data
@MappedSuperclass // 객체별로 공통매핑정보가 필요할 때 부모클래스에 선언하고 속성만 상속받아서 사용하고 싶을 때
@EntityListeners(value = AuditingEntityListener.class)
public class BaseEntity {
    @CreatedDate
    private LocalDateTime createdAt;

    @LastModifiedDate
    private LocalDateTime updatedAt;

}


```

- 공통 매핑 정보가 필요한 객체에 상속시킴
- `@ToString(callSuper=true)` : 부모의 toString()함꼐 호출할 수 있도록 함
- `@EqualsAndHashCode(callSuper = true)` : callSuper 속성을 통해 eqauls와 hashCode 메소드 자동 생성 시 부모 클래스의 필드까지 감안할지의 여부를 설정
  
> 주의 BaseEntity클래스의 ToString, EqualsAndHashCode 메서드를 사용해야할 때 `@Data`를 사용하면 callSuper 옵션을 줄 수 없다.
>  - 각자의 어노테이션을 달아서 callSuper옵션을 달아줘야 함

```java
package com.jpa.fedeleo.bookmanager.domain;

@ToString(callSuper = true) // 부모의 toString()함꼐 호출할 수 있도록 함
@EqualsAndHashCode(callSuper = true)
@Data
@Entity // 객체를 entity로 선언. 내부에 primaery key 선언이 필수
@Builder
@NoArgsConstructor
@AllArgsConstructor
@RequiredArgsConstructor
@EntityListeners(value = {UserEntityListener.class})
public class UserTable extends BaseEntity  implements Auditable {

    @Id // pk
    @GeneratedValue // autoincrement,
    private Long id;
    @NonNull
    private String name;
    @NonNull
    private String email;
    @Enumerated(value = EnumType.STRING)
    private Gender gender;

}
// ----------------------------------------------

package com.jpa.fedeleo.bookmanager.domain;

@ToString(callSuper = true)
@EqualsAndHashCode(callSuper = true)
@Entity
@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class Book extends BaseEntity implements Auditable {
    @Id
    @GeneratedValue
    private Long id;

    private String name;

    private String author;

}
// ----------------------------------------

package com.jpa.fedeleo.bookmanager.domain;

@ToString(callSuper = true)
@EqualsAndHashCode(callSuper = true)
@Entity
@NoArgsConstructor
@Data
public class UserHistory extends BaseEntity implements Auditable {
    @Id
    @GeneratedValue
    private Long id;

    private Long UserId;

    private String name;

    private String email;

}
// ------------------------------------
@Test
void UserHistoryTest(){
    UserTable user = new UserTable();
    user.setEmail("martin-new@fastcampus.com");
    user.setName("martin-new");

    userTableRepository.save(user);

    user.setName("martin-new-new");
    userTableRepository.save(user);

    userHistoryRepository.findAll().forEach(System.out::println);
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
        user_history
        (created_at, updated_at, user_id, email, name, id) 
    values
        (?, ?, ?, ?, ?, ?)
Hibernate: 
    insert 
    into
        user_table
        (created_at, updated_at, email, gender, name, id) 
    values
        (?, ?, ?, ?, ?, ?)
Hibernate: 
    select
        usertable0_.id as id1_3_0_,
        usertable0_.created_at as created_2_3_0_,
        usertable0_.updated_at as updated_3_3_0_,
        usertable0_.email as email4_3_0_,
        usertable0_.gender as gender5_3_0_,
        usertable0_.name as name6_3_0_ 
    from
        user_table usertable0_ 
    where
        usertable0_.id=?
Hibernate: 
    call next value for hibernate_sequence
Hibernate: 
    insert 
    into
        user_history
        (created_at, updated_at, user_id, email, name, id) 
    values
        (?, ?, ?, ?, ?, ?)
Hibernate: 
    update
        user_table 
    set
        created_at=?,
        updated_at=?,
        email=?,
        gender=?,
        name=? 
    where
        id=?
Hibernate: 
    select
        userhistor0_.id as id1_2_,
        userhistor0_.created_at as created_2_2_,
        userhistor0_.updated_at as updated_3_2_,
        userhistor0_.user_id as user_id4_2_,
        userhistor0_.email as email5_2_,
        userhistor0_.name as name6_2_ 
    from
        user_history userhistor0_
        
-- UserHistory(super=BaseEntity(createdAt=2022-12-24T16:22:58.977690, updatedAt=2022-12-24T16:22:58.977690), id=6, UserId=null, name=martin-new, email=martin-new@fastcampus.com)
-- UserHistory(super=BaseEntity(createdAt=2022-12-24T16:22:59.129710, updatedAt=2022-12-24T16:22:59.129710), id=8, UserId=7, name=martin-new-new, email=martin-new@fastcampus.com)


```