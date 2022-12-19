package com.jpa.fedeleo.bookmanager.domain;

import lombok.*;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import java.time.LocalDateTime;

@Data
@Entity // 객체를 entity로 선언. 내부에 primaery key 선언이 필수
@Builder
@NoArgsConstructor
@AllArgsConstructor
@RequiredArgsConstructor
public class UserTable {

    @Id // pk
    @GeneratedValue // autoincrement,
    private Long id;
    @NonNull
    private String name;
    @NonNull
    private String email;
    private LocalDateTime createdAt;
    private LocalDateTime updatedAt;

}
