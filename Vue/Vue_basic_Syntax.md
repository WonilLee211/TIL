# Basic of Syntax

## 1. template Syntax

- Vue2 guide > template Syntax 참고
- `렌더링된 DOM`을 기본 Vue instance의 data `선언적으로 바인딩`할 수 있는 `HTML 기반 template syntax를 사용`
- 3가지 출력방식1
    1. 렌더링된 DOM - 브라우저에 의해 보기 좋게 그려질 HTML 코드
    2. HTML 기반 template syntax - HTML 코드에 직접 작성할 수 있는 문법 제공
    3. 선언적으로 바인딩 - Vue instance와 DOM을 연결

## 2. Template Interpolation

- 가장 기본적인 바인딩(연결) 방법
- 중괄호 2개로 표기
- DTL과 동일한 형태로 작성
- Template interpolation 방법은 HTML을 일반 텍스트로 표현

```jsx
<!-- 1. Text interpolation -->
  <div id="app">
    <p>메시지: {{ msg }}</p>   
    <p>HTML 메시지 : {{ rawHTML }}</p>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
  <script>
    // 1. Text interpolation
    const app = new Vue({
      el: '#app',
      data: {
        msg: 'Text interpolation',
        rawHTML: '<span style="color:red"> 빨간 글씨</span>'
      }
    })
  </script>

// 출력 - 메시지 : <span style="color:red"> 빨간 글씨</span>
```

## 3. RAW HTML

- `v-html` directive을 사용하여 data와 바인딩
- directive-HTML 기반 template syntax
- HTML의 기본 속성이아닌 Vue가 제공하는 특수 속성의 값으로 data를 작성

```
<!-- 1. Text interpolation -->
  <div id="app">
    <p>HTML 메시지 : <span v-html="rawHTML"></span></p>
  </div>
...
  <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
  <script>
    // 1. Text interpolation
    const app = new Vue({
      el: '#app',
      data: {
        rawHTML: '<span style="color:red"> 빨간 글씨</span>'
      }
    })

// HTML 메시지 : 빨간 글씨
```

- [참고] JS 표현식
- - 표현식 형태로 작성 가능

```jsx
<!-- 1. Text interpolation -->
  <div id="app">
    <p>{{ msg.split('').reverse().join('') }}</p>
  </div>
...
  <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
  <script>
    // 1. Text interpolation
    const app = new Vue({
      el: '#app',
      data: {
        msg: 'Text interpolation',
      }
    })
```