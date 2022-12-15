# Object Mapper


## object -> text

- `objectsMapper.writeValueAsString([object])`

```java
package com.example.objectmapper;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
class ObjectMapperApplicationTests {

	// 1. ObjectMapper는 GET method를 참조함

	@Test
	void contextLoads() throws JsonProcessingException {
		System.out.println("hello");

		// Text Json -> Object
		// Object -> TextJson

		// controller req json(text) -> object
		//response object - json(text)

		var objectMapper = new ObjectMapper();

		// object -> text
        // object -> text 과정에서 objectMapper는 getMethod를 활용한다.
		var user = new User("steve", 20);
		var text = objectMapper.writeValueAsString(user);
		System.out.println(text);

		// text -> object


	}

}

```

 - 에러 발생


 1. ObjectMapper는 GET method를 참조함
   
```java

package com.example.objectmapper;

public class User {
    private String name;
    private int age;

    public User(String name, int age){
        this.name = name;
        this.age = age;
    }

    // 1. ObjectMapper는 GET method를 참조함
    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }

    @Override
    public String toString() {
        return "User{" +
                "name='" + name + '\'' +
                ", age=" + age +
                '}';
    }
}

// {"name":"steve","age":20}
```
- **object -> text 과정에서 objectMapper는 getMethod를 활용한다.**


## text -> object

- `objectMapper.readValue([text], Class.class)`

```java
package com.example.objectmapper;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
class ObjectMapperApplicationTests {

	// 1. ObjectMapper는 GET method를 참조함

	@Test
	void contextLoads() throws JsonProcessingException {
        ...
		// text -> object
		var objectUser = objectMapper.readValue(text, User.class); // 생성자 오버로딩
	}

}


```
- 에러 발생
- objectMapper는 text -> object 과정에서 **default생성자를 사용함**
  - default 생성자 선언하기


```java

package com.example.objectmapper;

public class User {
    private String name;
    private int age;

    // Default Constructor
    public User(){
        this.name = null;
        this.age = 0;
    }
    public User(String name, int age){
        this.name = name;
        this.age = age;
    }
    ...
}

//		User{name='steve', age=20}
```
> ### 주의
> 작성한 class가 ObjectMapper에 사용될 경우, method명에 get 메소드 외에 메소드의 이름에 get을 포함하지 않아야 한다.

## JsonProperty - ObjectMapper

```java
package com.example.objectmapper;

import com.fasterxml.jackson.annotation.JsonProperty;

public class User {
    ...

    @JsonProperty("phone_number")
    private String phoneNumber;

    public String getPhoneNumber() {
        return phoneNumber;
    }

    // Default Constructor
    public User(){
        this.name = null;
        this.age = 0;
        this.phoneNumber = null;
    }
    ...

    @Override
    public String toString() {
        return "User{" +
                "name='" + name + '\'' +
                ", age=" + age +
                ", phoneNumber='" + phoneNumber + '\'' +
                '}';
    }
}

// {"name":"steve","age":20,"phone_number":null} // snake-case
// User{name='steve', age=20, phoneNumber='null'} // camelCase
```


## object mapper로 Json node에 접근하기

### java library 활용

- maven repository >> Jackson Databind 2.12 버전 dependencies 추가
- 사용할 json 설계

```java
package dto;

import java.util.List;

public class User {
    private String name;
    private int age;
    private List<Car> cars;
    ...
}
// --------------------------
package dto;

import com.fasterxml.jackson.annotation.JsonProperty;

public class Car {
    private String name;

    @JsonProperty("car_number")
    private String carNumber;
    @JsonProperty("TYPE")
    private String type;
...

}

```

- 기존 objectMapper를 이용한 json 작성

```java

public class Main {

    public static void main(String[] args) throws JsonProcessingException {

        ObjectMapper objectMapper = new ObjectMapper();

        User user = new User();
        user.setName("Fideleo");
        user.setAge(28);

        Car car1 = new Car();
        car1.setName("K5");
        car1.setCarNumber("11가 1111");
        car1.setType("sedan");

        Car car2 = new Car();
        car2.setName("Q5");
        car2.setCarNumber("22가 2222");
        car2.setType("SUV");

        List<Car> carList = Arrays.asList(car1, car2);
        user.setCars(carList);

        System.out.println(user);

        String json = objectMapper.writeValueAsString(user);
        System.out.println(json);

        // 지금까지 objectmapper 이용한 json 작성
    }
}

```

### JsonNode에 직접 접근하여 json 조작하기

1. json parsing

   - `objectMapper.readTree()`
   - json 표준 스펙을 알 때 parsing 방법
     - `ArrayNode` : json 내 속성 값의 타입이 Array일 때 ArrayNode로 형변환
     - `objectMapper.convertValue(객체, new TypeReference<변경할 클래스타입>(){});` : 최종 형변환 완료



   
```java

public class Main {

    public static void main(String[] args) throws JsonProcessingException {

        ObjectMapper objectMapper = new ObjectMapper();

        // 1. json parsing

        JsonNode jsonNode = objectMapper.readTree(json);
        String _name = jsonNode.get("name").asText();
        int _age = jsonNode.get("age").asInt();

        System.out.println("name : " + _name);
        System.out.println("age : " + _age);
//        name : Fideleo
//        age : 28

//        String _list = jsonNode.get("cars").asText();
//        System.out.println(_list);
        // 타입이 맞지 않아 아무 것도 안찍힘

        // 이미 json 표준 스펙을 알 떄 parsing 방법
        JsonNode cars = jsonNode.get("cars");
        ArrayNode arrayNode = (ArrayNode)cars; // ArrayNode : value가 Array 타입일 때
        // objectMapper.convertValue : json이 아닌 우리가 원하는 클래스로 맵핑시키기
        List<Car> _cars = objectMapper.convertValue(arrayNode, new TypeReference<List<Car>>(){});
        System.out.println(_cars);
//        [Car{name='K5', carNumber='11가 1111', type='sedan'}, Car{name='Q5', carNumber='22가 2222', type='SUV'}]

    }
}


```


2. json 속성 값 변경하기

   - 기본적으로  ObjectMapper를 통해 직접 Json 내에 값을 변경할 수 없음
   - `ObjectNode`클래스 사용
     - `put()`, `set()`을 이용한 데이터 변경

```java

public class Main {

    public static void main(String[] args) throws JsonProcessingException {

        ObjectMapper objectMapper = new ObjectMapper();
        
        ...
        
        // 1. json parsing

        JsonNode jsonNode = objectMapper.readTree(json);
  
        // ObjectNode : 기본적으로 ObjectMapper로 Json값을 직접 변경하지 못함. 이를 해결하는 클래스
        ObjectNode objectNode = (ObjectNode)jsonNode;
        objectNode.put("name", "steve");
        objectNode.put("age", 20);
        

        System.out.println(objectNode.toPrettyString());
//        {
//            "name" : "steve",
//            "age" : 20,
//            "cars" : [ {
//                "name" : "K5",
//                        "car_number" : "11가 1111",
//                        "TYPE" : "sedan"
//                }, {
//                "name" : "Q5",
//                        "car_number" : "22가 2222",
//                        "TYPE" : "SUV"
//            } ]
//        }
        // Json 바디의 특정 값을 변경할 때 사용


    }
}

```
