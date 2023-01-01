# Object Mapper

중요한 기능

1. "Java Object" =Serialize=> "JSON"
2. "JSON" =Deserialize=> "Java Object"

## 1. object -> text

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

## 2. text -> object

- `objectMapper.readValue([text], Class.class)`

```java
package com.example.objectmapper;

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

//        User{name='steve', age=20}
```

> ### 주의
> 
> 작성한 class가 ObjectMapper에 사용될 경우, method명에 get 메소드 외에 메소드의 이름에 get을 포함하지 않아야 한다.

## JsonProperty - ObjectMapper

```java
package com.example.objectmapper;

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


## 3. Advanced Features

- 위에서 설명한 Jackson Library의 Basic Features에 추가적으로 유용한 기능
- JSON과 Object에 대해서 **커스터마이징한 Serialize/Deserialize가 가능한 기능**

### 3.1. Configuring Serialization or Deserialization Feature

- 3.1.1. JSON에는 있지만 Mapping될 Object에는 없는 필드를 무시해야하는 경우
```java

String json = "{\"name\":\"Ryan\",\"age\":30,\"sex\":\"M\"}";
// User Object에서는 "sex" field가 없습니다. 아래 설정을 안하게되면 익셉션이 발생합니다.
objectMapper.configure(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, false);
User user = objectMapper.readValue(json, User.class);
```

- 3.1.2. JSON에 있는 propety가 Mapping될 Object에 primitive인데 null 값이 전달을 무시해야하는 경우

```java
String json = "{\"name\":\"Ryan\",\"age\":null}";
// 기본적으로 FAIL_ON_NULL_FOR_PRIMITIVES 옵션은 false 상태입니다. 의도적으로 옵션을 설정해주었습니다.
// 옵션이 true가 되게되면, age가 int인 primitive 자료형이 null인 JSON이 전달되는 경우 익셉션을 발생합니다.
objectMapper.configure(DeserializationFeature.FAIL_ON_NULL_FOR_PRIMITIVES, false);
User user = objectMapper.readValue(json, User.class);
```

### 3.2. Creating Custom Serializer or Deserializer

- Object이 JSON으로 Serialize될 때, 서로 다른 정보로 전달되고 있는데 Object나 JSON이 전달하는 모델을 변경하지 못하는 경우,
    - "Custom Serializer"를 사용

- JSON이 Object로 Deserialize될 때, 서로 다른 정보로 전달되고 있는데 Object나 JSON이 전달하는 모델을 변경하지 못하는 경우,
    - "Custom Deserializer"를 사용


```java
class User {
    private final int age;
	
    User(int age) {
    	this.age = age;
    }
}
```

- 3.2.1. Custom Serializer Example : "Object" =Custom Serialize=> "JSON"

```java
public class CustomUserSerializer extends StdSerializer<Car> {
    public CustomUserSerializer() {
        this(null);
    }

    public CustomUserSerializer(Class<Car> t) {
        super(t);
    }

    @Override
    public void serialize(Car car, JsonGenerator jsonGenerator, SerializerProvider serializer) {
        jsonGenerator.writeStartObject();
        jsonGenerator.writeStringField("user_age", user.getAge());
        jsonGenerator.writeEndObject();
    }
}
```
```java
ObjectMapper mapper = new ObjectMapper();
SimpleModule module = new SimpleModule("CustomUserSerializer", new Version(1, 0, 0, null, null, null));
module.addSerializer(User.class, new CustomUserSerializer());
mapper.registerModule(module);
User user = new User(20);
String userJson = mapper.writeValueAsString(user);
System.out.println(userJson);// {"user_age":20}
```

3.2.2. Custom Deserializer Example : "JSON" => Custom Deserialize=> "Object"

```java
public class CustomUserDeserializer extends StdDeserializer<User> {
    public CustomUserDeserializer() {
        this(null);
    }

    public CustomUserDeserializer(Class<?> vc) {
        super(vc);
    }

    @Override
    public User deserialize(JsonParser parser, DeserializationContext deserializer) {
        User user = new User();
        ObjectCodec codec = parser.getCodec();
        JsonNode node = codec.readTree(parser);
        
        // try catch block
        JsonNode ageNode = node.get("user_age");
        String age = ageNode.asText();
        user.setAge(age);
        return user;
    }
}

```
```java
String json = "{ \"user_age\" : 30}";
ObjectMapper mapper = new ObjectMapper();
SimpleModule module = new SimpleModule("CustomUserDeserializer", new Version(1, 0, 0, null, null, null));
module.addDeserializer(User.class, new CustomUserDeserializer());
mapper.registerModule(module);
User user = mapper.readValue(json, User.class);
```

### 3.3. Handling Date Formats

- Serialize를 하는 과정에서 Date로 구성된 Object field의 Format을 변경할 수 있음
```java
class User {
    private int age;
    private Date createdAt;

    // getters, setters
}
```

```java
User user = new User();
user.setAge(30);
user.setCreatedAt(Date.from(Instant.now()));

ObjectMapper objectMapper = new ObjectMapper();
DateFormat df = new SimpleDateFormat("yyyy-MM-dd HH:mm a z");
objectMapper.setDateFormat(df);
String userAsString = objectMapper.writeValueAsString(user);
System.out.println(userAsString);// {"age":30,"createdAt":"2021-06-10 11:43 AM CEST"}
```

### 3.4. Handling Collections

- JSON에 존재하는 복수개의 모델을 Collections 자료형으로 Deserialize
    - Deserialize JSON to Array
```java
String jsonUserArray = "[{\"age\":30,\"createdAt\":\"2021-06-10T11:43:12\"},{\"age\":30,\"createdAt\":\"2021-06-10T11:43:12\"}]";
ObjectMapper objectMapper = new ObjectMapper();
objectMapper.configure(DeserializationFeature.USE_JAVA_ARRAY_FOR_JSON_ARRAY, true);
User[] users = objectMapper.readValue(jsonCarArray, User[].class);
// print users
또는 Deserialize JSON to List

String jsonUserArray = "[{\"age\":30,\"createdAt\":\"2021-06-10T11:43:12\"},{\"age\":30,\"createdAt\":\"2021-06-10T11:43:12\"}]";
ObjectMapper objectMapper = new ObjectMapper();
List<User> listUser = objectMapper.readValue(jsonCarArray, new TypeReference<List<User>>(){});
// print users
```

<h6> 참조 :https://interconnection.tistory.com/137 </h6>