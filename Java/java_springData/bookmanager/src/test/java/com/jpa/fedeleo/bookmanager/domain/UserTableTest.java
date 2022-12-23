package com.jpa.fedeleo.bookmanager.domain;

import java.time.LocalDateTime;


class UserTableTest {

//    @Test
    void test(){

        UserTable userTable = new UserTable();
        userTable.setName("martin");
        userTable.setEmail("martin@naver.com");
        userTable.setCreatedAt(LocalDateTime.now());
        userTable.setUpdatedAt(LocalDateTime.now());

//        UserTable userTable1 = new UserTable(null, "martin", "martin@naver.com", LocalDateTime.now(), LocalDateTime.now());
        UserTable userTable2 = new UserTable("martin", "martin@naver.com");

        UserTable userTable3 = UserTable.builder()
                .name("martin")
                .email("martin@naver.com")
                .build();
        System.out.println(">>>" + userTable.toString());
    }


}