package ch10;

public class TypeConversionTest {

	public static void main(String[] args) {
		byte bNum = 10;
		int iNum = bNum;
		System.out.print(iNum); // 10
		
		int iNum1 = 20;
		float fNum = iNum1;
		System.out.print(fNum); //20.0 암시적 형변환
		
		int iNum2 = 10;
		byte bNum1 = (byte)iNum2;
		System.out.print(bNum1); // 10 명시적 형변환
		
		double dNum = 3.14;
		int iNum3 = (int)dNum;
		System.out.print(iNum3); // 3 명시적 형변환
	}
}
