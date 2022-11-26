# 동기와 비동기

# 동기(Synchronous)

- 모든 일을 `순서대로 하나씩` 처리하는 것
- 순서대로 처리한다 == 이전 작업이 끝나면 다음 작업을 시작한다
- 우리가 작성했던 python 코드가 모두 동기식

```jsx
print('첫번째 작업')
for i i range(10):
    print('두번째 작업')
    print(i)
print('세번째 작업')
```

- 요청과 응답을 동기식으로 처리한다면?
    - 요청을 보내고 응답이 올 때까지 기다렸다가 다음 로직을 처리

```jsx
<body>
  <button>버튼</button> 
  <script>
    const btn = document.querySelector('button')
    btn.addEventListener('click', () => {
      alert('you clicked me!')
      const pElem = document.createElement('p')
      pElem.innerText = 'p Element'
      document.body.appendChild(pElem)
  })
  </script>
</body>
```

# 비동기(Asynchronous)

- 작업을 시작한 후 `결과를 기다리지 않고` 다음 작업을 처리하는 것(병렬적 수행)
- 시간이 필요한 작업들은 보낸 뒤 응답을 빨리 오는 작업부터 처리
- 예시> Gmail에서 메일 전송을 누르면 목록 화면으로 전환되지만 실제로 메일을 보내는 작업은 병렬적으로 뒤에 처리됨

```jsx
function slowRequest(callBack) {
  console.log('1. 오래 걸리는 작업 시작 ...') // 3초를 기다리는 함수(오래 걸리는 작업)
  setTimeout(function () {  
    callBack()
  }, 3000)
}

function myCallBack() {
  console.log('2. 콜백함수 실행됨') // 가장 마지막에 출력됨
}

slowRequest(myCallBack)
console.log('3. 다른 작업 실행')

// 출력결과
// 1. 오래 걸리는 작업 시작
// 3. 다른 작업 실행
// 2. 콜백 함수 실행됨
```

## 1. 비동기를 사용해야 하는 이유

- **사용자 경험**
    - 예를 들어 아주 큰 데이터를 불러온 뒤 실행되는 앱이 있을 때
    - 동기로 처리한다면 데이터를 모두 불러온 뒤에야 앱의 실행 로직이 수행되므로
    - 사용자는 마치 앱이 멈춘 것과 같은 경험을 겪게 됨
    - 즉, 동기식 처리는 특정 로직이  실행되는 동안 다른 로직 실행을 차단하기 때문에 마치 프로그램이 응답하지 앟는 듯한 사용자 경험을 만들게 됨
    - `비동기로 처리한다면 먼저 처리되는 부분부터 보여줄 수 있으므로,`
    - 사용자 경험에 긍정적인 효과를 볼 수 있음
    - 이와 같은 이유로 많은 웹 기능은 비동기 로직을 사용해서 구현되어 있음

# JavaScript의 비동기 처리

## 1. single Thread 언어, JavaScript

- 응답이 먼저 오는 순서대로 처리하지 말고, 아예 여러 작업을 동시에 처리하면 되지 않을까?
- `JavaScript는 한 번에 하나의 일만 수행할 수 있는 Single Thread언어로` 동시에 여러 작업을 처리할 수 없음
- [참고] Thread란?
    
    
- -  작업을 처리할 때 실제로 작업을 수행하는 주체로, mult-thread라면 업무를 수행할 수 있는 주체가 여러 개라는 의미
- `즉, JavaScript는 하나의 작업을 요청한 순서대로 처리` 할 수 밖에 없다 !
- 어떻게 Single Thread인 JavaScript가 비동기 처리를 할 수 있을까?

## 2. JavaScript Runtime

- JavaScript자체는 Single Thread이므로 비동기 처리를 할 수 있도록 도와주는 환경이 필요함
- 특정 언어가 동작할 수 있는 환경을 런타임(Runtime)이라 함
- JavaScript에서 `비동기와 관련한 작업은 브라우저 또는 Node환경에서 처리`
- 이 중에서 브라우저 환경에서의 비동기 작업은 크게 아래의 요소들로 구성됨
    1. JavaScript Engine의 `Call back`
    2. `Web API`
    3. `Task Queue`
    4. `Event Loop`

## 3. 비동기 처리 동작 방식

- 브라우저 환경에서의 JavaScript의 비동기는 아래와 같이 처리
    1. 모든 작업은 Call stack(LIFO)으로 들어간 후 처리
    2. 오래 걸리는 작업이 Call Stack으로 들어오면 Web API로 보내서 처리하도록 한다
    3. Web API에서 처리가 끝난 작업들은 Task Queue(FIFO)에 순서대로 들어간다.
    4. Event Loop가 Call Stack이 비어있는 것을 체크하고, Task Queue에서 가장 오래된 작업을 Call Stack으로 보낸다.
    
1. `Call Stack`
    - 요청이 들어올 때 마다 순차적으로 처리하는 Stack(LIFO)
    - 기본적인 javaScript의 Single Thread 작업 처리
2. `Web API`
    - JavaScript 엔진이 아닌 브라우저에서 제공하는 runtime환경으로 시간이 소요되는 작업을 처리(setTimeout, DOM Event, AJAX 요청 등)
- setTimeout : 설정된 시간동안 Web API에서 처리를 시작하지 않고 지연시킨 후 실행됨
1. `Task Queue`
    - 비동기 처리된 Callback함수가 대기하는 Queue(FIFO)
2. `Event Loop`
    - Call Stack과 Task Queue를 지속적으로 모니터링
    - Call stack이 비어있는지 확인 후 비어 있다면 Task Queue에서 대기중인 오래된 작업을 Call Stack으로 Push

### 정리

- JavaScript는 한 번에 하나의 작업을 수행하는 single Thread언어로 동기적 처리를 하지만, 브라우저 환경에서는 Web API에서 처리된 작업이 지속적으로 Task Queue를 거쳐 EventLoop에 의해 Call Stack에 들어와 순차적으로 실행됨으로써 비동기 작업이 가능한 환경이 된다.

# Axios 라이브러리

- JavaScript Http 웹 통신을 위한 라이브러리
- 확장 가능하나 인터페이스와 쉽게 사용할 수 있는 비동기 통신 기능을 제공
- node 환경은 npm을 이용해서 설치 후 사용할 수 있고, browser 환경은 CDN을 이용해서 사용할 수 있음
- Axios 공식 문서 및 Github
    - https://axios-http.com/kr/docs/intro
        - 요청 config 위치에서 요청형식 보기
    - https://github.com/axios/axios

## 1. Axios 사용

- get, post 등 메서드 사용 가능
- `then` : 성공하면 수행할 로직 작성
- `catch` : 이용해서 실패하면 수행할 로직을 작성

### 고양이 사진 가져오기

- the Cat API(https://api.thecatapi.com/v1/images/search)
- 이미지를 요청해서 가져오는 작업을 비동기로 처리

```jsx
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
<script>
  console.log('고양이는 야옹')
  const catImageSearchURL = 'https://api.thecatapi.com/v1/images/search'

    axios.get(catImageSearchURL)
      .then((response) => {
        console.log(response)
      })
      .catch((error) => { 
        console.log('실패했다옹')
      })
      console.log('야옹야옹') 
  })
</script>

// 고양이는 야옹
// 야옹야옹
// {data: Array(1) ...}

```

### 결과

- 동기식 코드 : 위에서 부터 순서대로 처리가 되기 때문에 첫번째 print가 출력되고 이미지를 가져오는 처리를 기다렸다가 다음 print가 출력됨
- 비동기식 코드 : 바로 처리가 가능한 작업은 바로 처리하고, 오래 걸리는 작업인 이미지를 요청하고 가져오는 일은 요청을 보내놓고 기다리지 않고 다음 코드로 진행 후 완료가 된 시점에서 결과 출력이 진행됨

```jsx
<button>야옹아 이리온</button>

  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script>
    console.log('고양이는 야옹')
    const catImageSearchURL = 'https://api.thecatapi.com/v1/images/search'
    // 버튼을 선택하고 이벤트 리스너 달기
    const btn = document.querySelector('button')
    btn.addEventListener('click', function () {
      axios.get(catImageSearchURL)

         // 비동기 요청을 보내고, 응답이 오면 처리하기
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
```

- 버튼을 여러 번 누르면 먼저 로딩되는 이미지부터 나오는 것을 볼 수 있음

### 정리

- axios는 비동기로 데이터 통신을 가능하게 하는 라이브러리
- 같은 방식으로 우리가 배운 Django REST API로 요청을 보내서 데이터를 받아 온 후 처리할 수 있음