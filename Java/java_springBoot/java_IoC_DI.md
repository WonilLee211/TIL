# IoC / DI

## IoC (Inversion of Control) 

- 스프링에서는 일반적인 Java 객체를 new로 생성하여 개발자가 관리 하는 것이 아닌 **Spring Container**에 모두 맡긴다.
- 즉, 개발자에서 -> 프레임워크로 **제어의 객체 관리의 권한이 넘어 갔음** 으로 `“제어의 역전”` 이라고 합니다.

## DI(Dependency Injection)

### 장점

- 의존성으로부터 격리시켜 코드 테스트에 용이하다.
- 이를 통하여, 불가능한 상황을 Mock와 같은 기술을 통하여, 안정적으로 테스트 가능하다. 
- 코드를 확장하거나 변경 할 때 영향을 최소화 한다 추상화)
- 순환참조를 막을 수 있다.


## 실습 - encode

```java

package org.example.ioc;

import java.util.Base64;

public class Encoder {

    public String encode(String message){
        return Base64.getEncoder().encodeToString(message.getBytes());
    }
}

```
```java
package org.example.ioc;

public class Main {
    public static void main(String[] args) {
        String url = "www.naver.com/books/it?page=10&size=20&name=spring-boot";

        //Base 64 encoding
        Encoder encoder = new Encoder();
        String result = encoder.encode(url);
        System.out.println(result);
//        d3d3Lm5hdmVyLmNvbS9ib29rcy9pdD9wYWdlPTEwJnNpemU9MjAmbmFtZT1zcHJpbmctYm9vdA==

    }
}
```

### DI 적용 전

-  url encoding 적용

```java
package org.example.ioc;

import java.io.UnsupportedEncodingException;
import java.net.URLEncoder;

public class UrlEncoder {

    public String encode(String message){
        try {
            return URLEncoder.encode(message, "UTF-8");
        } catch (UnsupportedEncodingException e) {
            e.printStackTrace();
            return null;
        }
    }
}
```
```java
package org.example.ioc;

public class Main {
    public static void main(String[] args) {
        String url = "www.naver.com/books/it?page=10&size=20&name=spring-boot";

        //Base 64 encoding
        Encoder encoder = new Encoder();
        String result = encoder.encode(url);
        System.out.println(result);
//        d3d3Lm5hdmVyLmNvbS9ib29rcy9pdD9wYWdlPTEwJnNpemU9MjAmbmFtZT1zcHJpbmctYm9vdA==

        // url encoding
        UrlEncoder urlEncoder = new UrlEncoder();
        String urlResult = urlEncoder.encode(url);

        System.out.println(urlResult);
        // www.naver.com%2Fbooks%2Fit%3Fpage%3D10%26size%3D20%26name%3Dspring-boot


    }
}
```

### interface 생성
  
```java
package org.example.ioc;

public interface IEncoder {
    
    String encode(String message);
}

```
```java
package org.example.ioc;

public class Main {
    public static void main(String[] args) {
        String url = "www.naver.com/books/it?page=10&size=20&name=spring-boot";

        //Base 64 encoding
        IEncoder encoder = new Base64Encoder();
        String result = encoder.encode(url);

        // url encoding
        IEncoder urlEncoder = new UrlEncoder();
        String urlResult = urlEncoder.encode(url);

    }
}

```
- 캡슐화

```java
package org.example.ioc;

public class Encoder {
    private IEncoder iEncoder;

    public Encoder(){
        //this.iEncoder = new Base64Encoder();
        this.iEncoder = new UrlEncoder();
    }
    public String encode(String message){
        return iEncoder.encode(message);
    }
}
// ___--------------------------------------------

package org.example.ioc;

public class Main {
    public static void main(String[] args) {
        String url = "www.naver.com/books/it?page=10&size=20&name=spring-boot";

        Encoder encoder = new Encoder();
        String result = encoder.encode(url);
        System.out.println(result);

    }
}
```

- 테스트마다 Encoder 클래스 생성자 내부를 수정해야하는 비효율적인 코드

### DI 적용

- 외부에서 사용하는 객체(의존있는 것)를 주입받음
  
```java
package org.example.ioc;

public class Encoder {
    private IEncoder iEncoder;

    public Encoder(IEncoder iEncoder){ // 외부에서 사용하는 객체를 주입받음

        this.iEncoder = iEncoder;
    }
    public String encode(String message){
        return iEncoder.encode(message);
    }
}

```
```java

package org.example.ioc;

public class Main {
    public static void main(String[] args) {
        String url = "www.naver.com/books/it?page=10&size=20&name=spring-boot";

        // Encoder encoder = new Encoder(new UrlEncoder());
        Encoder encoder = new Encoder(new Base64Encoder());
        String result = encoder.encode(url);
        System.out.println(result);

    }
}

```

## IOC, Spring Container에서 DI

- `@Component` : 클래스를 spring bean으로 등록됨
  - 빈이라고 불리는 자바 객체로 취급하여 관리
  - Spring이 실행되면 spring bean을 찾아서 싱글톤 형태로 만들어서 관리함

- ApplicationContextAware 
  - @Component선언된 객체를 관리할 권한을 넘겨 받는 인터페이스
  - IOC
```java
package com.example.springioc;

import org.springframework.beans.BeansException;
import org.springframework.context.ApplicationContext;
import org.springframework.context.ApplicationContextAware;
import org.springframework.stereotype.Component;

@Component
public class ApplicationContextProvider implements ApplicationContextAware {

    private static ApplicationContext context;

    @Override
    public void setApplicationContext(ApplicationContext applicationContext) throws BeansException {
        context = applicationContext;

    }

    public static ApplicationContext getContext(){
        return context;
    }
}

```

```java
package com.example.springioc;

import org.springframework.stereotype.Component;

import java.util.Base64;

@Component
public class Base64Encoder implements IEncoder{

    public String encode(String message){
        return Base64.getEncoder().encodeToString(message.getBytes());
    }
}
//-------------------------------------------
package com.example.springioc;

import org.springframework.stereotype.Component;

import java.io.UnsupportedEncodingException;
import java.net.URLEncoder;

@Component
public class UrlEncoder implements IEncoder{

    public String encode(String message){
        try {
            return URLEncoder.encode(message, "UTF-8");
        } catch (UnsupportedEncodingException e) {
            e.printStackTrace();
            return null;
        }
    }
}
//-------------------------------------------

```

```java
package com.example.springioc;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ApplicationContext;

import java.util.Base64;

@SpringBootApplication
public class SpringIocApplication {

	public static void main(String[] args) {
		SpringApplication.run(SpringIocApplication.class, args);

		ApplicationContext context = ApplicationContextProvider.getContext();

		Base64Encoder base64Encoder = context.getBean(Base64Encoder.class);
		UrlEncoder urlEncoder = context.getBean(UrlEncoder.class);

		Encoder encoder = new Encoder(base64Encoder);

		String url = "www.naver.com/books/it?page=10&size=20&name=spring-boot";

		String result = encoder.encode(url);
		System.out.println(result);
		// d3d3Lm5hdmVyLmNvbS9ib29rcy9pdD9wYWdlPTEwJnNpemU9MjAmbmFtZT1zcHJpbmctYm9vdA==

		encoder.setIEncoder(urlEncoder);
		result = encoder.encode(url);
		System.out.println(result);
		// www.naver.com%2Fbooks%2Fit%3Fpage%3D10%26size%3D20%26name%3Dspring-boot
	}

}

```

### default 객체 정하기

- EnCoder도 bean으로 넘기기
  - 에러 발생
  - Bean이 하나 이상일 때 매칭시키지 못함
  - `@Qualifier("beanName")` : 매칭할 Default bean을 선언해줌


```java
package com.example.springioc;

import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Component;

@Component
public class Encoder {
    private IEncoder iEncoder;

    public Encoder(@Qualifier("base64Encoder") IEncoder iEncoder){

        this.iEncoder = iEncoder;
}

    public void setIEncoder(IEncoder iEncoder){
        this.iEncoder = iEncoder;
    }

    public String encode(String message){
        return iEncoder.encode(message);
    }
}


```

-  bean이름 변경하기
    - `@Component("changedBeanName")`
  
```java
package com.example.springioc;

import org.springframework.stereotype.Component;

import java.util.Base64;

@Component("base74Encoder")
public class Base64Encoder implements IEncoder{

    public String encode(String message){
        return Base64.getEncoder().encodeToString(message.getBytes());
    }
}

```

```java
package com.example.springioc;

import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Component;

@Component
public class Encoder {
    private IEncoder iEncoder;

    public Encoder(@Qualifier("base74Encoder") IEncoder iEncoder){

        this.iEncoder = iEncoder;
}

    public void setIEncoder(IEncoder iEncoder){
        this.iEncoder = iEncoder;
    }

    public String encode(String message){
        return iEncoder.encode(message);
    }
}
```

- 객체 전달에 있어 완전 독립됨
- 스프링에서 모든 객체의 생명 주기가 관리됨

```java
package com.example.springioc;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ApplicationContext;

import java.util.Base64;

@SpringBootApplication
public class SpringIocApplication {

	public static void main(String[] args) {
		SpringApplication.run(SpringIocApplication.class, args);
		ApplicationContext context = ApplicationContextProvider.getContext();

//		Base64Encoder base64Encoder = context.getBean(Base64Encoder.class);
//		UrlEncoder urlEncoder = context.getBean(UrlEncoder.class);

		Encoder encoder = context.getBean(Encoder.class);
		String url = "www.naver.com/books/it?page=10&size=20&name=spring-boot";
		String result = encoder.encode(url);
		System.out.println(result);
	}

}

```

### 여러 Bean 사용하기

- `@Configuration`
  - 한개의 클래스에서 여러 개의 빈을 등록한다는 의미
  
- `@Bean("customizedBeanName")`
  - bean 인식할 이름 설정 

```java
package com.example.springioc;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.util.Base64;

@SpringBootApplication
public class SpringIocApplication {

	public static void main(String[] args) {
		SpringApplication.run(SpringIocApplication.class, args);
		ApplicationContext context = ApplicationContextProvider.getContext();

//		Base64Encoder base64Encoder = context.getBean(Base64Encoder.class);
//		UrlEncoder urlEncoder = context.getBean(UrlEncoder.class);

		Encoder encoder = context.getBean("urlEncode", Encoder.class);
		String url = "www.naver.com/books/it?page=10&size=20&name=spring-boot";
		String result = encoder.encode(url);
		System.out.println(result);
	}

}

@Configuration // 한개의 클래스에서 여러 개의 빈을 등록한다는 의미
class AppConfig{

	@Bean("base64Encode")
	public Encoder encoder(Base64Encoder base64Encoder){
		return new Encoder(base64Encoder);
	}
	@Bean("urlEncode")
	public Encoder encoder(UrlEncoder urlEncoder){
		return new Encoder(urlEncoder);
	}

}
```


- 이러한 방식으로  IOC/ DI 발생