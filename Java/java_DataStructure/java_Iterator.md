# 11. Collection 요소를 순회하는 Iterator

## 요소의 순회란?

- 컬렉션 프레임워크에 저장된 요소들을 하나씩 차례로 참조하는것

- 순서가 있는 List인터페이스의 경우는 Iterator를 사용 하지 않고 get(i) 메서드를 활용할 수 있음

- **Set 인터페이스의 경우 get(i) 메서드가 제공되지 않으므로 Iterator를 활용하여 객체를 순회함**

## Iterator 사용하기

- boolean hasNext() : 이후에 요소가 더 있는지를 체크하는 메서드, 요소가 있다면 true를 반환

- E next() : 다음에 있는 요소를 반환

MemberArrayList.java 의 removeMember() 메서드를 Iterator를 활용하여 구현
```java
package ch10_ArrayList;

import java.util.ArrayList;
import java.util.Iterator;

public class MemberArrayList {
    ..
	
	public boolean removeMember(int memberId) {
		
		// Iterator를 활용한 구현
		Iterator<Member> ir = arrayList.iterator();
		
		while(ir.hasNext()) {
			Member member = ir.next();
			int tempId = member.getMemberId();
			
			if(tempId == memberId) {
				arrayList.remove(memberId);
				return true;
			}
		}
		
		// get() 메서드를 이용한 요소 순회
		/*
		for(int i = 0; i < arrayList.size(); i++) {
			Member member = arrayList.get(i);
			int tempId = member.getMemberId();
			if(tempId == memberId) {
				arrayList.remove(i);
				return true;
			}
		}
		*/

		System.out.println(memberId + "가 존재하지 않습니다");  //for 가 끝날때 까지 return 이 안된경우
		return false;
	}
    ...
}

```



