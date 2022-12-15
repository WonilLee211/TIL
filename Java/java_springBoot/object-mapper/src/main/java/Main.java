import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ArrayNode;
import com.fasterxml.jackson.databind.node.ObjectNode;
import dto.Car;
import dto.User;

import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.List;

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

        // 지금까지 기본적인 objectmapper 사용법

        // 이제 JsonNode에 직접 접근하여 조작하기
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
        // 아무 것도 안찍힘

        // 이미 json 표준 스펙을 알 떄 parsing 방법
        JsonNode cars = jsonNode.get("cars");
        ArrayNode arrayNode = (ArrayNode)cars; // ArrayNode : value가 Array 타입일 때
        // objectMapper.convertValue : json이 아닌 우리가 원하는 클래스로 맵핑시키기
        List<Car> _cars = objectMapper.convertValue(arrayNode, new TypeReference<List<Car>>(){});
        System.out.println(_cars);
//        [Car{name='K5', carNumber='11가 1111', type='sedan'}, Car{name='Q5', carNumber='22가 2222', type='SUV'}]

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
