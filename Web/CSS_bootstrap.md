# Bootstrap

## 부트스트랩이란?

- 빠르고 반응형 웹을 만드는 라이브러리

## 1. 부트스트랩 연습

- [https://getbootstrap.com/docs](https://getbootstrap.com/docs) 에서 가져와서 쓰면 됨

---

# Bootstrap 기본 원리

## 1. Spacing(margin and padding)

- CSS는 완성되어 있음
- 우리는 클래스만 지정하면 됨
- 원리와 규칙이 존재함
- 선택자를 볼 필요가 없다

### 1.1 {property}{sides}-{size}

- ex> mt-3 : 마진 탑 3

### 1.2 property 종류

- m : margin
- p : padding

### 1.3 side 종류

- t : 마진이나 패딩의 top
- s : LTR에서 margin/padding-left가 지정된 클래스들의 start
- b : 마진이나 패딩의 bottom
- e : LTR에서 margin/padding-left가 지정된 클래스들의 end
- x : x방향
- y : y방향
- blank

### 1.4 sizing

|class name|rem|px|

|—|—|—|

|m-1 | 0.25 | 4|

|m-2 | 0.5 | 8|

|m-3 | 1 | 16|

|m-4 | 1.5 | 24|

|m-5 | 3 | 48|

### 예시

- mx - 0 : 가로 마진이 0
- mx-auto : 수평 중앙 정렬, 가로 가운데 정렬
- my-auto : 수직 중앙 정렬, 세로 가운데 정렬

## 실습해보기

## 2. color

## 3. text

## 4. position / display

## 5. components

- bootstrap의 다양한 UI요소를 활용할 수 있음
- button : 클릭했을 때 어떤 동작이 일어나도록 하는 요소
- Dropdown : 옵션 메뉴를 만들 수 있음

## 6. form

- form-control 클래스를 사용해 input 및 form 태그를 스타일링할 수 있음

## 7. nav bar

- 네비게이션 바를 제작할 수 있음

## 8. 캐러셀

- 콘텐츠를 순환시키기 위한 슬라이드 쇼

## 9. 모달창 (중요!)

- 사용자와 상호작용하기 위해서 팝업창을 반환하는 버튼
- **data-bs-toggle과 id과 연결**
- 주의 : 다른 요소로부터 방해받지 않도록 모달을 중첩해서 놓지마라! body랑 같은 레벨(탑레벨)로 배치하기.

## 10. flexbox

## 11. grid card

- 반응형 웹 : 화면 크기에 따라 배치가 달라짐
- 자동 구현되어있음
- 예 > 네이버 모바일 버전 [https://m.naver.com](https://m.naver.com)

## 그리드 시스템(중요)

- 반응형 웹을 만드는 시스템
- 요소들의 디자인과 배치에 도움을 주는 시스템
- **기본 요소**
    - column : 실제 컨텐츠를 포함하는 부분
    - gutter : 컬럼과 컬럼간의 사이 공간(사이 간격)
    - container : column을 담고있는 공간
- **반드시 기억해야 할 2가지(중요)**
    1. 12개의 column
    2. 6개의 grid breakpoints
    

## Grid system breakpoints

- breakpoint에 따라 화면 크기별로 화면 배치를 변경할 수 있다.
- **범위 6개**

## nesting

## responsive web 중요