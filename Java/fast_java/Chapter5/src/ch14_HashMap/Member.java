package ch14_HashMap;


//Member class가 아이디 오름차순으로 정렬되게 하기 위해 Comparable 인터페이스 구현
public class Member implements Comparable<Member>{
	
	private int memberId;
	private String memberName;
	
	public Member(int memberId, String memberName) {
		this.memberId = memberId;
		this.memberName = memberName;
	}
	
	public int getMemberId() {
		return memberId;
	}
	
	public String getMemberName() {
		return memberName;
	}
	public void setMemberId(int memberId) {
		this.memberId = memberId;
	}
	public void setMemberName(String memberName) {
		this.memberName = memberName;
	}
	
	@Override
	public String toString(){   //toString 메소드 오버로딩
		return memberName + " 회원님의 아이디는 " + memberId + "입니다";
	}
	
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
	
	// TreeSet의  compareTo 재정의
	@Override
	public int compareTo(Member member) {
//		return (this.memberId - member.memberId); // 오룸차순
		return (this.memberId - member.memberId) * (-1); // 내림차순
	}
	
}
