package com.jpa.fedeleo.bookmanager.repository;

import com.jpa.fedeleo.bookmanager.domain.UserTable;
import org.apache.catalina.User;
import org.assertj.core.util.Lists;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.data.domain.Sort;

import java.util.List;
import java.util.Optional;


@SpringBootTest
class UserTableRepositoryTest {

    @Autowired
    private UserTableRepository userTableRepository;

    @Test
    void crud(){

        Optional<UserTable> user = userTableRepository.findById(1L);

//        UserTable user = userTableRepository.findById(1L).orElse(null);

        System.out.println(user);

    }

}