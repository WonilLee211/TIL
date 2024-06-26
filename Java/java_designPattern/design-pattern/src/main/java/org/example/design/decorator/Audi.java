package org.example.design.decorator;

public class Audi implements ICar{

    private int cost;

    public Audi(int cost){ this.cost = cost; }

    @Override
    public int getPrice() {
        return cost;
    }

    @Override
    public void showCost() {
        System.out.println("Audi Base는 "+cost+" 원 입니다.");
    }
}
