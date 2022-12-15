# 여러가지 annotation

1. `@SpringBootApplication` : Spring boot application으로 설정
2. `@Controller` : View를 제공하는 controller로 설정
3. `@RestController` : View를 제공하는 controller로 설정
4. `@RequestMapping` : URL 주소를 맵핑
5. `@GetMappiang` : Http GetMethod Url 주소 맵핑
6. `@PostMappiang` : Http PostMethod Url 주소 맵핑
7. `@PutMappiang` : Http PutMethod Url 주소 맵핑
8. `@DeleteMappiang` : Http DeleteMethod Url 주소 맵핑
9. `@RequestParam` : URL Query Parameter 맵핑
10. `@RequestBody` : Http Body를 Parsing 맵핑
11. `@Valid` : POJO Java class의 검증
12. `@Configration` : 1개 이상의 bean을 등록할 때 설정
13. `@Component` : 1개의 Class 단위로 등록할 때 사용
14. `@Bean` : 1개의 외부 library로부터 생성한 객체를 등록 시 사용
15. `@Autowired` : DI를 위한 곳에 사용
16. `@Qualifier` : @Autowired 사용 시 bean이 2개 이상일 때 명시적 사용
17. `@Resource` : @Autowired + @Qualifier 의 개념으로 이해
18. `@Aspect` : AOP 적용 시 사용
19. `@Before` : AOP 메소드 이전 호출 지정
20. `@After` : 메소드가 성공적으로 실행 후, 예외가 발생하더라도 실행
21. `@AfterReturning` : 메소드 호출 성공 실행 시(Not Throws)
22. `@AfterThrowing` : 메소드 호출 실패 예외 발생(Throws)
23. `@Around` : Before / after  모두 제어

