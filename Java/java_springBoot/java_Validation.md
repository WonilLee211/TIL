# Validation

- 특히 Java에서는 null 값에 대해서 접근하려고 할 때 null pointer exceptionO| 발생 함으로, 이러한 부분을 방지 하기 위해서 미리 검증을 하는 과정을 Validation 이라고 합니다.
- 예)
```java
public void run(String account Spring pwf int age){
    if(account== null || pw == null){ 
        return
    }
    if(age == 0){
        return
    }
}
```

## 단점

1. 검증해야 할 값이 많은 경우 코드의 길이가 길어진다
2. 구현에 따라서 달라 질 수 있지만 Service Logic과의 분리가 필요 하다.
3. 흩어져 있는 경우 어디에서 검증을 하는지 알기 어려우며, 재사용의 한계가 있다.
4. 구현에 따라 달라질 수 있지만, 검증 Logic이 변경 되는 경우 테스트 코드 등 참조하는 클래스에서 Logic이 변경되어야 하는 부분이 발생할 수 있다.

## validation annotation

1. `@Size` : 문자 길이 측정
2. `@NotNull` : null 불가
3. `@NotEmpty` : null, ""불가
4. `@NotBlank` : null, "", " " 불가
5. `@Past` : 과거 날짜
6. `@PastOrPresent` : 오늘이거나 과거날짜
7. `@Future` : 미래날짜
8. `@FutureOrPresent` : 오늘이거나 미래날짜
9. `@Pattern` : 정규식 적용
10. `@Max` : 최댓값
11. `@Min` : 최소값
12. `@AssertTrue/ False` : 별도 Logic 적용
13. `@Valid` : 해당 object validation 실행


l.gradle dependecies
    - `implementation(,,org.springframework.boot：pring-boot-starter-validation")`

2.  bean validation spec

    -  `https://beanvalidation.org/2.0-jsr80/`

3. 핸드폰 번호 정규식

    - `"\\d{2, 3}-\\d{3,4}-\\d{4}$"`

## Validation 모범사례

