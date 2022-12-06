# 12. 중복되지 않게 자료를 관리하는 Set 인터페이스를 구현한 클래스와 그 활용

## HashSet 클래스

- Set 인터페이스를 구현한 클래스와

- 멤버의 중복 여부를 체크하기 위해 인스턴스의 동일성을 확인해야 함

- 동일성 구현을 위해 필요에 따라 equals()와 hashCode()메서드를 재정의함


HashSetTest.java
```java
package ch12_hashSet;

import java.util.HashSet;

public class HashsetTest {

	public static void main(String[] args) {
		
		HashSet<String> hashSet = new HashSet<String>();
		hashSet.add(new String("김유신"));
		hashSet.add(new String("이순신"));
		hashSet.add(new String("홍연의"));
		hashSet.add(new String("강감찬"));
		hashSet.add(new String("강감찬"));
		
		System.out.println(hashSet);
		// [김유신, 홍연의, 강감찬, 이순신]

	}
}

```

MemberHashSet.java
```java
package ch12_hashSet;

import java.util.HashSet;
import java.util.Iterator;

public class MemberHashSet {
	
	private HashSet<Member> hashSet;
	
	public MemberHashSet() {
		hashSet = new HashSet<Member>();
	}
	
	public void addMember(Member member) {
		hashSet.add(member);
	}
	
	public boolean removeMember(int memberId) {
		
		Iterator<Member> ir = hashSet.iterator();
		while(ir.hasNext()) {
			Member member = ir.next();
			int tempId = member.getMemberId();
			if(tempId == memberId) {
				hashSet.remove(member);
				return true;
			}
		}
		System.out.println(memberId + "가 존재하지 않습니다");
		return false;
		
	}
	
	public void showAllMember(){
		for(Member member : hashSet){
			System.out.println(member);
		}
		System.out.println();
	}

}

```

MemberHashSetTest.java
```java
package ch12_hashSet;

public class MemberHashSetTest {

	public static void main(String[] args) {
		
		MemberHashSet memberHashSet = new MemberHashSet();
		
		Member memberLee = new Member(1001, "이순신");
		Member memberKim = new Member(1002, "김유신");
		Member memberKang = new Member(1003, "강감찬");
		
		
		memberHashSet.addMember(memberLee);
		memberHashSet.addMember(memberKim);
		memberHashSet.addMember(memberKang);
		memberHashSet.showAllMember();

		//		이순신 회원님의 아이디는 1001입니다
//		김유신 회원님의 아이디는 1002입니다
//		강감찬 회원님의 아이디는 1003입니다
		
		Member memberHong = new Member(1003, "홍길동");  //1003 아이디 중복 
		memberHashSet.addMember(memberHong);
		memberHashSet.showAllMember();
		
//
//		이순신 회원님의 아이디는 1001입니다
//		김유신 회원님의 아이디는 1002입니다
//		강감찬 회원님의 아이디는 1003입니다


	}

}

```

- 아이디가 동일한 경우 같은 멤버이므로 중복되지 않도록 Member 클래스의 equals()와 hashCode()메서드를 재정의함

Member.java
```java
package ch12_hashSet;

public class Member {
    ...
	
	// hashCode 재정의 필요
	@Override
	public int hashCode() {
		return memberId;
	}
	
	@Override
	public boolean equals(Object obj) {
		if(obj instanceof Member) {
			Member member = (Member)obj;
			if(this.memberId == member.getMemberId()) {
				return true;
			}
			else {
				return false;
			}
		}
		return false;
	}
	
}

```
  
