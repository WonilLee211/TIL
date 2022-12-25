package com.jpa.fedeleo.bookmanager.repository;

import com.jpa.fedeleo.bookmanager.domain.Gender;
import com.jpa.fedeleo.bookmanager.domain.UserTable;
import org.assertj.core.util.Lists;
import org.hibernate.criterion.Order;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.data.domain.*;

import java.time.LocalDateTime;
import java.util.List;

import static org.springframework.data.domain.ExampleMatcher.GenericPropertyMatchers.*;


@SpringBootTest
class UserTableRepositoryTest {

    @Autowired
    private UserTableRepository userTableRepository;

    @Autowired
    private UserHistoryRepository userHistoryRepository;

    @Test
    void crud() {

//        userTableRepository.save(new UserTable("david", "david@fastcumpus.com"));

        UserTable user = userTableRepository.findById(1L).orElse(null);
        user.setEmail("martin-updated@fastcampus.com");
        userTableRepository.save(user);
    }

    @Test
    void select() {
//        System.out.println(userTableRepository.findByName("dennis"));
//
//        System.out.println("findByEmail : " + userTableRepository.findByEmail("martin@fastcampus.com"));
//        System.out.println("getByEmail : " + userTableRepository.getByEmail("martin@fastcampus.com"));
//        System.out.println("searchByEmail : " + userTableRepository.searchByEmail("martin@fastcampus.com"));
//        System.out.println("readByEmail : " + userTableRepository.readByEmail("martin@fastcampus.com"));
//        System.out.println("queryByEmail : " + userTableRepository.queryByEmail("martin@fastcampus.com"));
//        System.out.println("streamByEmail : " + userTableRepository.streamByEmail("martin@fastcampus.com"));
//        System.out.println("findUserByEmail : " + userTableRepository.findUserByEmail("martin@fastcampus.com"));
//
//        System.out.println("findFirstByName : " + userTableRepository.findFirstByName("martin"));
//        System.out.println("findTopByName : " + userTableRepository.findTopByName("martin"));

//        System.out.println("findFirst2ByName : " + userTableRepository.findFirst2ByName("martin"));
//        System.out.println("findTop2ByName : " + userTableRepository.findTop2ByName("martin"));

//        System.out.println("findByEmailAndName : " + userTableRepository.findByEmailAndName("martin@fastcampus.com", "martin"));
//        System.out.println("findByEmailOrName : " + userTableRepository.findByEmailOrName("martin@fastcampus.com", "dennis"));

//        System.out.println("findByCreatedAtAfter : " + userTableRepository.findByCreatedAtAfter(LocalDateTime.now()));
//        System.out.println("findByIdAfter : " + userTableRepository.findByIdAfter(4L));\

//        System.out.println("findByCreatedGreaterThan : " + userTableRepository.findByCreatedAtGreaterThan(LocalDateTime.now().minusDays(1L)));
//        System.out.println("findByIdGreaterThan : " + userTableRepository.findByIdGreaterThan(4L));
//        System.out.println("findByIdGreaterThanEqual : " + userTableRepository.findByIdGreaterThanEqual(4L));

//        System.out.println("findByCreatedBetween : " + userTableRepository.findByCreatedAtBetween(LocalDateTime.now().minusDays(1L), LocalDateTime.now().plusDays(1L)));
//        System.out.println("findByIdBetween : " + userTableRepository.findByIdBetween(1L, 3L));

//        System.out.println("findByIdIsNotNull : " + userTableRepository.findByIdIsNotNull());
//        System.out.println("findByIdIsNotEmpty : " + userTableRepository.findByAddressIsNotEmpty());

//        System.out.println("findByIdIn : " + userTableRepository.findByNameIn(Lists.newArrayList("martin", "dennis")));

//        System.out.println("findByNameStartingWith : " + userTableRepository.findByNameStartingWith("mar"));
//        System.out.println("findByNameEndingWith : " + userTableRepository.findByNameEndingWith("tin"));
//        System.out.println("findByNameContains : " + userTableRepository.findByNameContains("art"));
//        System.out.println("findByNameLike : " + userTableRepository.findByNameLike("%art%"));

//        System.out.println("findUserByNameIs : " + userTableRepository.findUserByNameIs("martin"));
//        System.out.println("findUserByName : " + userTableRepository.findUserByName("martin"));
//        System.out.println("findUserByNameEqual : " + userTableRepository.findUserByNameEquals("martin"));

    }

//    @Test
    void PagingSortingTest() {

//        System.out.println("findTop1ByName : " + userTableRepository.findTop1ByName("martin"));
//        System.out.println("findTop1ByNameOrderByIdDesc : " + userTableRepository.findTop1ByNameOrderByIdDesc("martin"));
//        System.out.println("findFirstByNameOrderByIdDescEmailAsc : " + userTableRepository.findFirstByNameOrderByIdDescEmailAsc("martin"));

//        System.out.println("findByName(String name, Sort sort) : " + userTableRepository.findByName("martin", Sort.by(Sort.Order.desc("id"))));
//        System.out.println("findByName(String name, Sort sort) : " + userTableRepository.findByName("martin", getSort()));
//        System.out.println("findByName(String name, Pageable pageable) : " + userTableRepository.findByName("martin", PageRequest.of(0, 1, Sort.by(Sort.Order.desc("id")))).getContent());

    }
    private Sort getSort(){
        return Sort.by(
                Sort.Order.desc("id"),
                Sort.Order.asc("email"),
                Sort.Order.desc("createdAt"),
                Sort.Order.asc("updatedAt")

        );
    }

    @Test
    void insertAndUpdateTest(){
        UserTable user = new UserTable();
        user.setName("martin");
        user.setEmail("martin@fastcampus1.com");

        userTableRepository.save(user);

        UserTable user2 = userTableRepository.findById(1L).orElseThrow(RuntimeException::new);
        user2.setName("marrrrin");

        userTableRepository.save(user2);

    }

    @Test
    void EnumTest(){
        UserTable user = userTableRepository.findById(1L).orElseThrow(RuntimeException::new);
        user.setGender(Gender.MALE);
        userTableRepository.save(user);

        userTableRepository.findAll().forEach(System.out::println);

//        System.out.println(userTableRepository.findRawRecord().get("gender"));
    }

    @Test
    void Listener(){
        UserTable user = new UserTable();
        user.setName("martin");
        user.setEmail("martin@naver.com");

        userTableRepository.save(user);

        UserTable user2 = userTableRepository.findById(4L).orElseThrow(RuntimeException::new);
        user2.setName("marrrrrtin");

        userTableRepository.save(user2);
        userTableRepository.deleteById(4L);

    }

    @Test
    void prePersistTest(){
        UserTable user = new UserTable();
        user.setEmail("martin@fastcampus.com");
        user.setName("martin");

        userTableRepository.save(user);
        System.out.println(userTableRepository.findByEmail("martin@fastcampus.com"));
    }
    @Test
    void preUpdateTest(){
        UserTable user = userTableRepository.findById(1L).orElseThrow(RuntimeException::new);
        user.setName("marrrrin");

        userTableRepository.save(user);
        System.out.println(userTableRepository.findById(1L).orElseThrow(RuntimeException::new));

    }

    @Test
    void UserHistoryTest(){
        UserTable user = new UserTable();
        user.setEmail("martin-new@fastcampus.com");
        user.setName("martin-new");

        userTableRepository.save(user);

        user.setName("martin-new-new");
        userTableRepository.save(user);

        userHistoryRepository.findAll().forEach(System.out::println);
    }

    @Test
    void userRelationTest(){
        UserTable user = new UserTable();
//        user.setName("david");
//        user.setEmail("david@fastcampus.com");
//        user.setGender(Gender.MALE);

        userTableRepository.save(user);

//        userHistoryRepository.findAll().forEach(System.out::println);

    }
}
