package com.example.pjtrestaurant.db;


import java.util.List;
import java.util.Optional;

public interface MemoryDbRepositoryIfs<T> {

    Optional<T> findByid(int index); // 해당 값에 대해 옵셔널하게 반환. index값에 해당하는 엔티티를 찾아서 반환하는 메서드
    T save(T entity);
    void deleteById(int index);
    List<T> listAll();

}
