package annotation2;

import java.lang.annotation.Target;
import java.lang.annotation.ElementType;

// Target을 작성하지 않으면 아무데나 붙일 수 있음
//@Target(value=ElementType.PARAMETER)
// 이렇게하면 모든 곳에 붙일 수 있음
@Target({
	ElementType.TYPE,
	ElementType.FIELD,
	ElementType.METHOD,
	ElementType.LOCAL_VARIABLE,
	ElementType.PARAMETER,
})
public @interface MyTarget {

}
