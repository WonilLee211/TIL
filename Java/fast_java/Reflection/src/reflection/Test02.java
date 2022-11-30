package reflection;

import java.lang.reflect.Method;
import java.lang.reflect.Parameter;
import java.lang.reflect.Type;

public class Test02 {

	public static void main(String[] args) {
		try {
			exam();
			exam2();
		}catch (Exception e) {
			e.printStackTrace();
		}

	}
	
	private static void exam() throws Exception {
		
		Class<?> clz = Dog.class;
		
		
		System.out.println("Dog이 가지고 있는 모든 메서드들을 출력해보자");
		Method[] mArr = clz.getDeclaredMethods();
		
		
		for(Method m : mArr) {
			System.out.println("메서드 이름: " + m.getName());
			
			Class<?> rClz = m.getReturnType();
			System.out.println("반환타입 :" + rClz.getName());
			
			// 파라미터 정보를 가져와보자
			Parameter[] pArr = m.getParameters();
			for(Parameter p : pArr) {
				Type t = p.getParameterizedType();
			    System.out.println(t.getTypeName() + " " + p.getName());
			}
		}
		
 		
	}
	// reflection을 이용한 메서드 실행
	private static void exam2() throws Exception {
		Class<?> clz = Class.forName("reflection.Dog");
		Object obj = clz.getDeclaredConstructor().newInstance();
		
		// setName이라는 메서드를 얻어보자
		Method method = clz.getDeclaredMethod("setName", String.class);
		
		// 메서드를 실행하는 방법 : invoke(객체, 매개변수)
		method.invoke(obj, "마리");
		
		method = clz.getDeclaredMethod("getName");
		// 형변환을 시켜줘야한다.			
		//String name = method.invoke(obj);
		String name = (String)method.invoke(obj);
		System.out.println(name);
	}

}
//Dog이 가지고 있는 모든 메서드들을 출력해보자
//메서드 이름: setAge
//반환타입 :void
//int arg0
//메서드 이름: getAge
//반환타입 :int
//메서드 이름: getName
//반환타입 :java.lang.String
//메서드 이름: setName
//반환타입 :void
//java.lang.String arg0
//마리
