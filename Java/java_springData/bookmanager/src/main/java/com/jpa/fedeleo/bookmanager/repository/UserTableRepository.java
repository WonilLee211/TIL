package com.jpa.fedeleo.bookmanager.repository;

import com.jpa.fedeleo.bookmanager.domain.UserTable;
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserTableRepository extends JpaRepository<UserTable, Long> {

}
