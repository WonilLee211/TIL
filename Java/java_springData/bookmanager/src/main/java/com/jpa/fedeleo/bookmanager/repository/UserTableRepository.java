package com.jpa.fedeleo.bookmanager.repository;

import com.jpa.fedeleo.bookmanager.domain.UserTable;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Sort;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.JpaSpecificationExecutor;
import org.springframework.data.jpa.repository.Query;

import java.time.LocalDateTime;
import java.util.List;
import java.util.Map;
import java.util.Set;

public interface UserTableRepository extends JpaRepository<UserTable, Long> {
//    List<UserTable> findByName(String name);

//    UserTable findByEmail(String email);
//    UserTable getByEmail(String email);
//    UserTable readByEmail(String email);
//    UserTable queryByEmail(String email);
//    UserTable searchByEmail(String email);
//    UserTable streamByEmail(String email);
//    UserTable findUserByEmail(String email);

//    UserTable findFirstByName(String name);
//    UserTable findTopByName(String name);

//    List<UserTable> findFirst2ByName(String name);
//    List<UserTable> findTop2ByName(String name);

//    List<UserTable> findByEmailAndName(String email, String name);
//    List<UserTable> findByEmailOrName(String email, String name);

//    List<UserTable> findByCreatedAtAfter(LocalDateTime yesterday);
//    List<UserTable> findByIdAfter(Long id);

//    List<UserTable> findByCreatedAtGreaterThan(LocalDateTime yesterday);
//    List<UserTable> findByIdGreaterThan(Long id);
//    List<UserTable> findByIdGreaterThanEqual(Long id);

//    List<UserTable> findByCreatedAtBetween(LocalDateTime yesterday, LocalDateTime tomorrow);
//    List<UserTable> findByIdBetween(Long id1, Long id2);

//    List<UserTable> findByIdIsNotNull();
//    List<UserTable> findByAddressIsNotEmpty();

//    List<UserTable> findByNameIn(List<String> names);

//    List<UserTable> findByNameStartingWith(String name);
//    List<UserTable> findByNameEndingWith(String name);
//    List<UserTable> findByNameContains(String name);
//    List<UserTable> findByNameLike(String name);

//    Set<UserTable> findUserByNameIs(String name);
//    Set<UserTable> findUserByName(String name);
//    Set<UserTable> findUserByNameEquals(String name);

//    List<UserTable> findTop1ByName(String name);
//    List<UserTable> findTop1ByNameOrderByIdDesc(String name);
//    List<UserTable> findFirstByNameOrderByIdDescEmailAsc(String name);
//    List<UserTable> findByName(String name, Sort sort);
//    Page<UserTable> findByName(String name, Pageable pageable);
//    @Query(value="select * from user_table limit 1", nativeQuery = true)
//    Map<String, Object> findRawRecord();

    List<UserTable> findByEmail(String email);

}
