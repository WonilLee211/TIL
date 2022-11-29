package ch08_constructor_practice;

public class UserOrderTest {

	public static void main(String[] args) {
		UserInfo user = new UserInfo();
		user.userName = "Tomas";
		user.age = 37;
		user.weight = 78;
		user.height = 180;
		user.isMale = true;
		
		System.out.println(user.showUserInfo());
		
		OrderInfo order = new OrderInfo(202011020003L, 01023450001, "서울시 강남구 역삼동 111-333", 20201102, 130258, 35000, 0003);
		
		System.out.println(order.orderNumber);
	}

}
