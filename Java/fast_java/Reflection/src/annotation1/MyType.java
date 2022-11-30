package annotation1;

// @interface 추가해서 어노테이션으로 만들기
public @interface MyType {
	Class<?> classType();
	String stringType();
	int intType();
	
	Food foodType();
	
	Class<?>[] classArrType();
	
	String[] stringArrDefault() default {"a", "b"};
}
