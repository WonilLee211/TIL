import org.example.Calculator;
import org.example.DollarCalculator;
import org.example.MarketApi;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.Mock;
import org.mockito.Mockito;
import org.mockito.junit.jupiter.MockitoExtension;

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

        // 인자 : 예상 값, 실행할 메서드
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
