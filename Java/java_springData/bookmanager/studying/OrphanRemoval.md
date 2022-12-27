# JPA에서 Orphan Removal 활용하기

- 부모 엔터티의 관계 어노테이션의 옵션

### orphanRemoval=true  vs  CascadeType.REMOVE

- Parent가 삭제 되었을 때 Child도 함께 삭제시키는 역할을 수행하는 점에선 동일

- 다른 점
- 관계를 끊는 것에 대한 응답!
  - 만약 Parent의 Child 값을 null을 주었다고 가정
  - `orphanRemoval=true` : 관계가 끊어진 child를 자동으로 제거한다. 
  - `CascadeType.REMOVE` : 관계가 끊어진 child를 자동 제거하지 않는다.
    - 관계가 끊어졌다는 것을 제거로 보지 않기 때문에


## 요약

- `CascadeType.REMOVE` : 관계가 없는 데이터라도 남겨야 할 때 사용
- `orphanRemoval=true` : 관계가 없는 데이터는 삭제할 때 사용


# soft delete

- 현업에서 가장 많이 사용하는 flag를 이용한 Delete 기능

## `@DWhere(clause = "")`

- @Where가 달린 엔터티가 조회될 때 항상 실행되는 조건절을 생성
- 내부에 쿼리를 생성하는 메서드를 만들 때 반복적인 조건을 달지 않아도 된다.
  



