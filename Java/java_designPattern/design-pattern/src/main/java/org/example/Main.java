package org.example;

import org.example.design.adapter.*;
import org.example.design.aop.AopProxy;
import org.example.design.aop.IAopBrowser;
import org.example.design.decorator.*;
import org.example.design.facade.SftpClient;
import org.example.design.observer.IButtonClickListener;
import org.example.design.observer.MyButton;
import org.example.design.proxy.BrowserProxy;
import org.example.design.proxy.IBrowser;
import org.example.design.singleton.AClass;
import org.example.design.singleton.BClass;
import org.example.design.strategy.Base64Strategy;
import org.example.design.strategy.Encoder;
import org.example.design.strategy.NormalStrategy;

import java.util.concurrent.atomic.AtomicLong;

public class Main {
    public static void connect(Electronic110V electronic110V){
        electronic110V.powerOn();
    }

    public static void main(String[] args) throws InterruptedException {

        AClass a = new AClass();
        BClass b = new BClass();

        System.out.println(a.getSocketClient().equals(b.getSocketClient()));
//        socket new instance
//        true

        HairDryer hairDryer = new HairDryer();
        connect(hairDryer);
//        110v 헤어드라이기 ON

        Cleaner cleaner = new Cleaner();
        AirConditioner airConditioner = new AirConditioner();

//        // Electronic220V 타입 이라 에러 발생
//        connect(cleaner);
//        connect(airConditioner);

        Electronic110V _cleaner = new SocketAdapter(cleaner);
        Electronic110V _airConditioner = new SocketAdapter(airConditioner);

        connect(_cleaner);
        connect(_airConditioner);
//        220v 청소기 ON
//        220v 에어컨 ON

        IBrowser Browser = new BrowserProxy("www.naver.com");
        Browser.show();
        Browser.show();

//        BrowserProxy loading html from www.naver.com
//        BrowserProxy use cache html
//        BrowserProxy use cache html

        ICar audi = new Audi(1000);
        audi.showCost();

        ICar audi3 = new A3(audi);
        audi3.showCost();

        ICar audi4 = new A4(audi);
        audi4.showCost();

        ICar audi5 = new A5(audi);
        audi5.showCost();
//        Audi Base는 1000 원 입니다.
//        가격은 2000 만원 입니다
//        가격은 3000 만원 입니다
//        가격은 4000 만원 입니다

        MyButton button = new MyButton("종료 버튼");
        IButtonClickListener listener = event -> System.out.println("click event : "+event);
        button.addListener(listener);

        button.click("한번 클릭");
        button.click("두번 클릭");
        button.click("세번 클릭");
//        click event : 종료 버튼, 한번 클릭
//        click event : 종료 버튼, 두번 클릭
//        click event : 종료 버튼, 세번 클릭


        SftpClient client = new SftpClient("www.google.com", 22, "/home/content", "content.tmp");
        client.connect();

        String content = "content";
        client.write(content);
        String result = client.read();
        System.out.println("----- 내용 : "+result+" -----");

        client.disConnect();

//        ftp server create
//        ftp server connected
//        move path
//        FileReader Connected
//        FileWriter Connected
//        write : content
//                ----- 내용 : content -----
//                FileReader disConnected
//        FileWriter disConnected
//        ftp server disConnected

        Encoder base64Encoder = new Encoder();
        base64Encoder.setEncodingStrategy(new Base64Strategy());
        System.out.println(base64Encoder.getMessage("message"));

        Encoder normalEncoder = new Encoder();
        normalEncoder.setEncodingStrategy(new NormalStrategy());
        System.out.println(normalEncoder.getMessage("message"));

//        bWVzc2FnZQ==
//        message

        AtomicLong startTime = new AtomicLong();
        AtomicLong endTime = new AtomicLong();
        IAopBrowser aopBrowser = new AopProxy(
                "www.google.com",
                () -> {
                    System.out.println("before");
                    startTime.set(System.currentTimeMillis());
                },
                () -> {
                    System.out.println("after");
                    endTime.set(System.currentTimeMillis() - startTime.get());
                }
        );
        aopBrowser.show();
        System.out.println(endTime + " ms");

//        after
//        BrowserProxy loading html from www.google.com
//        BrowserProxy use cache html
//        before
//        1670808595740 ms
    }
}