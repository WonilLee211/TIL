package ch08_constructor_practice;

public class OrderInfo {
	
	public long orderNumber;
	public int phoneNumber;
	public String address;
	public int date;
	public int time;
	public int price;
	public int menuNumber;
	
	public OrderInfo(long orderNumber, int phoneNumber, String address, int date, int time, int price, int menuNumber) {
		this.orderNumber = orderNumber;
		this.phoneNumber = phoneNumber;
		this.address = address;
		this.date = date;
		this.time = time;
		this.price = price;
		this.menuNumber = menuNumber;	
	}

}
