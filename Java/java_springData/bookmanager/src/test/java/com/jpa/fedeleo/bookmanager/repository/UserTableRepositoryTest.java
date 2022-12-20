package com.jpa.fedeleo.bookmanager.repository;

import com.jpa.fedeleo.bookmanager.domain.UserTable;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.data.domain.Example;
import org.springframework.data.domain.ExampleMatcher;

import static org.springframework.data.domain.ExampleMatcher.GenericPropertyMatchers.*;


@SpringBootTest
class UserTableRepositoryTest {

    @Autowired
    private UserTableRepository userTableRepository;

    @Test
    void crud(){

        userTableRepository.save(new UserTable("david", "david@fastcumpus.com"));

        UserTable user = userTableRepository.findById(1L).orElse(null);
        user.setEmail("martin-updated@fastcampus.com");
        userTableRepository.save(user);
    }

    @Test
    void select(){
        System.out.println(userTableRepository.findByName("dennis"));

        System.out.println("findByEmail : " + userTableRepository.findByEmail("martin@fastcampus.com"));
        System.out.println("getByEmail : " + userTableRepository.getByEmail("martin@fastcampus.com"));
        System.out.println("searchByEmail : " + userTableRepository.searchByEmail("martin@fastcampus.com"));
        System.out.println("readByEmail : " + userTableRepository.readByEmail("martin@fastcampus.com"));
        System.out.println("queryByEmail : " + userTableRepository.queryByEmail("martin@fastcampus.com"));
        System.out.println("streamByEmail : " + userTableRepository.streamByEmail("martin@fastcampus.com"));
        System.out.println("findUserByEmail : " + userTableRepository.findUserByEmail("martin@fastcampus.com"));
    }
}