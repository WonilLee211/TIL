# 영속성 전이


- 특정 엔티티를 영속성 상태로 만들때 연관되어진 엔티티도 함께 영속성 상태로 변경 하는 것
- JPA 에서는 부모 엔티티를 영속성 상태로 변경 하면 자식도 함께 변경 될 수 있도록 하는 기능을 제공
- **cascade**
  - @OneToMany, @ManyToOne 옵션 값 (parent-child 관계 일 때)
  - **기본 값은 빈 배열**임
- 처음엔 그냥 `cascade = CascadeType.All`로 지정함
  - 세부 조건이 필요할 땐 배열로 여러 조합을 입력하기
  

## 영속성 전이 옵션 정보

|옵션 | 정보 |
| --- | --- |
| `CascadeType.ALL` | 모두 적용 |
| `CascadeType.PERSIST` | 연관관계의 객체가 영속되면 다른 관계의 객체도 영속되도록 함 |
| `CascadeType.MERGE` | db에 저장된 값을 불러와 수정할 때 관계된 엔티티도 반영하겠다는 의미 |
| `CascadeType.REMOVE` | 부모를 삭제 하면 연관된 자식도 삭제 |
| `CascadeType.REFRESH` | 엔티티를 로딩할 때 연관관계가 있는 엔티티도 함께 재로딩하겠다는 의미 |
| `CascadeType.DETACH` | 영속성으로 관리하지 않겠다는 의미로 컨텍스트에서 분리시킴 |


## `CascadeType.PERSIST`

- 아래는 영속성 컨텍스트에 관리되지 않는 객체끼리 관계를 형성하도록 할 때 에러 발생

```java
package com.jpa.fedeleo.bookmanager.repository;

@SpringBootTest
public class BookRepositoryTest {

    ...

    @Test
     void bookCascadeTest(){
        Book book = new Book();
        book.setName("jpa cascade");

        Publisher publisher = new Publisher();
        publisher.setName("패스트캠퍼스");

        book.setPublisher(publisher);
        bookRepository.save(book);

        publisher.addBook(book);
        publisherRepository.save(publisher);

        System.out.println("books : " + bookRepository.findAll());
        System.out.println("publishers : " + publisherRepository.findAll());

    }
}

org.hibernate.TransientPropertyValueException: object references an unsaved transient instance - save the transient instance before flushing : com.jpa.fedeleo.bookmanager.domain.Book.publisher -> com.jpa.fedeleo.bookmanager.domain.Publisher; nested exception is java.lang.IllegalStateException: org.hibernate.TransientPropertyValueException: object references an unsaved transient instance - save the transient instance before flushing : com.jpa.fedeleo.bookmanager.domain.Book.publisher -> com.jpa.fedeleo.bookmanager.domain.Publisher
```

- `TransientPropertyValueException : ~ object references an unsaved transient instance`
- 여기서 이를 해결하는 옵션

```java
package com.jpa.fedeleo.bookmanager.domain;

...

@ToString(callSuper = true)
@EqualsAndHashCode(callSuper = true)
@Entity
@Data
@NoArgsConstructor
public class Book extends BaseEntity {

    ...

    @ManyToOne(cascade = CascadeType.PERSIST)
    @ToString.Exclude
    private Publisher publisher;

}
```

- **publisher에 book을 저장하려할 떄 book 또한 persist가 실행됨**

### 주의 ! perist 후 다시 불러와서 merge 한다면?

```java

    @Test
     void bookCascadeTest(){
        Book book = new Book();
        book.setName("jpa cascade");

        Publisher publisher = new Publisher();
        publisher.setName("패스트캠퍼스");

        book.setPublisher(publisher);
        bookRepository.save(book);

        publisher.addBook(book);
        publisherRepository.save(publisher);

        System.out.println("books : " + bookRepository.findAll());
        System.out.println("publishers : " + publisherRepository.findAll());

        // db에 저장된 값을 불러와 수정하기 때문에 merge 발생!
        Book book1 = bookRepository.findById(1L).get();
        book1.getPublisher().setName("슬로우");

        bookRepository.save(book1);

        System.out.println("publisher : " + publisherRepository.findAll());

    }
```

- db에 저장된 값을 불러와 수정하기 때문에 merge 발생!

- `publisher : [Publisher(super=BaseEntity(createdAt=2022-12-27T22:41:32.329065, updatedAt=2022-12-27T22:41:32.509581), id=1, name=패스트캠퍼스)]`
- 결과 값이 바뀌지 않음을 볼 수 있음
- 영속성 전이만 일어나고 MERGE에 대해서는 영속성 전이가 되지 않음

### 해결

- CascadeType.MERGE 옵션 추가하기

```java

    @ManyToOne(cascade = {CascadeType.PERSIST, CascadeType.MERGE})
    @ToString.Exclude
    private Publisher publisher;

```

## 영속성 상태 삭제(CascadeType.REMOVE)

- 영속성 상태에서 삭제를 하기 위해서는 아래 예와 같이 자식 엔티티를 삭제 한뒤 부모 엔티티를 삭제 해야 합니다.

```java
Member member = em.find(Member.class, "1");
Teacher teacher = em.find(Teacher.class, "1");
em.remove(teacher);
em.remove(member);

```

- `@ManyToOne(cascade = CascadeType.REMOVE)`: 부모를 삭제 하면 연관된 자식도 삭제

```java
Member member = em.find(Member.class, "1");
em.remove(member);

```

### 특징

- 관계가 없는 데이터가 남게 된다.

