package com.jpa.fedeleo.bookmanager.service;

import com.jpa.fedeleo.bookmanager.domain.UserTable;
import org.springframework.stereotype.Service;

@Service
public class UserService {
    public void put(){
        UserTable user = new UserTable();
        user.setName("newUser");
        user.setEmail("newUser@fastcampus.com");

    }
}
