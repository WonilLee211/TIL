# 목차

- web이란
    - 웹사이트 구성요소
    - 웹 표준과 크로스 브라우징
    - 개발환경 설정
- HTML
    - HTML 기본구조
    - HTML 문서 구조화
- CSS
    - CSS Selectors
    - CSS 단위
    - Selectors 심화
    - box model
    - display
    - position
    

---

## 1. 웹의 구성요소

- 웹사이트 : 브라우저를 통해서 접속하는 웹페이지들의 모음
- 웹페이지는 글, 그림, 동영상 등 여러가지 정보를 담고 있으며, 마우스로 클릭하면 다른 웹페이지로 이동하는 링크가 담겨있음
    - 링크를 통해 여러 웹페이지를 연결한 것을 웹사이트라고 함.

### 1.1 HTML : 구조

### 1.2 CSS : 표현

### 1.3 Javascript  : 동작

## 2. 웹사이트와 브라우저

- 웹사이트는 브라우저를 통해 동작

### 브라우저

- 파일들을 실행프로그램이 있어야 열 수 있듯, HTML 문저를 열 수 있는 것을 브라우저라 한다.

### 웹표준

- 웹에서 표준적으로 사용되는 기술이나 규칙
- 크로스 브라우징 : 웹 페이지가 동일하게 보이도록 함
- 팀 버스너리나 WHATWG와 같은 단체들이 웹 표준을 만든다
- 현재 대세는 HTML5

### Can i use?

- 브라우저별 호환성 체크하는 사이트
- 빨간색은 못쓰고 초록색은 가능.

---

# HTML

- Hyper Text Markup Language
- 웹 페이지를 작성(구조화)하기 위한 언어
- 파일 형식 : `.html`

### Hyper text

- 하이퍼링크를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트

### Markup Language

- 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어
    - 대표적인 예 - HTML, Markdown

## 1. HTML 스타일 가이드

- **indentation**
- 2칸으로 들여쓰기

```html
<body>
  <h1> 웹문서 </h1>
  <ul>
    <li>HTML</li>
    <li>CSS</li>
  </ul>
</body>
```

## 2. HTML 기본 구조

- html : 문서의 최상위(root) 요소
- head : 문서 메타데이터 요소
    - 문서 제목, 인코딩, 스타일, 외부 파일 로딩 등
    - 일반적으로 브라우저에 나타나지 않는 내용
- body : 문서 본문 요소
    - 실제 화면 구성과 관련된 내용

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Document</title>
</head>
<body>

</body>
</html>
```

### 2.1 head 예시

- `<title>` : 브라우저 상단 타이틀
- `<meta>` : 문서 레벨 메타데이터 요소
- `<link>` : 외부 리소스 연결 요소 ( CSS, favicon)
- `<script>` : 스크립트 요소(Javascript 파일/코드)
- `<style>` : CSS 직접 작성

```html
<head>
  <title>HTML</title>
  <meta charset="UTP-8">
  <link href="style.css" rel="stypesheet">
  <scrip src="javascript.js"></script>
  <style>
    p {
      color : black;
    }
  </style>
</head>
```

### 2.2 요소 (element)

- `<h1> contents </h1>` : 태그와 내용으로 구성됨
- HTML 요소는 시작 태그와 종료 태그 그리고 태그 사이에 위치한 내용으로 구성
    - 요소는 태그로 컨텐츠를 감싸는 것으로 그 정보의 성격과 의미를 정의
    - 내용이 없는 태그들도 존재(닫는 태그가 없음)
        - br, hr, img, input, link, meta
- 요소는 중첩(nested)될 수 있음
    - 요소의 중첩을 통해 하나의 문서를 구조화
    - **여는 태그와 닫는 태그의 쌍을 잘 확인해야 함**
        - 오류를 반환하는 것이 아닌 그냥 레이아웃을 깨진 상태로 출력되기 떄문에, 디버깅이 힘들어질 수 있음

### 2.3 속성(attribute)

- `<a href="https://google.com"></a>`
- href : 속성값으로 이동한다는 속성명
- “https://google.com” : 속성값
- 주의 ! 공백 X , 쌍따옴표 사용
- 속성을 통해 태그의 부가적인 정보를 설정할 수 있음
- 요소는 속성을 가질 수 있으며, 경로나 크기와 같은 추가적인 정보 제공
- 요소의 시작 태그에 작성하며 보통 이름과 값이 하나의 쌍으로 존재
- 태그와 상관없이 사용가능한 속성(HTML Global Attribute)들도 있음

### HTML Global Attribute

- 모든 HTML 요소가 공통으로 사용할 수 있는 대표적인 속성(몇몇 요소에는 아무 효과가 없을 수 있음)
    - id : 문서 전체에서 유일한 고유 식별자 지정
    - class : 공백으로 구분된 해당 요소의 클래스 목록(CSS, js에서 요소를 선택하거나 접근)
    - data-* : 페이지 개인 사용자 정의 데이터를 저장하기 위해 사용
    - style : inline 스타일
    - title : 요소에 대한 추가 정보 지정
    - tabindex : 요소의 탭 순서
    
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>Document</title>
    </head>
    <body>
      <!--이것은 주석입니다. -->
      <h1>나의 첫번째 HTML</h1>
      <p>이것은 본문입니다.</p>
      <span>이것은 인라인 요소</span>
      <a href="https://www.naver.com">네이버로 이동 !!</a>
    </body>
    </html>
    ```
    

### 2.4 시맨틱 태그

- HTML5에서 의미론적 요소를 담은 태그의 등장
    - 기존 영역을 의미하는 div 태그를 대체하여 사용
- 대표적인 태그 목록
    - header : 문서 전체나 섹션의 헤더
    - nav : 네비게이션
    - aside  : 사이드에 위치한 공간 메인 콘텐츠와 관련성이 적은 콘텐츠
    - section : 문서의 일반적인 구분, 컨텐츠의 그룹을 표현
    - article : 문서. 페이지, 사이트 안에서 독립적으로 구분되는 영역
    - footer :  문서 전체나 섹션의 푸터(마지막부분)
- Non semantic 요소는 div, span등이 있으며 h1, table 태그들도  시맨틱 태그로 볼 수 있음
- 개발자 및 사용자 뿐만 아니라 검색 엔진 등에 의미 있는 정보의 그룹을 태그로 표현

### 랜더링

- 웹사이트 코드를 사용자가 보게 되는 웹 사이트로 바꾸는 과정

### DOM(Document Object Model) 트리

- 텍스트 파일인 HTML문서를 브라우저에서 렌터링하기 위한 구조
    - HTML문서에 대한 모델 구성
    - HTML 문서 내의 각 요소에 접근/ 수정에 필요한 프로퍼티와 메서드 제공
    
    ```html
    <body>
      <h1> 웹 문서 </h1>
      <ul>
        <li>HTML</li>
        <li>CSS</li>
      </ul>
    </body>
    
    # 구조를 잘 기억하기 !
    ```
    

## 3. HTML 문서 구조화

### 인라인/ 블록 요소

- HTML 요소는 크게 인라인/블럭 요소로 나눔
- 인라인 요소는 글자처럼 취급
- 블록요소는 한 줄 모두 사용

### 3.1 텍스트 요소

- `<a></a>` : href 속성을 활용하여 다른url로 연결하는 하이버링크 생성
- `<b></b>`/`<strong></strong>`(시맨틱) : 굵은 글씨 요소, 중요한 강조하고자 하는 요소
- `<i></i>` / `<em></em>`(시맨틱): 기울임 글씨 요소 / 중요한 강조하고자 하는 요소
- `<br>` : 텍스트 내에 줄 바꿈 생성
- `<img>` : src 속성을 활용하여 이미지 표현
- `<span></span>` : 의미없는 **인라인** 컨테이너

### 3.2 그룹 컨텐츠

- `<p></p>` : 하나의 문단
- `<hr>` : 문단 레벨 요소에서의 주제의 분리를 의미
- `<ol></ol>`/`<ul></ul>` : 순서가 있는 리스트/ 순서가 없는 리스트
- `<pre></pre>` : HTML에 작성한 내용을 그대로 표현. 보통 고정폭 글꼴이 사용되고 공백 문자를 유지
- `<blockquote></blockquote>` : 텍스트가 긴 인용문. 주로 들여쓰기한 것처럼 표현됨
- `<div></div>` : 의미없는 **블록** 레벨 컨테이너
    - vs <span> 차이 이해하기
    

### 3.3 form

- <form>은 정보를 서버에 제출하기 위해 사용하는 태그
- <form 기본 속성>
    - action : form을 처리할 서버의 url(데이터를 보낼 곳)
    - method : form을 제출할 때 사용할 HTTP 메서드(GET or POST)
    - enctype : method가 post인 경우 데이터의 유형
        - application/x-www-form-urlencoded : 기본값
        - multipart/form-data : 파일 전송시 (input type이 file인 경우)

```html
<form action="/search" method="GET">
</form>
```

- 크롬 개발자도구 열기
    
    
- `F12`

### 3.4 input

- 다양한 타입을 가지는 입력 데이터 유형과 위젯이 제공됨
- <input> 대표적인 속성
    - name : form control에 적용되는 이름(이름/값 페어로 전송됨)
    - value : form control에 적용되는 값(이름/값 페어로 전송됨)
    - required, readonly, autofocus, autocomplete, disable 등
    
    ```html
    <form action="/search" method="GET">
      <input type="text" name="q">
    </form>
    
    # https://www.google.com/search?q=HTML
    ```
    

### 3.5 input label

- label을 클릭하여 input 자체의 초점을 맞추거나 활성화시킬 수 있음
    - 사용자는 선택할 수 있는 영역이 늘어나 웹/모바일 환경에서 편하게 사용 가능
    - label과 input입력의 관계가 시각적 뿐만 아니라 화면 리더기에서도 label을 읽어 쉽게 내용을 확인할 수 있도록 함
- **`<input>에 id속성을, <label>에는 for 속성을 활용하여** 상호 연관`을 시킴
- 직접 쳐보기

### input 유형 - 일반

- 입력을 받기 위하여 제공됨
- 타입별로 HTML 기본 검증 및 추가 속성을 활용
    - text : 일반 텍스트 입력
    - password : 입력 시 값이 보이지 않고 문자를 특수기호로 표현
    - email : 이메일 형식이 아닌 경우 form 제출 불가
    - number : min, max, step 속성을 활용하여 숫자 범위 설정 가능
    - file : accept 속성을 활용하여 파일 타입 지정 가능

### input 유형 - 항목 중 선택

- 일반적으로 label 태그와 함께 사용하여 선택 항목을 작성함
- 동일 항목에 대해서는 name을 지정하고 선택된 항목에 대한 값 지정해야 함
    - checkbox : 다중선택
    - radio : 단일 선택
    

### input 유형 - 기타

- 다양한 종류의 input을 위한 picker를 제공
    - color : color picker
    - date : date picker
- hidden input을 활용하여 사용자 입력을 받지 않고 서버에 전송되어야 하는 값을 설정
    - hidden : 사용자에게 보이지 않는 input

### input 유형 - 종합

- <input>요소의 동작은 type에 따라 달라지므로, 각각의 내용을 숙지할 것
- `developer.mozilla.org/ko/docs/Web/HTML/Element/input`

- HTML : 태그에 속성을 넣어서 구성을 잡으면 된다.
- 다양한 태그마다 속성이 다르다.

### 마크업 해보기

- 구조
    1. header
    2. section
    3. footer
    
    실습해보기
