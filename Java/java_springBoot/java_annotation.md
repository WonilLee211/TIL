# 여러가지 annotation

1. `@SpringBootApplication` :  Spring boot application으로 설정
2. `@Controller` : View를 제공하는 Controller로 설정

   - response형태가 기본적으로 html

3. `@RestController` : REST API를 제공하는 Controller로 설정
   - response형태가 기본적으로 json
4. `@RequestMapping` : URL주소를 맵핑

   - 원하는 http method를 선언하지않으면 http Method가 실행됨

5. `@GetMapping` : Http GetMethod URL 주소 맵핑
6. `@PostMapping` : Http PostMethod URL 주소 맵핑
7. `@PutMapping` : Http PutMethod URL 주소 맵핑
8. `@DeleteMapping` : Http DeleteMethod URL 주소 맵핑
9.  `@RequestParam` : URL  Query Parameter 맵핑
10. `@RequestBody` : Http Body를 Parsing 맵핑
11. `@Valid` : POJO java class의 검증
12. `@Configuration` : 1개 이상의 bean을 등록할 때 사용
13. `@Component` : 1개의 class단위로 등록할 때 클래스 위에 달아서 사용
14. `@Bean` : 1개의 외부 라이브러리로부터 생성한 객체를 등록 시 메소드에 위에 달아서 사용
    - 직접 new 객체로 생성하고 ban으로 등록할 때 사용

15. `@Autowired` : DI를 받기 위한 곳에 사용

    - 기본적으로 생성자로 된 메서드에 들어오는 건 스프링이 알아서 주입해줌
    - 명시적으로 받고싶을 때 사용

16. `@Qualifier` : @Autowired 사용 시 bean이 2개 이상일 때 사용할 bean을 명시적으로 선언
17. `@Resource` : @Autowired + @Qualifier의 개념으로 이해
18. `@Aspect` : AOP적용 시 사용
19. `@Before` : AOP 메소드 실행 이전 호출 지정
20. `@After` : AOP 메소드 호출 이후 지정 예외 발생 포함
21. `@Around` : AOP 이전/이후 모두 포함 예외 발생 포함
22. `@AfterReturning` : AOP 메소드의 호출이 정상일 때 실행
23. `@AfterThrowing` : AOP 시 해당 메소드가 예외 발생 시 지정
