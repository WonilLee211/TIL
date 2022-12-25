package com.jpa.fedeleo.bookmanager.domain.listener;

import com.jpa.fedeleo.bookmanager.domain.UserHistory;
import com.jpa.fedeleo.bookmanager.domain.UserTable;
import com.jpa.fedeleo.bookmanager.repository.UserHistoryRepository;
import com.jpa.fedeleo.bookmanager.support.BeanUtils;

import javax.persistence.PostPersist;
import javax.persistence.PostUpdate;

//@Component
public class UserEntityListener {

//    @Autowired
//    private UserHistoryRepository userHistoryRepository;

    @PostPersist
    @PostUpdate
    public void prePersistAndPreUpdate(Object o){
        UserHistoryRepository userHistoryRepository = BeanUtils.getBean(UserHistoryRepository.class);
        UserTable user = (UserTable) o;
        UserHistory userHistory = new UserHistory();
        userHistory.setName(user.getName());
        userHistory.setEmail(user.getEmail());
        userHistory.setUser(user);

        userHistoryRepository.save(userHistory);

    }
}
