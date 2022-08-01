> MDN을 바탕으로 공부하기

# CSS(Cascading Style Sheets)

- 스타일을 지정하기 위한 언어
- 선택하고 스타일을 지정한다.
- 선택자를 통해 스타일을 지정할 HTML 요소를 선택
- 중괄호 안에서 속성과 값, 하나의 쌍으로 이루어진 선언을 진행

## 1. CSS 구문

```css
h1{
  color: blue;
  font-size: 15px;
}
```

- 용어 정리
    - `h1` : 선택자(selector)
    - `color: blue;` : 선언(Declaration)
    - `font-size` : 속성(property)
    - `15px` : 값(value)

## 2. CSS 정의 방법

1. 인라인(inline)
2. 내부참조(embedding) - <style>
3. 외부 참조(link file) - 분리된 CSS 파일

### 인라인(쓰지말기 - 협업 시 문제 발생)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1 style="color:blue; font-size: 100px;">Hello</h1>
</body>
</html>
```

### 내부 참조

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
      h1 {
        color: blue;
        font-size: 100px;
      }
    </style>
</head>
<body>
    <h1>Hello</h1>
</body>
</html>
```

### 외부 참조

- 외부 css파일을 <head>내  <link>를 통해 불러오기

```css
# mystyle.css
P{
    color: pink;
    font-size: 40px;
}
```

```html
# html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="mystyle.css">
</head>
<body>
    <p>나는야 p tag </p>
    <p>나는야 p tag </p>
    <p>나는야 p tag </p>
    <p>나는야 p tag </p>
    <p>나는야 p tag </p>
</body>
</html>
```

- 주로 활용하는 속성 위주로 기억하자 `30~40개로 다 이루어짐`
    
    
- `Global CSS Property Usage`

## 3. CSS with 개발자 도구

- Styles : 해당 요소에 선언된 모든 CSS
- computed : 해당 요소에 최종 계산된 CSS

---

# CSS Selectors

## 1. 선택자(selector) 유형

### 기본 선택자

- 전체 선택자, 요소 선택자
- 클래스 선택자, 아이디 선택자, 속성 선택자

### 결합자(combinators)

- 자손 결합자, 자식 결합자
- 일반 형제 결합자, 인접 형제 결합자

### 의사 클래스/요소(Pseudo Class)

- 링크, 동적 의사 클래스
- 구조적 의사 클래스, 기타 의사 클래스, 의사 엘리먼트 속성, 속성 선택자

- 실습해보기 ~99p

## 2. <mark>CSS 선택자 정리</mark>

### 요소 선택자

- HTML 태그를 직접 선택

### 클래스 선택자

- 마침표 문자로 시작하여 해당 클래스가 적용된 항목을 선택

### 아이디(id) 선택자

- #문자로 시작하여, 해당 아이디가 적용된 항목을 선택
- 일반적으로 하나의 문서에 1번만 사용
- 여러 번 사용해도 동작하지만, 단일 id를 사용하는 것을 권장

## 3. <mark> CSS 적용 우선순위(cascading order)</mark>

### CSS 우선순위를 아래와 같이 그룹을 지어볼 수 있다.

1. 중요도(Importance) - 사용 시 주의
    - !important
2. 우선순위(Specificity)
    - 범위가 좁을수록 강하다
    - 동등한 크기이면 아래있을수록 강하다(cascading)
    - 인라인 > id > class, 속성, pseudo-class > 요소, prseudo-element
3. CSS 파일 로딩 순서

** 외우지말고 실습으로 체득하기**

- 실습해보기 103p
    
    

## 4. CSS 상속

- CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속한다.
    - 속성 중에는 상속이 안되는 것도 있음
    - **상속되는 것 : text관련 요소(font, color, text-align), opacity, visibility 등**
    - 상속되지 않는 것 : box model 관련 요소(width, height, margin, padding, border, box-sizing, display), position 관련 요소(position, top/right/bottom/left, z-index) 등
    
    ```css
    <style>
      p {
        /* 상속됨 */
        color: red;
        /*상속 안됨*/
        border: 3px solid black;
      }
      span { 
      {
    </style>
    ```
    
    ```html
    <body>
      <p> 안녕하세요! <span>테스트</span>입니다.</p>
    </body>
    
     /* 결과 보기*/
    ```
    

---

# CSS 기본 스타일

## 1. <mark>크기 단위</mark>

### 1.1 px(픽셀)

- 모니터 해상도의 한화소인 픽셀 기준
- 픽셀의 크기는 변하지 않기 때문에 고정적인 단위

### 1.2 %

- 백분율 단위
- 가변적인 레이아웃에서 자주 사용

### 1.3 em

- (바로 위, 부모 요소에 대한) 상속의 영향을 받음
- (배수 단위, 요소에 지정된 사이즈에 상대적인 사이즈를 가짐

### 1.4 rem(root em)

- (바로 위, 부모 요소에 대한) 상속의 영향을 받지 않음
- 최상위 요소(HTML, 브라우저?16px?)의 사이즈를 기준으로 배수 단위를 가짐
- 현업에서 많이쓰는 단위들

- 실습해보기

### 1.5 viewport (화면 크기 기준)

- 웹페이지를 방문한 유저에게 바로 보이게 되는 웹 컨텐츠의 영역(디바이스 영역)
- 디바이스의 viewpoint를 기준으로 상대적인 사이즈가 결정됨
- vw, vh, vmin, vmax

## 2. 색상단위

### 색상 키워드

- 대소문자 구분하지 않음
- 특정 색을 직접 글자로 나타냄

### RGB 색상

- 16진수 표기법 혹은 함수형 표기법 사용
- `# + 16진수 표기법`
- `rgb() 함수형 표기법`

### HSL 색상

- 색상, 채도 ,명도를 통해 특정 색을 표현
- `hsla` : alpha (투명도)

---

# selectors 심화

## 1.<mark>결합자(combinators)</mark>

### 1.1 자손 결합자(공백)

- selector A 하위의 모든 selector  B 요소

### 1.2 자식 결합자( > )

- selector A 바로 아래의 selectorB 요소

### 1.3 일반 형제 결합자 ( ~)

- selectorA 형제 요소 중 뒤에 위치하는 selectorB 요소를 모두 선택

### 1.4 인접 형제 결합자( +)

- seletorA의 형제 요소 중 바로 뒤에 위치하는 selectorB 요소를 선택

---

# CSS Box model

## 1. <mark>Box model</mark>

- **모든 HTML 요소는 box 형태로 되어있음**
- 하나의 box-model의 구성
    1. margin : **테두리 바깥의** 외부 여백 배경색을 지정할 수 없다.
    2. border : **테두리 영역**
    3. padding : **테두리 안쪽**의 내부 여백/ 요소에 적용된 배경색/ 이미지는 padding 까지 적용
    4. content : **글이나 이미지** 등 요소의 실제 내용
    

## 2. CSS 원칙

- 모든 요소는 네모(박스 모델)
- **위에서 아래, 왼쪽에서 오른쪽으로 쌓임**

## 3.<mark> box model  구성</mark>

### 1. margin

- `.margin{}`
- `.margin-padding{}`
- `.border{}`
- `margin-1{}` 상하좌우 동일
- `margin-2{}` 상하 동일, 좌우 동일
- `margin-3{}` 상, 좌우, 하
- `margin-4{}`  시계방향 : 상 우 하 좌

- 실습 136p
    
    

### <mark>box-sizing</mark>

- 기본적으로 모든 요소의 **box-sizing은 content-box**
    - padding을 제외한 순수 컨탠츠 영역만을 box로 지정
- 일반적으로 우리가 바라는 크기과 실제 박스 크기와 달라지게 됨.
    - 그 경우 box-sizing을  border-box로 설정 `box-sizing: border-box;`
    

---

# CSS Display

## CSS원칙 2

- display에 따라 크기와 배치가 달라진다.

## 대표적으로 활용되는 display

### display: block

- 줄 바꿈이 일어나는 요소
- 화면 크기 전체의 가로 폭을 차지
- 블록 레벨 전체의 가로 폭을 차지

### display: inline

- 줄 바꿈이 일어나지 않는 행의 일부 요소
- content 너비만큼 가로 폭을 차지한다
- width, height, margin-top, margin-bottom을 지정할 수 없다.
- 상하 여백은 line-height로 지정

### 블록 레벨 요소와 인라인 레벨 요소(구분하기)

- 대표적 블록 레벨 요소
    - div / ul, ol, li / p / hr / form 등
- 대표적인 인라인 레벨 요소
    - span/ a / img / input / label/ b, em, i , strong 등
    

### block

- 기본 너비는 가질 수 있는 너비의 100%
- 너비를 가질 수 없다면 자동으로 부여되는 margin

### inline

- inline의 기본 너비는 컨텐츠 영역만큼

### <mark>속성에 따른 수평 정렬</mark>

- 우측에 여백
    - `margin-right: auto;`
- 좌측에 여백
    - `margin-left: auto;`
- 좌우 동일
    
    ```html
    margin-right: auto;
    margin-left: auto;
    ```
    
- `text-align: left;`
- `text-align: right`
- `text-align: center;`

## display

- inline-block
    - block과 inline 레벨요소의 특징을 모두 가짐
    - inline처럼 한 줄에 표시할 수 있고, block처럼 width, height, margin 속성을 모두 지정할 수 있음
- <mark>display: none</mark> visibility와 hidden과 차이
    - 해당 요소를 화면에 표시하지 않고, 공간조차 부여하지 않음
    - 이와 비슷한 visibility: hidden은 해당 요소가 공간은 차지하나 화면에 표시만 하지 않는다
- 이 외 다양한 display 속성 : `https://developer.mozilla.org/ko/docs/Web/CSS/display`
- 실습 155p

---

# CSS position

- 문서 상에서 요소의 위치를 지정
- static : 모든 태그의 기본 값(기준 위치)
    - 일반적인 요소의 배치 순서에 따름(좌측 상단)
    - 부모 요소 내에서 배치될 때는 부모 요소의 위치를 기준으로 배치됨
- 아래는 좌표 프로퍼티(top, bottom, left, right)를 사용하여 이동 가능
    1. relative
    2. absolute
    3. fixed (광고에 사용)
    4. sticky
    

## 1. 좌표 프로터피를 사용한 이동

### 1.1 relative : 상대 위치

- 자기 자신의 static 위치를 기준으로 이동(normal flow 유지)
- 레이아웃에서 요소가 차지하는 공간은 static일 때와 같음(normal position 대비 offset)

### 1.2 absolute : 절대 위치

- 요소를 일반적인 문저 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음(normal flow에서 벗어남)
- static이 아닌 가장 가까이 있는 부모/조상 요소를 기준으로 이동(없는 경우 브라우저 화면 기준으로 이동)

### 1.3 fixed : 고정 위치

- 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간이 차지하지 않음(normal flow에서 벗어남)
- 부모 요소와 관계없이 viewport를 기준으로 이동
    - 스크롤 시에도 항상 같은 곳에 위치함

### 1.4 sticky : 스크롤에 따라 static >> fixed로 변경

- 속성을 적용한 박스는 평소에 문서 안에서 `position:static 상태`와 같이 일반적인 흐름에 따르지만 스크롤 위치가 임계점에 이르면 `position: fixed`와 같이 박스를 화면에 고정할 수 있는 속성

## **position sticky**

- sticky :  스크롤에 따라 static >> fixed로 변경
- **MDN 문서 보기**

## CSS 원칙

### CSS원칙 1,2 : Normal flow

- 모든 요소는 네모(박스모델), 좌측 상단에 배치
- display에 따라 크기와 배치가 달라짐

### CSS 원칙 3

- position으로 위치 기준을 변경
    - relative : 본인의 원래 위치
    - absolute : 특정 부모의 위치
    - fixed : 화면의 위치
    - sticky : 기본적으로 static이나 스크롤 이동에 따라 fixed로 변경