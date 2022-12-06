package ch13_TreeSet;

import java.util.Comparator;

class MyCompare implements Comparator<String>{

	// Comparator의 활용 : 이미 Comparable이 구현된 경우 
	//Comparator로 비교하는 방식을 다시 구현할 수 있음
	@Override
	public int compare(String s1, String s2) {
		
		return (s1.compareTo(s2)) * (-1);
	}
}