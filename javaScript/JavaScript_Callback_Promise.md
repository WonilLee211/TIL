# Callback과 Promise

### 비동기 처리의 단점

- 비동기 처리의 핵심은 WEB API로 들어오는 순서가 아니라 `작업이 완료되는 순서에 따라 처리`
- 그런데 이는 개발자입장에서 코드의 실행 순서가 불명확하다는 단점
- `실행결과는 예상하면서 코들르작성할 수 없게 함`
- 콜백함수를 사용해서 해결 !

## Callback 함수

- 특별한 함수가 아님
- `다른 함수의 인자로 전달되는 함수`
- 비동기에만 사용되는 함수가아니며 동기, 비동기 상관없이 사용 가능
- 시간이 걸리는 비동기 작업이 완료된 후 실행할 작업을 명시하는 데 사용되는 콜백 함수를 `비동기 콜백`이라 부름

## 1. 콜백 함수를 사용하는 이유

- 명시적인 호출이 아닌 특정한 조건 혹은 행동에 의해 호출되도록 작성할 수 있음
- “요청이 들어오면”, “이벤트가 발생하면”, “데이터가 드러오면” 등의 조건으로 이후 로직을 제어할 수 있음
- `비동기 처리를 순차적으로 동작할 수 있게 함`

## 2. 콜백 지옥(Callback Hell)

- 콜백함수는 연쇄적으로 발생하는 비동기 작업을 순차적으로 동작할 수 있게 함
- 보통 어떤 기능의 실행 결과를 받아서 다른  기능을 수행하기 위해 많이 사용
- 이 과정을 반복하면 코드가 깊어지는 단점
- 피라미드 같이 생겨서 **Pyramid of doom**이라고도 함

### 정리

- 콜백 함수는 비동기 작업을 순차적으로 실행할 수 있게 하는 반드시 필요한 로직
- 콜백 지옥은 반드시 발생하는 문제
    - 코드 가독성이 낮아지고
    - 유지 보수가 어려움

# 프로미스(Promise)

- callback hell 문제를 해결하기 위해 등장한 비동기 처리를 위한 객체
- “작업이 끝나면 실행시켜줄게”라는 약속
- `비동기 작업의 완료 또는 실패를 나타내는 객체`
- promise 기반의 클라이언트가 바로 이전에 사용한 `Axios` 라이브러리
    - promise based HTTP client for the browser and node.js
    - `then()` : 성공에 대한 약속
    - `catch()` : 실패에 대한 악속

1. then(callback)
    - 요청한 작업이 성공하면 callback 실행
    - callback은 이전 작업의 성공 결과를 인자로 전달 받음
2. catch(callback)
    - then()이 하나라도 실패하면 callback 실행
    - callback은 이전 작업의 실패 객체를 인자로 전달받음

- then과 catch 무도 항상 promise 객체를 반환
- 즉, 계속해서 chaining을 할 수 있음
- `axios로 처리한 비동기 로직이 항상 promise 객체를 반환`
- 그래서 then을 계속 이어가면서 작성할 수 있던 것
    - `axios.get('요청할 URL').then(...).then(...).catch(...)`

## 1. Promise가 보장하는 것(VS 비동기 콜백)

- 비동기 콜백 작성 스타일과 달리 promise가 보장하는 특징
1. callbaack 함수는 JavaScript의 Event Loop가 현재 실행 중인 Call stack을 완료하기 이전에는 절대 호출되지 않음
    - promise callback 함수는 Event Queue에 배치되는 엄격한 순서를 호출됨
2. 비동기 작업이 성공하거나 실패한 뒤에 .then()메서드를 이용하여 추가한 경우에도 1번과 똑같이 동작
3. .then()을 여러 번 사용하여 여러 개의 callback함수를 추가할 수 있음(chaining)
    - 각각의 callback은 주어진 순서대로 하나하나 실행하게 됨
    - chaining은 promise의 가장 뛰어난 장점

```jsx
<body>
  <button>야옹아 이리온</button>
  <button id="dog-btn">멍멍아 이리온</button>

  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script>

    const catImageSearchURL = 'https://api.thecatapi.com/v1/images/search'
    const btn = document.querySelector('button')
    
    const dogImageSearchURL = 'https://dog.ceo/api/breeds/imgage/random'
    const dogBtn = document.querySelector('#dog-btn')

    dogBtn.addEventListener('click', function (event) {
      axios({
        method: 'get',
        url: dogImageSearchURL,
      })
        .then(response => {
          console.log(response.data.message)
          const imgSrc = response.data.message
          return imgSrc
        })
        .then((imgSrc) => {
          const imgTag = document.createElement('img')
          imgTag.setAttribute('src', imgSrc)
          document.body.appendChild(imgTag)
        })
        .catch((error) => {
          console.log(error)
        })
    })

    btn.addEventListener('click', function () {
      axios({
        method: 'get',
        url: catImageSearchURL,
      })
        .then()
        .then()
        .catch()

      axios.get(catImageSearchURL)
        .then((response) => {
          imgElem = document.createElement('img')
          imgElem.setAttribute('src', response.data[0].url)
          document.body.appendChild(imgElem)
        })
        .catch((error) => { 
          console.log('실패했다옹')
        })
        console.log('야옹야옹') 
    })
  </script>
</body>
```