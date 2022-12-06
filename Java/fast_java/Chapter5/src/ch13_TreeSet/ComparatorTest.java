package ch13_TreeSet;

import java.util.Set;
import java.util.TreeSet;

public class ComparatorTest{

	public static void main(String[] args) {
		Set<String> set = new TreeSet<String>(new MyCompare());
		set.add("add");
		set.add("bbb");
		set.add("ccc");
		
		System.out.println(set);
	}
	
}