package ch03_FunctionalInterface;

import java.util.Arrays;

public class InArrayTest {
	public static void main(String[] args) {
		
		int[] arr = {1, 2, 3, 4, 5};
		int sumVal = Arrays.stream(arr).sum();
		long count = Arrays.stream(arr).count();
		
		System.out.println(sumVal);
		System.out.println(count);
		
//		15
//		5

	}
}
