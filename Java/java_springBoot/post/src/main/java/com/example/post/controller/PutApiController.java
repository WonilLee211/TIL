package com.example.post.controller;

import com.example.post.dto.PutRequestDto;
import com.fasterxml.jackson.databind.annotation.JsonNaming;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api")
public class PutApiController {

    @PutMapping("/put/{userId}")
    public PutRequestDto put(@RequestBody PutRequestDto putRequestDto, @PathVariable(name="userId") Long id){
        System.out.println(id);
        return putRequestDto;
    }
//    PutRequestDto{name='steve', age=20, carList=[CarDto{name='BMW', carNumber='11가 1234'}, CarDto{name='A4', carNumber='22가 5678'}]}
//    @JsonNaming 적용
//    PutRequestDto{name='steve', age=20, carList=[CarDto{name='BMW', carNumber='11가 1234'}, CarDto{name='A4', carNumber='22가 5678'}]}

    // response 내리기 : return 하면 됨
//    {
//        "name": "steve",
//            "age": 20,
//            "car_list": [
//        {
//            "name": "BMW",
//                "car_number": "11가 1234"
//        },
//        {
//            "name": "A4",
//                "car_number": "22가 5678"
//        }
//    ]
//    }
}
