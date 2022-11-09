# Event

- 프로그래밍하고 있는 시스템에서 발생하는 사건 혹은 발생인데, 우리가 원한다면 그것들을 어떠한 방식으로 응답할 수 있도록 시스템이 말해주는 것
- **예시**
    - 사용자가 웹 페이지의 버튼을 클릭한다면 우리는 클릭이라는 사건에 대한 결과를 응답받기 원할 수 있음
- 클릭 말고도 웹에서는 각양각색의 Event가 존재
    - 키보드 키 입력, 브라우저 닫기, 데이터 제출, 텍스트 복사 등

# Event Intro

# 1. Event object

- 네트워크 활동이나 사용자와의 상호작용 같은 사건의 발생을 알리기 위한 객체
- Event 발생
    - 마우스를 클릭하거나 키보드를 누르는 등 사용자 행동으로 발생할 수도 있고
    - 특정 메서드를 호출하여 프로그래밍적으로도 만들어 낼 수 있음
- DOM 요소는 Event를 받고(”수신”)
- 받은 Event를 “처리”할 수 있음
    - event 처리는 주로 `addEventListener()` 라는 Event 처리기(Event Handler)를 사용해 다양한 html 요소에 부착하게 됨.

## 1.1 Event handler - `addEventListener()`

- `대상`에 `특정 event`가 발생하면, `할 일`을 등록하자
    - `eventTarget.addEventListener(type, listener)`
- `eventTarget.addEventListener(type, listener[, options])`
    - 지정한 event가 대상에 전달될 때마다 호출할 함수를 설정
    - event를 지원하는 **모든 객체(Element, Document, window 등**)를 대상(EventTarget)으로 지정 가능
    - **type**
        - 반응할  Event 유형을나타내는 대소문자 구분 문자열
        - 대표 이벤트
            - input, click, submit …
            - 다양한 이벤트 확인(https://deceloper.mozilla.org/en-US/docs/Web/Events)
    - **listener**
        - 지정된 타입의 event를 수신할 객체
        - JavaScript function 객체(콜백함수)여야 함
        - `콜백 함수는 발생한 event의 데이터를 가진 event 기반 객체를 유일한 매개 변수로 받음`
    

### 1.1.1 사용법

- 버튼을 클릭하면, 특정 변수 값 변경하기

```jsx
<body>
  <button id="btn">버튼</button>
  <p id="counter">0</p>
  
  <script>
    const btn = document.querySelector('#btn')
    let = countNum = 0
    // 이벤트 핸들러 작성
    btn.addEventListener('click', function (event) {
      // console.log(event)
      const pTag = document.querySelector('#counter')
      countNum += 1

      pTag.innerText = countNum

    })
  </script>
</body>
```

- input에 입력하면 입력 값을 실시간으로 출력하기

```jsx
<body>
  <input type="text" id="text-input">
  <p></p>
  <script>
    // 1. input 선택
    const inputTag = document.querySelector('#text-input')

    // 2. 이벤트 핸들러 부착
    inputTag.addEventListener('input', function (event) {
      // console.log(event)
      const pTag = document.querySelector('p')
      pTag.innerText = event.target.value
    })
  </script>
</body>
```

- input에 입력하면, 입력값을 실시간으로 출력
- 버튼을 클릭하면, 출력된 값의 클래스를 토글하기

```jsx
<!DOCTYPE html>
<html lang="en">
<head>
...
  <style>
    .blue {
      color: blue;
    }
  </style>
</head>
<body>
  <h1></h1>
  <button id="btn">클릭</button>
  <input type="text">

  <script>
   const btnTag = document.querySelector('#btn')
   btnTag.addEventListener('click', function (event) {
    const h1Tag = document.querySelector('h1')
    h1Tag.classList.toggle('blue')
   })

   const inputTag = document.querySelector('input')
   inputTag.addEventListener('input', function (event) {
    const h1Tag = document.querySelector('h1')
    h1Tag.innerText = event.target.value
   })

  </script>
</body>
</html>
```

## addEventListener 정리

- “~하면 ~한다.”
    - “클릭하면, 경고창을 띄운다.”
    - “특정 Event가 발생하면, 할 일(callback 함수을 등록한다)”

# Event 취소(중요)

## 1. `event.preventFefault()`

- 현재 event의 기본 동작을 중단
- HTML 요소의 기본 동작을 작동하지 않게 막음
- HTML 요소의 기본 동작 예시
    - a태그 : 클릭 시 특정 주소로 이동(화면전환)
    - form 태크 : form 데이터 전송

### 사용법

- 웹 페이지 내용을 복사하지 못하도록 하기

```jsx
const h1Tag = document.querySelector('h1')
    h1Tag.addEventListener('copy', function (event) {
      event.preventDefault()
      // window.alert('복사할 수 없습니다.')
      alert('복사할 수 없습니다.')
    })
```

# event 종합

### **button을 클릭하면, 랜덤 번호 6개를 출력하기**

```jsx
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>프로젝트</title>
  <style>
    /* 스타일은 수정하지 않습니다. */
    .ball {
      width: 10rem;
      height: 10rem;
      margin: .5rem;
      border-radius: 50%;
      text-align: center;
      line-height: 10rem;
      font-size: xx-large;
      font-weight: bold;
      color: white;
    }
    .ball-container {
      display: flex;
    }
  </style>
</head>
<body>
  <h1>로또 추천 번호</h1>
  <button id="lotto-btn">행운 번호 받기</button>
  <div id="result"></div>

  <!-- lodash 라이브러리 CDN : 난수 생성을 위한 라이브러리를 사용하기 위함 -->
  <script src="https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js"></script>
  <script>
    const btn = document.querySelector('#lotto-btn')
    btn.addEventListener('click', function (event) {
      // 1부터 45 까지 랜덤한 수의 배열을 만들고 div태그에 넣어야 함
      // 공이 들어갈 컨테이너 생성
      const ballContainer = document.createElement('div')
      ballContainer.classList.add('ball-container')
      
      // 랜덤한 숫자 6개를 만들기
      const numbers = _.sampleSize(_.range(1, 46), 6)
      console.log(numbers)

      // 공만들기
      numbers.forEach((number) => {
        const ball = document.createElement('div')
        ball.innerText = number
        ball.classList.add('ball')
        ball.style.backgroundColor = 'crimson'
        ballContainer.appendChild(ball)
      })
      // 공 컨테이너는 결과 영역의 자식으로 넣기
      const resultDiv = document.querySelector('#result')
      resultDiv.appendChild(ballContainer)
    })

  </script>
</body>
</html>
```

- lodash
- - 모듈성, 성능 및 추가 기능을 제공하는 JavaScript 유틸리티 라이브러리
- - array, object 등 자료구조를 다룰 때 사용하는 유용하고 간편한 유틸리티 함수들을 제공
- - 함수 예시 :  reverse, sortBy, range, random, …
    
    
- https://lodash.com

### CREATE, READ 기능을 충족하는 Todo app 만들기

```jsx
...
<body>
  <form action="#">
    <input type="text" class="inputData">
    <input type="submit" value="Add">
  </form>
  <ul></ul>

  <script>
    const formTag = document.querySelector('form')

    const addTodo = function (event) {
      event.preventDefault()

      const inputTag = document.querySelector('.inputData')
      const data = inputTag.value

      if (data.trim()) {
        const liTag = document.createElement('li')
        liTag.innerText = data

        ulTag = document.querySelector('ul')
        ulTag.appendChild(liTag)
        
      }else {
        alert('내용을 입력하세요.')
      }
      event.target.reset()
    }
    formTag.addEventListener('submit', addTodo)

  </script>
</body>
</html>
```