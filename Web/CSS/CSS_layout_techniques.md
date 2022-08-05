# CSS layout techniques

- display
- position
- float(1996)
- flexbox(2012)
- grid(2017)
- 기타

### CSS 원칙

1. **normal flow**
    - inline direction과 block direction의 자연스러운 방향으로 쌓이는 흐름
    - 모든 요소는 네모(박스모델)이고 위에서 아래로, 왼쪽에서 오른쪽으로 쌓인다.
    - 방향이 중요한게 아니라, 쌓인다는 개념이 핵심이다.
    - 요소가 자리를 차지하고 쌓인다는 개념

---

# 1. Float(중요하지 않음)

- 박스를 왼쪽 혹은 오른쪽으로 이동시켜 텍스트를 포함 인라인 요소들이 주변을 wrapping하도록 함
- 요소가 normal flow를 벗어나도록 함
    - `clear:left/right/both;` 하지 않으면(`clear:none;`) 다른 박스가 float박스를 침범하게 됨.
    - float은 떠다니는데 텍스트가 float경계를 따라 쌓이는 것 뿐

## 1.2. 속성  설명

- none : 기본값
- left : 요소를 왼쪽으로 띄움
- right : 요소를 오른쪽으로 띄움

---

# <mark>2. Flexbox(핵심)</mark>

## 2.1. CSS Flexible Box Layout

- 행과 열 형태로 아이템들을 배치하는 1차원 레이아웃 모델

### 축

- main axis(메인 축)
- cross axis(교차 축)

### 구성요소

- flex container(부모요소)
    - flexbox레이아웃을 형성하는 가장 기본 모델
    - flex item들이 놓이는 영역
    - `.display:flex/inline-flex;` 선언
    - `flex-direction : row/row-reverse/column/column-reverse;` 으로 main 축 변경
- flex item(자식 요소)
    - 부모태그 안에 각각의 요소들이 들어가 있는 형태를 구성

### <mark>축 : main axis(중요)</mark>

- 기본 `row` : 방향이 >> .(1 ~~2 3 4 5~~)
- 방향도 조절 가능

### cross axis

- 좌우가 없다
- 그냥 main axis의 수직 방향으로 생각

### 개발자도구에서 flex 배치 테스트

- 개발자도구 - styles - 버튼

### display: inline-flex;

- 박스와 인라인 차이라고 생각하자.

## 2.2 Flex 속성

### 배치 설정

- **flex-direction**
- flex-wrap

### 공간나누기

- **justify-content(main axis)**
- **align content(cross axis)**

### 정렬

- **align-items (모든 아이템을 cross axis기준으로)**
- align-self ( 개별적으로 정렬, 보통 통일로 배치하는게 나아서 잘 안씀)

### <mark>flex-direction(중요)</mark>

- main axis 기준 방향 설정
- 역방향의 경우 html 태그 선언 순서와 시각적으로 다르니 유의(웹 접근성에 영향)

### flex-wrap(기억만 하기)

- 아이템이 범위를 벗어날 경우, 요소들이 강제로 한 줄에 배치되도록 할지 결정
- 아이템이 컨테이너를 벗어나는 경우 해당 영역 내에 배치되도록 설정
- 즉, 기본적으로 컨테이너 영역을 벗어나지 못하게 함.
- wrap(default) : 아이템 크기를 줄이지않도록 배치. 넘치면 다음 줄로 이동
    - wrap-reverse : 최신 글이 위로 배치되도록 함
- nowrap : 넘치면 아이템 크기 줄여서 맞춤

### flex-flow

- flex-direction과 flex-wrap의 shorthand(두개를 한번에 설정)
- flex-direction과 flex-wrap에 대한 설정값을 차레로 작성
- 예)  `flex-flow : row nowrap;`

### justify-content(메인축에서 왔다 갔다)

- main axis를 기준으로 공백 배분
- option
    1. flex-start : 메인축이 쌓이기 시작하는 곳에서 임의의 간격으로 배치
    2. flex-end : 매인축이 쌓이기 시작하는 부분 반대편에서부터 임의의 간격으로 배치
    3. center :  메인 축에서 정중앙
    4. space-between : 아이템 양끝에 배치하고 남은 공간 아이템 사이에 배분
    5. space-around : 아이템의 좌우를 같은 간격으로 배분하고 쌓기
    6. space-evenly : 공간이 균등하게 배분

### align-content

- cross axis를 기준으로 공백 배분
- 아이템이 한 줄로 배치되는 경우 확인할 수 없음
- option
    1. first-start : 아이템들이 메인축 방향으로 쌓이긴 하는데, 교차축의 시작점에 배치(공백이 끝부분에)
    2. first-end : 아이템들이 메인축 방향으로 쌓이긴 하는데, 교차축의 끝점에 배치(공백이 시작점에)
    3. center : 아이템들이 메인축 방향으로 쌓이긴 하는데, 교차축의 중앙에 배치(공백을 양분)
    4. space-between : 공백을 중간에 배치
    5. space-around : 공백을 아이템 매인 축 위아래로 같은 공백 배분
    6. space-evenly : 메인 축마다 동일한 공백 배분
    
    ### justify&align content 공통 요소(1,2,3 외우기)
    
    1. **flex-start : 아이템들을 axis 시작점으로**
    2. **flex-end : 아이템들을 axis 끝 쪽으로**
    3. **center : 아이템들을 axis 중앙으로**
    4. space-between : 아이템 사이 간격을 균일하게 분배
    5. space-around : 아이템을 둘러싼 영역을 균일하게 분배(가질 수 있는 영역을 반으로 나눠 양쪽에)
    6. space-evenly : 전체 영역에서 아이템간 간격을 균일하게 분배

### align-items

- 모든 아이템을 cross axis기준으로 정렬
- 요소
    1. stretch : 컨테이너를 가득 채움
    2. flex-start : 축 방향 시작점
    3. flex-end : 축 방향 끝점
    4. center : 가운데
    5. baseline : 텍스트 baseline에 기준선을 맞춤

### align-self

- 개별 아이템을 cross axis기준으로 정렬
    - 주의 해당 속성은 컨테이너에 적용하는 것이 아니라 개별 아이템에 적용
    - 요소
        1. stretch
        2. flex-start
        3. flex-end
        4. center
        

### 기타 속성

- `flex-grow` : 남은 영역을 아이템에 분배(다중 설정하면 값의 비율에 따라 배분)
    - 
- `order` : 배치 순서(-1이 제일 앞)

## 활용 레이아웃 - 수직 수평 가운데 정렬

```css
/*방법 1
컨테이너 설정
*/
.container {
  display : flex;
  justify-content : center;
  align-items: center;
}

/*방법 2
아이템 설정
*/
.container {
  display : flex;
}
.item {
  margin : auto;
}
```