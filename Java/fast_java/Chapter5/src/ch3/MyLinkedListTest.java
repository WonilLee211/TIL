package ch3;

public class MyLinkedListTest {
	public static void main(String[] args) {

		MyLinkedList list = new MyLinkedList();
		list.addElement("A");
		list.addElement("B");
		list.addElement("C");
		list.printAll();
		list.insertElement(3, "D");
		list.printAll();
		list.removeElement(0);
		list.printAll();
		list.removeElement(1);
		list.printAll();
						
		list.insertElement(0, "A-1");
		list.printAll();
		System.out.println(list.getSize());
		
		list.removeElement(0);
		list.printAll();
		System.out.println(list.getSize());
		
		list.removeAll();
		list.printAll();
		list.addElement("A");
		list.printAll();
		System.out.println(list.getElement(0));
		list.removeElement(0);
	}
//	A+->B+->C
//	A+->B+->C+->D
//	0번째 항목 삭제되었습니다.
//	B+->C+->D
//	1번째 항목 삭제되었습니다.
//	B+->D
//	A-1+->B+->D
//	3
//	0번째 항목 삭제되었습니다.
//	B+->D
//	2
//	출력할 내용이 없습니다.
//	A
//	A
//	0번째 항목 삭제되었습니다.
}
