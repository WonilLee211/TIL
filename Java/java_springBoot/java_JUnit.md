# JUnit

## TDD(Test-Driven Development)

- 테스트 주도 개발에서 사용하지만, 코드의 유지 보수 및 운영 환경에서의 에러를 미리 방지 하기 위해서 단위 별로 검증 하는 테스트 프레임워크

## 테스트 단위
- 작성한 코드가 기대하는 대로 동작하는지 검증하는 절차

## JUnit
-Java 기반의 단위 테스트를 위한 프레임워크
- Annotation기반으로 테스트를 지원
- Assert를 통하여 예상, 실제를 통해 검증

## 실습

### 계산기 테스트

```java

public class DollarCalculatorTest {
    @Test
    public void testHello(){
        System.out.println("hello");
    }

    @Test
    public void dollar(){
        MarketApi marketApi = new MarketApi();
        DollarCalculator dollarCalculator = new DollarCalculator(marketApi);
        dollarCalculator.init();

        Calculator calculator = new Calculator(dollarCalculator);

        // 인자 : 예상 값, 실행할 메서드
        Assertions.assertEquals(22000, calculator.sum(10 ,10));
        Assertions.assertEquals(0, calculator.minus(10 ,10));
    }
}

```

## mockito

- dependencies 추가
  - // https://mvnrepository.com/artifact/org.mockito/mockito-core
    - `testImplementation group: 'org.mockito', name: 'mockito-core', version: '3.9.0'`
  - // https://mvnrepository.com/artifact/org.mockito/mockito-junit-jupiter
    - `testImplementation group: 'org.mockito', name: 'mockito-junit-jupiter', version: '3.9.0'`
  


```java 
// 특정한 객체가 매칭됐을 때 원하는 결과값이 나오는지 확인
@ExtendWith(MockitoExtension.class)
public class DollarCalculatorTest {

    // 1. MarketAPi Mocking 처리
    @Mock
    public MarketApi marketApi;

    @BeforeEach
    public void init(){

        // 2. marketApi.connect()가 실행될 때 1100 값이 아닌 다른 값으로 리턴하도록 설정
        Mockito.lenient().when(marketApi.connect()).thenReturn(3000);
    }

    @Test
    public void dollarTest(){
        MarketApi marketApi = new MarketApi();
        DollarCalculator dollarCalculator = new DollarCalculator(marketApi);
        dollarCalculator.init();

        Calculator calculator = new Calculator(dollarCalculator);

        Assertions.assertEquals(22000, calculator.sum(10 ,10));
        Assertions.assertEquals(0, calculator.minus(10 ,10));
    }

    @Test
    public void mockTest(){
        // @Mock 처리한 marketApi를 객체로 넣기
        DollarCalculator dollarCalculator = new DollarCalculator(marketApi);
        dollarCalculator.init();

        Calculator calculator = new Calculator(dollarCalculator);

        // 인자 : 예상 값, 실행할 메서드
        Assertions.assertEquals(60000, calculator.sum(10 ,10));
        Assertions.assertEquals(0, calculator.minus(10 ,10));
    }
}


```

## REST API CRUD 테스트 코드

## 1. 통합테스트 


```java
package com.example.springcalculatortdd.component;


// 통합테스트
@SpringBootTest // 모든 빈이 등록됨
public class DollarCalculatorTest {

    @MockBean
    private MarketApi marketApi;

    @Autowired // 필요한 의존 객체의 타입에 해당하는 빈을 찾아 주입한다.
    private Calculator calculator;

    @Test
    public void dollarCalculatorTest(){
        Mockito.when(marketApi.connect()).thenReturn(3000);

        int sum = calculator.sum(10, 10);
        int minus = calculator.minus(10, 10);
        
        Assertions.assertEquals(60000, sum);
        Assertions.assertEquals(0, minus);

    }
}

```

## 2. 단위 테스트

### GET method Test

```java
package com.example.springcalculatortdd.controller;

@WebMvcTest(CalculatorApiController.class) // web에 특화된 자원만 빈에 등록함. @SpringBootTest보다 경제적
@AutoConfigureWebMvc
@Import({Calculator.class, DollarCalculator.class}) // 예외로 가지고 와야하는 클래스들 선언
public class CalculatorApiControllerTest {

    @MockBean
    private MarketApi marketApi; // import 말고 mocking으로 가져오기

    @Autowired
    private MockMvc mockMvc;

    @BeforeEach
    public void init(){
        Mockito.when(marketApi.connect()).thenReturn(3000);
    }

    // GET method Test
    @Test
    public void sumTest() throws Exception {
        // http://localhost:8080/api/sum

        mockMvc.perform(
                MockMvcRequestBuilders.get("http://localhost:8080/api/sum")
                        .queryParam("x", "10")
                        .queryParam("y", "10")
        ).andExpect(
                MockMvcResultMatchers.status().isOk()
        ).andExpect(
                MockMvcResultMatchers.content().string("60000")
        ).andDo(MockMvcResultHandlers.print());

    }


}

```

### POST Method

```java
package com.example.springcalculatortdd.controller;

@WebMvcTest(CalculatorApiController.class) // web에 특화된 자원만 빈에 등록함. @SpringBootTest보다 경제적
@AutoConfigureWebMvc
@Import({Calculator.class, DollarCalculator.class})
public class CalculatorApiControllerTest {

    @MockBean
    private MarketApi marketApi;

    @Autowired
    private MockMvc mockMvc;

    @BeforeEach
    public void init(){
        Mockito.when(marketApi.connect()).thenReturn(3000);
    }

    @Test
    public void minusTest() throws Exception {

        Req req = new Req();
        req.setX(10);
        req.setY(10);

        String json = new ObjectMapper().writeValueAsString(req);

        mockMvc.perform(
                MockMvcRequestBuilders.post("http://localhost:8080/api/minus")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(json)
        ).andExpect(
                MockMvcResultMatchers.status().isOk()
        ).andExpect(
                MockMvcResultMatchers.jsonPath("$.result").value("0")
        ).andExpect(
                MockMvcResultMatchers.jsonPath("$.response.resultCode").value("OK")
        ).andDo(
             MockMvcResultHandlers.print()
        );
    }
}

```

## Jacoco

- Java코드의 코드 커버리지를 체크하는 라이브러리 결과를 Html, xml, csv로 확인이 가능

- build.gradle에서 plugins에 `id 'jacoco'` 추가
- gradle/Tasks/verification/test 실행(double-click)
- gradle/Tasks/verification/JacocoTestReport 확인 
  - build.reports에서 index.html 확인할 수 있음