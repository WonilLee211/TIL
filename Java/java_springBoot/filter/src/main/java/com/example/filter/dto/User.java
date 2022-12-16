package com.example.filter.dto;


import lombok.*;

// lombok library의 annotation
//@Setter
//@Getter
@Data // getter + setter + toString 메서드까지 overriding
@NoArgsConstructor
@AllArgsConstructor
public class User {

    private String name;
    private int age;

}
