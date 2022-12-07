package ch18_File;

import java.io.File;
import java.io.IOException;

public class FileTest {

	public static void main(String[] args) throws IOException {
		
		File file = new File("C:\\Users\\LEEWONIL\\ssafy8th\\TIL\\Java\\fast_java\\Chapter6\\newFile.txt");
		file.createNewFile();
		
		System.out.println(file.isFile());
//		true
		System.out.println(file.isDirectory());
//		false
		System.out.println(file.getName());
//		newFile.txt
		System.out.println(file.getAbsolutePath());
//		C:\Users\LEEWONIL\ssafy8th\TIL\Java\fast_java\Chapter6\newFile.txt
		System.out.println(file.getPath());
//		C:\Users\LEEWONIL\ssafy8th\TIL\Java\fast_java\Chapter6\newFile.txt
		System.out.println(file.canRead());
//		true
		System.out.println(file.canWrite());
//		true
		file.delete();

	}

}
