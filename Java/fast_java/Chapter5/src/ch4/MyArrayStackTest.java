package ch4;

public class MyArrayStackTest {

	public static void main(String[] args) {

		MyArrayStack stack = new MyArrayStack(3);
		
		stack.push(10);
		stack.push(20);
		stack.push(30);
		stack.push(40);
		
		stack.printAll();
		
		System.out.println("top element is " + stack.pop());
		stack.printAll();
		System.out.println("stack size is " + stack.getSize());
	}

	
//	stack is full
//	10
//	20
//	30
//	top element is 30
//	10
//	20
//	stack size is 2
}
