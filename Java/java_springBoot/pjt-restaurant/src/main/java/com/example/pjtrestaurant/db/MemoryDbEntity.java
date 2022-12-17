package com.example.pjtrestaurant.db;


import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

// 모든 데이터베이스를 가진 클래스는 MemoryDbEntity를 상속받도록 함

@Data
@AllArgsConstructor
@NoArgsConstructor
public class MemoryDbEntity {
    protected int index;
}
