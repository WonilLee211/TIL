package com.example.springcalculatortdd.component;


import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import org.mockito.Mockito;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.mock.mockito.MockBean;


// 단위 테스트
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
