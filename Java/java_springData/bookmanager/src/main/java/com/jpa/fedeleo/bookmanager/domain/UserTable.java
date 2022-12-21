package com.jpa.fedeleo.bookmanager.domain;

import lombok.*;

import javax.persistence.*;
import java.time.LocalDateTime;
import java.util.List;

@Data
@Entity // 객체를 entity로 선언. 내부에 primaery key 선언이 필수
@Builder
@NoArgsConstructor
@AllArgsConstructor
@RequiredArgsConstructor
@Table(indexes = {@Index(columnList = "name")}, uniqueConstraints = {@UniqueConstraint(columnNames = {"email"})})
public class UserTable {

    @Id // pk
    @GeneratedValue // autoincrement,
    private Long id;
    @NonNull
    private String name;
    @NonNull
    private String email;
    @Column
    private LocalDateTime createdAt;
    private LocalDateTime updatedAt;

//    @OneToMany(fetch= FetchType.EAGER)
//    private List<Address> address;


}
