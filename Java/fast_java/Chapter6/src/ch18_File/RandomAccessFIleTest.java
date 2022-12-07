package ch18_File;

import java.io.IOException;
import java.io.RandomAccessFile;

public class RandomAccessFIleTest {

	public static void main(String[] args) throws IOException {
		@SuppressWarnings("resource")
		RandomAccessFile rf = new RandomAccessFile("random.txt", "rw");
		rf.writeInt(100);
		System.out.println("파일 포인터 위치:" + rf.getFilePointer());
//		파일 포인터 위치:4
		rf.writeDouble(3.14);
		System.out.println("파일 포인터 위치:" + rf.getFilePointer());
//		파일 포인터 위치:12
		rf.writeUTF("안녕하세요");
		System.out.println("파일 포인터 위치:" + rf.getFilePointer());
//		파일 포인터 위치:29
	
		rf.seek(0);
		System.out.println("파일 포인터 위치:" + rf.getFilePointer());
//		파일 포인터 위치:0
		
		int i = rf.readInt();
		double d = rf.readDouble();
		String str = rf.readUTF();
	
		System.out.println("파일 포인터 위치:" + rf.getFilePointer());
//		파일 포인터 위치:29
		System.out.println(i);
//		100
		System.out.println(d);
//		3.14
		System.out.println(str);
//		안녕하세요

	}

}
