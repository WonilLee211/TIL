package ch2;

public class MyArrarTest {

	public static void main(String[] args) {
		MyArray array = new MyArray();
		array.addElement(10);
		array.addElement(20);
		array.addElement(30);
		array.insertElement(1, 50);
		array.printAll();
		
		System.out.println("===============");
		array.removeElement(1);
		array.printAll();
		System.out.println("===============");
			
		array.addElement(70);
		array.printAll();
		System.out.println("===============");
		array.removeElement(1);
		array.printAll();
		
		System.out.println("===============");
		System.out.println(array.getElement(2));

	}
	
//	10
//	50
//	20
//	30
//	===============
//	10
//	20
//	30
//	===============
//	10
//	20
//	30
//	70
//	===============
//	10
//	30
//	70
//	===============
//	70

}
