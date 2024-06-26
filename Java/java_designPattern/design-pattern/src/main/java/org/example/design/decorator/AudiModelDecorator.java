package org.example.design.decorator;

public class AudiModelDecorator implements ICar{

    protected ICar audi;
    protected int modelPrice;

    public AudiModelDecorator(ICar audi){
        this.audi = audi;
    }

    @Override
    public int getPrice() {
        return audi.getPrice();
    }

    @Override
    public void showCost() {
        // audi base cost + Model cost
        System.out.println("가격은 "+(audi.getPrice() + modelPrice)+" 만원 입니다");
    }
}
