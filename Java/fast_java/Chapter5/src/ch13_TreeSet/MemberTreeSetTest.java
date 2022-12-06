package ch13_TreeSet;

public class MemberTreeSetTest {

	public static void main(String[] args) {
		
		MemberTreeSet memberTreeSet = new MemberTreeSet();
		
		Member memberKim = new Member(1003, "김유신");
		Member memberLee = new Member(1001, "이순신");
		Member memberKang = new Member(1002, "강감찬");
		
		memberTreeSet.addMember(memberKim);
		memberTreeSet.addMember(memberLee);
		memberTreeSet.addMember(memberKang);
		memberTreeSet.showAllMember();

	}
	// 내림차순
//	김유신 회원님의 아이디는 1003입니다
//	강감찬 회원님의 아이디는 1002입니다
//	이순신 회원님의 아이디는 1001입니다

}
