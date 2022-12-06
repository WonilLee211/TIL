package ch10_ArrayList;

import java.util.ArrayList;
import java.util.Iterator;

public class MemberArrayList {
	private ArrayList<Member> arrayList; // ArrayList 선언
	
	public MemberArrayList() {
		arrayList = new ArrayList<Member>(); // Member로 선언한  ArrayList 생성
		
	}
	
	public void addMember(Member member) { // ArrayList에 맴버 추가
		arrayList.add(member);
	}
	
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
	
	public void showAllMember() {
		for(Member member : arrayList) {
			System.out.println(member);
		}
		System.out.println();
	}
}
