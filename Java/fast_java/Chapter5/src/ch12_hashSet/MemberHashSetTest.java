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
