package ch05_stream;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class IntArrayStreamTest {

	public static void main(String[] args) {
		
		int[] arr = {1,2,3,4,5};
		// 에러 발생
		Arrays.stream(arr).forEach(n->System.out.println(n));
		System.out.println();
//		1
//		2
//		3
//		4
//		5
		
		int sum  = Arrays.stream(arr).sum();
		System.out.println("sum: " + sum);
//		sum: 15
		
		List<Integer> list = new ArrayList<Integer>();
		list.add(1);
		list.add(2);
		list.add(3);
		list.add(4);
		list.add(5);
		int sum2 = list.stream().mapToInt(n->n.intValue()).sum();
		System.out.println(sum2);
//		15


	}

}
