package com.jpa.fedeleo.bookmanager.repository;


import com.jpa.fedeleo.bookmanager.domain.UserHistory;
import com.jpa.fedeleo.bookmanager.domain.UserTable;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface UserHistoryRepository extends JpaRepository<UserHistory, Long> {
    // 기본적으로 제공하지 않기 때문에 쿼리메서드를 직접 작성
    List<UserHistory> findByUserId(Long userId);
}
