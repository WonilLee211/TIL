package org.example.repository;

import org.example.model.TodoEntity;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

// 제네릭 타입으로 TodoEntity로 설정하고 해당 Id타입을 입력
@Repository
public interface TodoRepository extends JpaRepository<TodoEntity, Long> {


}
