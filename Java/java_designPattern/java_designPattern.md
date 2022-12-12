# 디자인 패턴

- 자주 사용하는 설계 패턴을 정형화 해서 이를 유형별로 가장 최적의 방법으로 개발을 할 수 있도록 정해둔 설계 
- 알고리즘과 유사 하지만, 명확하게 정답이 있는 형태는 아니며, 프로젝트의 상황에 맞추어 적용 가능 하다.

## Gof 디자인 패턴

- 소프트웨어를 설계 할 때는 기존에 경험이 매우 중요하다. 그러나 모든 사람들이 다양한 경험을 가지고 있을 수는 없다.
- 이러한 지식을 공유하기 위해서 나온 것이 **GOF (Gang of Four) 의 디자인 패턴**이다. 
- **객체지향 개념에 따른 설계 중 재사용할 경우 유용한 설계를 디자인 패턴으로 정리 해둔 것**이다.
- Gof 의 디자인 패턴은 총 23개 이며, 이를 잘 이해하고 활용한다면, 경험이 부족하더라도 좋은 소프트웨어 설계가 가능하다.


## 디자인 패턴의 장점

>  개발자（설계자》간의원활한소통 
>  소프트웨어 구조 파악 용이
>  재사용을 통한 개발 시간 단축
>  설계 변경 요청에 대한 유연한 대처

## 디자인 패턴의 단점

> 객체지향설계/구현 
> 초기투자비용부담


## 1. 생성 패턴

- 객체를 생성하는 것과 관련된 패턴
- 객체의 생성과 변경이 전체 시스템에 미치는 영향을 최소화 하고, 코드의 유연성을 높여 준다.

>  Factory Method
>  **Singleton**
>  Prototype
>  **Builder**
>  Abstract Factory
>  **Chaining**


## 2. 구조 패턴

- 프로그램 내의 자료구조나 인터페이스 구조 등 프로그램 구조를 설계하는데 활용 될 수 있는 패턴 - 클래스, 객체들의 구성을 통해서 더 큰 구조를 만들 수 있게 해준다.
- 큰 규모의 시스템에서는 많은 클래스들이 서로 의존성을 가지게 되는데, 이런 복잡한 구조를 개발 하기 쉽게 만들어 주고, 유지 보수 하기 쉽게 만들어 준다.

> **Adapter**
> Composite 
> Bridge
> **Decorator**
> **Facade**
> Flyweight
> **Proxy**

## 3. 행위 패턴

- 반복적으로 사용되는 객체들의 상호작용을 패턴화한 것
- 클래스나 객체들이 상호작용하는 방법과 책임을 분산하는 방법을 제공 한다. 
- 행위 패턴은 행위 관련 패턴을 사용하여 독립적으로 일을 처리하고자 할 때 사용.
  
>  Template Method
>  Interpreter
>  Iterator
>  **Observer**
>  **Strategy**
>  Visitor
>  Chain of responsibility
>  Command
>  Mediator
>  State
>  Memento


---

## Singleton pattern

- Singleton 패턴은 어떠한 클래스（객체）가 유일하게 1개만 존재 할 때 사용한다.
- 이를 주로 사용하는 곳은 서로 자원을 공유 할 때 사용
- 실물 세계에서는 프린터가 해당
- 실제 프로그래밍에서는 TCP Socket 통신에서 서버와 연결된 connect 객체에 주로 사용

```java
package org.example.design.singleton;

public class SocketClient {

    private static SocketClient socketClient = null;
    // default 생성자 막기
    private SocketClient(){}

    public static SocketClient getInstance(){

        if(socketClient == null) {
            socketClient = new SocketClient();
            System.out.println("socket new instance");
        }
        return socketClient;
    }

    public void connect(){
        System.out.println("socket");
    }
}
// ---------------------------------------------

package org.example.design.singleton;

public class AClass {

    private SocketClient socketClient;

    public AClass() {
        this.socketClient = SocketClient.getInstance();
    }

    public SocketClient getSocketClient() {
        return socketClient;
    }

    public void setSocketClient(SocketClient socketClient){
        this.socketClient = socketClient;
    }
}

// --------------------------------------------------------

package org.example.design.singleton;

public class BClass {

    private SocketClient socketClient;

    public BClass() {
        this.socketClient = SocketClient.getInstance();
    }
    public SocketClient getSocketClient() {
        return socketClient;
    }
    public void setSocketClient(SocketClient socketClient){
        this.socketClient = socketClient;
    }
}


```

```java

package org.example;

import org.example.design.singleton.AClass;
import org.example.design.singleton.BClass;

public class Main {
    public static void main(String[] args) {

        AClass a = new AClass();
        BClass b = new BClass();

        System.out.println(a.getSocketClient().equals(b.getSocketClient()));
//        socket new instance
//        true

    }
}
```

## Adapter pattern

- 예) 실생활에서는 lOOv 를 220v로 변경해주거나, 그 반대로 해주는 흔히 돼지코 라고 불리는 변 환기.
- 호환성이 없는 기존 클래스의 인터페이스를 변환하여 재사용 할 수 있도록 한다. 
- SOLID중에서 개방폐쇄 원칙(OCP)을 따른다.

```java
package com.company.design.adapter;

public class SocketAdapter implements Electronic110V {

    private Electronic220V electronic220V;

    public SocketAdapter(Electronic220V electronic220V){
        this.electronic220V = electronic220V;
    }

    @Override
    public void powerOn() {
        electronic220V.connect();
    }
}

```

```java

package com.company.design.adapter;

public class Cleaner implements Electronic220V{
    @Override
    public void connect() {
        System.out.println("220v 청소기 ON");
    }
}
```

```java
package com.company.design.adapter;

public class HairDryer implements Electronic110V {
    @Override
    public void powerOn() {
        System.out.println("110v 헤어드라이기 ON");
    }
}

```
```java
package org.example;

import org.example.design.adapter.*;

public class Main {
    public static void connect(Electronic110V electronic110V){
        electronic110V.powerOn();
    }

    public static void main(String[] args) {

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


    }
}

```

## Proxy Pattern

- Proxy는 대리인 이라는 뜻으로써, 뭔가를 대신해서 처리하는 것
- Proxy Class를 통해서 대신 전달 하는 형태로 설계되며, 실제 Client는 Proxy 로 부터 결과를 받는다.
- Cache의 기능으로도 활용 가능
- SOLID중에 개방폐쇄원칙(OCP)과 의존 역전 원칙 (DIP)를 따른다.

```java
package com.company.design.proxy;

public class BrowserProxy implements IBrowser {

    private String url;
    private Html html;

    public BrowserProxy(String url){
        this.url = url;
    }

    @Override
    public Html show() {
        if(html == null){
            this.html = new Html(url);
            System.out.println("BrowserProxy loading html from "+url);
        }
        System.out.println("BrowserProxy use cache html");
        return html;
    }
}

```
```java
package org.example;

import org.example.design.proxy.BrowserProxy;
import org.example.design.proxy.IBrowser;

public class Main {

    public static void main(String[] args) {

        IBrowser Browser = new BrowserProxy("www.naver.com");
        Browser.show();
        Browser.show();
        
//        BrowserProxy loading html from www.naver.com
//        BrowserProxy use cache html
//        BrowserProxy use cache html

    }
}
```


## Decorator pattern

- 데코레이터 패턴은 기존 뼈대 (클래스)는 유지하되, 이후 필요한 형태로 꾸밀 때 사용한다.
- 확장이 필요한 경우 상속의 대안으로도 활용한다. 
- SOLID중에서 개방폐쇄 원칙 (OCP)과 의존 역전 원칙 (DIP)를 따른다.

- decorator pattern 사용하지 않은 사례
```java
package com.company.design.decorator;

public class Audi implements ICar{

    private int cost;

    public Audi(int cost){
        this.cost = cost;
    }

    @Override
    public int getPrice(){
        return this.cost;
    }

    @Override
    public void showCost() {
        System.out.println("Audi Base는 "+cost+" 원 입니다.");
    }
}

```

- decorator Pattern 사용한 사례
```java
package com.company.design.decorator;

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
        System.out.println("가격은 "+(audi.getPrice()+modelPrice)+" 만원 입니다");
    }
}

// ------------------------------------------------------------------------------
package com.company.design.decorator;

public class A3 extends AudiModelDecorator {

    public A3(ICar audi) {
        super(audi);
        this.modelPrice = 1000;
    }
}

```

```java
package org.example;

import org.example.design.decorator.*;

public class Main {

    public static void main(String[] args) {

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

    }
}

```

## Observer pattern

- 관찰자 패턴은 변화가 일어 났을 때, 미리 등록된 다른 클래스에 통보해주는 패턴을 구현한 것이다.
- 많이 보이는 곳은 event listener 에서 해당 패턴을 사용하고 있다.

```java
package com.company.design.observer;

public interface IButtonClickListener {
    void clickEvent(String event);
}

```

```java
package com.company.design.observer;

public class MyButton {
    private String name;
    private IButtonClickListener buttonClickListener;

    public MyButton(String buttonName){
        this.name = buttonName;
    }

    public void click(String clickEvent){
        buttonClickListener.clickEvent(this.name+", "+clickEvent);
    }

    public void addListener(IButtonClickListener buttonClickListener){
        this.buttonClickListener = buttonClickListener;
    }
}

```
```java
package org.example;

import org.example.design.observer.IButtonClickListener;
import org.example.design.observer.MyButton;

public class Main {

    public static void main(String[] args) {

        MyButton button = new MyButton("종료 버튼");
        IButtonClickListener listener = event -> System.out.println("click event : "+event);
        button.addListener(listener);

        button.click("한번 클릭");
        button.click("두번 클릭");
        button.click("세번 클릭");
//        click event : 종료 버튼, 한번 클릭
//        click event : 종료 버튼, 두번 클릭
//        click event : 종료 버튼, 세번 클릭

    }

```


## Facade pattern(?)
- Fagade는 건물의 앞쪽 정면 이라는 뜻을 가진다. 
- 여러 개의 객체와 실제 사용하는 서브 객체의 사이에 복잡한 의존간계가 있을 때, 중간에 facade 라는 객체를 두고, 여기서 제공하는 interface만을 활용하여 기능을 사용하는 방식이다.
-  Facade는 자신이 가지고 있는 각 클래스의 기능을 명확히 알아야 한다.

```java
package com.company.design.facade;

public class FtpProtocol {

    public FtpProtocol(String host, int port, String path){
        System.out.println("ftp server create");
    }


    public void connect(){
        System.out.println("ftp server connected");
    }

    public void moveDirectory(){
        System.out.println("move path");
    }

    public void disConnect(){
        System.out.println("ftp server disConnected");
    }
}
```

```java
package com.company.design.facade;

public class FileReader {

    public FileReader(String fileName){

    }

    public void fileConnect(){
        System.out.println("FileReader Connected");
    }

    public String fileRead(){
        return "content";
    }

    public void fileDisconnect(){
        System.out.println("FileReader disConnected");
    }
}
```

```java
package com.company.design.facade;

public class FileWriter {

    public FileWriter(String fileName){

    }

    public void fileConnect(){
        System.out.println("FileWriter Connected");
    }

    public void fileWrite(String content){
        System.out.println("write : "+content);
    }

    public void fileDisconnect(){
        System.out.println("FileWriter disConnected");
    }
}
```
- facade pattern class
```java
package com.company.design.facade;

public class SftpClient {

    private FtpProtocol ftpProtocol;
    private FileReader fileReader;
    private FileWriter fileWriter;

    public SftpClient(String host, int port, String path, String fileName){
        this.ftpProtocol = new FtpProtocol(host, port, path);
        this.fileReader = new FileReader(fileName);
        this.fileWriter = new FileWriter(fileName);
    }

    public void connect(){
        this.ftpProtocol.connect();
        this.ftpProtocol.moveDirectory();
        this.fileReader.fileConnect();
        this.fileWriter.fileConnect();

    }

    public void write(String content){
        this.fileWriter.fileWrite(content);
    }

    public String read(){
        return this.fileReader.fileRead();
    }

    public void disConnect(){
        this.fileReader.fileDisconnect();
        this.fileWriter.fileDisconnect();
        this.ftpProtocol.disConnect();
    }

}
```

```java
package org.example;

import org.example.design.facade.SftpClient;

public class Main {

    public static void main(String[] args) {

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
    }
}

```

## Strategy Pattern

- 전략 패턴으로 불리며, 객체지향의 꽃이다.
- 유사한 행위들을 캡슐화하여, 객체의 행위를 바꾸고 싶은 경우 직접 변경하는 것이 아닌 전략만 변경하여, 유연하게 확장 하는 패턴 
- SOLID 중에서 개방폐쇄 원칙 (OCP)과 의존 역전 원칙 (DIP)를 따른다.
- 전략 메서드를 가진 전략 객체 
  
  1. Normal Strategy
  2. Base64 Strategy 

- 전략 객채를 사용하는 컨텍스트
  -  Encoder
- 전략 객체를 생성해 컨텍스트에 주입하는 클라이언트


```java
package com.company.design.strategy;

public interface EncodingStrategy {
    String encoding(String message);
}
```

- encode 방식에 따라 각자 구현
```java
package com.company.design.strategy;

public class NormalStrategy implements EncodingStrategy{
    @Override
    public String encoding(String message) {
        return message;
    }
}

```

```java
package com.company.design.strategy;

import java.util.Base64;

public class Base64Strategy implements EncodingStrategy{
    @Override
    public String encoding(String message) {
        return Base64.getEncoder().encodeToString(message.getBytes());
    }
}

```

- 여러가지 encode 객체를 등록하여 사용
```java
package com.company.design.strategy;

public class Encoder {
    private EncodingStrategy encodingStrategy;

    public String getMessage(String message){
        return encodingStrategy.encoding(message);
    }

    public void setEncodingStrategy(EncodingStrategy encodingStrategy){
        this.encodingStrategy = encodingStrategy;
    }
}
```

```java

package org.example;

import org.example.design.strategy.Base64Strategy;
import org.example.design.strategy.Encoder;
import org.example.design.strategy.NormalStrategy;

public class Main {

    public static void main(String[] args) {

        Encoder base64Encoder = new Encoder();
        base64Encoder.setEncodingStrategy(new Base64Strategy());
        System.out.println(base64Encoder.getMessage("message"));

        Encoder normalEncoder = new Encoder();
        normalEncoder.setEncodingStrategy(new NormalStrategy());
        System.out.println(normalEncoder.getMessage("message"));

//        bWVzc2FnZQ==
//        message

    }
}
```


## AOP proxy

```java
package com.company.design.aop;

import com.company.design.proxy.Html;

public interface IAopBrowser {
    Html show() throws InterruptedException;
}


```
```java

package com.company.design.aop;

import com.company.design.proxy.Html;


public class AopProxy implements IAopBrowser {

    private String url;
    private Html html;
    private Runnable before;
    private Runnable after;

    public AopProxy(String url){
        this.url = url;
    }

    public AopProxy(String url, Runnable before,  Runnable after) {
        this.url = url;
        this.before = before;
        this.after = after;
    }

    @Override
    public Html show() throws InterruptedException {
        after.run();

        if(html == null){
            this.html = new Html(url);
            System.out.println("BrowserProxy loading html from "+url);
        }
        System.out.println("BrowserProxy use cache html");
        Thread.sleep(2000);
        before.run();
        return html;
    }
}

```
```java

package org.example;

import org.example.design.aop.AopProxy;
import org.example.design.aop.IAopBrowser;

import java.util.concurrent.atomic.AtomicLong;

public class Main {

    public static void main(String[] args) throws InterruptedException {

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
```