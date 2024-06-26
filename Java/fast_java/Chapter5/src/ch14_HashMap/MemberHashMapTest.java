package ch14_HashMap;

public class MemberHashMapTest {

	public static void main(String[] args) {
		
		MemberHashMap memberHashMap = new MemberHashMap();
		
		Member memberLee = new Member(1001, "이순신");
		Member memberKim = new Member(1002, "김유신");
		Member memberKang = new Member(1003, "강감찬");
		Member memberHong = new Member(1004, "홍길동");
		
		memberHashMap.addMember(memberLee);
		memberHashMap.addMember(memberKim);
		memberHashMap.addMember(memberKang);
		memberHashMap.addMember(memberHong);
		
//		이순신 회원님의 아이디는 1001입니다
//		김유신 회원님의 아이디는 1002입니다
//		강감찬 회원님의 아이디는 1003입니다
//		홍길동 회원님의 아이디는 1004입니다

		memberHashMap.showAllMember();

		memberHashMap.removeMember(1004);
		memberHashMap.showAllMember();

//		이순신 회원님의 아이디는 1001입니다
//		김유신 회원님의 아이디는 1002입니다
//		강감찬 회원님의 아이디는 1003입니다
	}

}
