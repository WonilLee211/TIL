package com.jpa.fedeleo.bookmanager.repository;

import com.jpa.fedeleo.bookmanager.domain.UserTable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.JpaSpecificationExecutor;

import java.util.List;

public interface UserTableRepository extends JpaRepository<UserTable, Long> {
    List<UserTable> findByName(String name);

    UserTable findByEmail(String email);
    UserTable getByEmail(String email);
    UserTable readByEmail(String email);
    UserTable queryByEmail(String email);
    UserTable searchByEmail(String email);
    UserTable streamByEmail(String email);
    UserTable findUserByEmail(String email);

}
