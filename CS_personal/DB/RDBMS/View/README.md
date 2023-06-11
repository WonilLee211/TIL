# View

### 목차

1. [개요](#1-개요)
2. [사용법](#2-사용법)
---

# 1. 개요

- 가상의 테이블
- 하나 이상의 기본 테이블에서 가져온 데이터를 쿼리를 통해 정의한 형태로 나타내는 개체
- 데이터베이스에 저장되는 실제 데이터를 가지지 않고 필요한 데이터를 쿼리를 통해 동적으로 생성하여 제공


# 2. 사용법

1. view 생성

```sql
CREATE VIEW my_view AS
SELECT c1, c2
FROM my_table
WHERE condition
;
```

2. view 조회

```sql
SELECT * FROM my_view;
```

3. View 갱신

```sql
UPDATE my_view
SET c1 = value
WHERE condition
;
```

4. view  수정 또는 삭제

```sql
-- view 수정
ALTER VIEW my_view AS
SELECT c1, c3
FROM my_table
WHERE condition
;
-- view 삭제
DROP VIEW my_view;
```

