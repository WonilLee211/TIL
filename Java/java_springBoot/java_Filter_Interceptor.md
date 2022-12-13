# Spring Boot Filter와 Interceptor

## Filter

- Web Application에서 관리되는 영역
- Spring Boot Framework 에서 Client로 부터 오는 요청/응답에 대해서 최초/최종 단계의 위치에 존재
- **요청/응답의 정보를 변경하거나, Spring에 의해서 데이터가 변환되기 전의 순수한 Client의 요청/응답 값을 확인 할 수 있다.**
- **유일하게 ServletRequest, ServletResponse 의 객체를 변환 할 수 있다.**
- 주로 Spring Framework에서는 request / response의 Logging 용도로 활용하거나, 인증과 관련된 Logic 들을 해당 Filter에서 처리 한다.
- 이를 선/후 처리함으로써, Service business logic과 분리 시킨다.

![lifeStyle](../img/MVCLifeStyle.PNG)