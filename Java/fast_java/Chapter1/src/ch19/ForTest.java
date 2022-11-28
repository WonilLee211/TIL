package ch19;

public class ForTest {

	public static void main(String[] args) {
		
		int count =0;
		int sum = 0;
		
		for( int i = 0 ; i<10; i++, ++count) {  //10번
			sum += count;
			//count++;
			System.out.println(i);
			System.out.println(count);
		}
		System.out.println(sum);

	}

}
