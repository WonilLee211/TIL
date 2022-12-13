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