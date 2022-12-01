package ch06;

public class VIPCustomer extends Customer {
	private int agentID;
	double salesRatio;
	
	// super를 이용하여 상위 클래스의 생성자 명시적으로 호출
	public VIPCustomer(int customerID, String customerName, int agentID) {
			super(customerID, customerName);
			
			customerGrade = "VIP";
			bonusRatio = 0.05;
			salesRatio = 0.1;
			this.agentID = agentID;
			
	}

	
	public int getAgentID() {
		return agentID;
	}

	@Override
	public int calcPrice(int price) {
		bonusPoint += price * bonusRatio;
		return price - (int)(price * salesRatio);
	}
	
	//showCustomerInfo() 재정의
	@Override
	public String showCustomerInfo(){
			return super.showCustomerInfo() + " 담당 상담원 번호는 " + agentID + "입니다";  
	}


}
