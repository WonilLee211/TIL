package ch20_Thread;

import java.util.ArrayList;

class FastLibrary{
	
	public ArrayList<String> shelf = new ArrayList<String>();
	
	public FastLibrary(){
		
		shelf.add("태백산맥 1");
		shelf.add("태백산맥 2");
		shelf.add("태백산맥 3");
	}
	
	public synchronized String lendBook() throws InterruptedException{
		
		Thread t = Thread.currentThread();
		
		while( shelf.size() == 0 ){
//		if(shelf.size() == 0 ) {
			System.out.println(t.getName() + " waiting start");
			wait();
			System.out.println(t.getName() + " waiting end");
		}
		String book = shelf.remove(0);
		System.out.println(t.getName() + ": " + book + " lend");
	
		return book;
	}
	
	public synchronized void returnBook(String book){
		Thread t = Thread.currentThread();
		
		shelf.add(book);
		notifyAll();
//		notify();
		System.out.println(t.getName() + ": " + book + " return");
	}
	
}

class Student extends Thread{
	
	public void run(){

		try{
				
			
			String title = LibraryMain.library.lendBook();
			if( title == null ) return;
			sleep(5000);
			LibraryMain.library.returnBook(title);
			
		}catch (InterruptedException e) {
			System.out.println(e);
		}
	}
	
}

public class LibraryMain {

	public static FastLibrary library = new FastLibrary(); 
	public static void main(String[] args) {

		Student std1 = new Student();
		Student std2 = new Student();
		Student std3 = new Student();
		Student std4 = new Student();
		Student std5 = new Student();
		Student std6 = new Student();
		
		std1.start();
		std2.start();
		std3.start();
		std4.start();
		std5.start();
		std6.start();
	}
//	notifyAll()
//	Thread-0: 태백산맥 1 lend
//	Thread-4: 태백산맥 2 lend
//	Thread-3: 태백산맥 3 lend
//	Thread-2 waiting start
//	Thread-1 waiting start
//	Thread-5 waiting start
//	Thread-4: 태백산맥 2 return
//	Thread-2 waiting end
//	Thread-2: 태백산맥 2 lend
//	Thread-0: 태백산맥 1 return
//	Thread-3: 태백산맥 3 return
//	Thread-5 waiting end
//	Thread-5: 태백산맥 1 lend
//	Thread-1 waiting end
//	Thread-1: 태백산맥 3 lend
//	Thread-2: 태백산맥 2 return
//	Thread-1: 태백산맥 3 return
//	Thread-5: 태백산맥 1 return

//	notify()
//	Thread-0: 태백산맥 1 lend
//	Thread-3: 태백산맥 2 lend
//	Thread-2: 태백산맥 3 lend
//	Thread-5 waiting start
//	Thread-1 waiting start
//	Thread-4 waiting start
//	Thread-3: 태백산맥 2 return
//	Thread-5 waiting end
//	Thread-5: 태백산맥 2 lend
//	Thread-0: 태백산맥 1 return
//	Thread-1 waiting end
//	Thread-1: 태백산맥 1 lend
//	Thread-2: 태백산맥 3 return
//	Thread-4 waiting end
//	Thread-4: 태백산맥 3 lend
//	Thread-1: 태백산맥 1 return
//	Thread-5: 태백산맥 2 return
//	Thread-4: 태백산맥 3 return


}