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
		var user = new User("steve", 20, "010-1234-5678");
		var text = objectMapper.writeValueAsString(user);
		System.out.println(text);

		// text -> object
		var objectUser = objectMapper.readValue(text, User.class); // 생성자 오버로딩
		System.out.println(objectUser);
//		User{name='steve', age=20}

	}
}
