package com.jpa.fedeleo.bookmanager.domain;

import com.jpa.fedeleo.bookmanager.domain.listener.Auditable;
import com.jpa.fedeleo.bookmanager.domain.listener.UserEntityListener;
import lombok.*;
import org.springframework.data.annotation.CreatedDate;
import org.springframework.data.annotation.LastModifiedDate;
import org.springframework.data.jpa.domain.support.AuditingEntityListener;

import javax.persistence.*;
import java.time.LocalDateTime;

@ToString(callSuper = true)
@EqualsAndHashCode(callSuper = true)
@Data
@Entity // 객체를 entity로 선언. 내부에 primaery key 선언이 필수
@Builder
@NoArgsConstructor
@AllArgsConstructor
@RequiredArgsConstructor
@EntityListeners(value = UserEntityListener.class)
public class UserTable extends BaseEntity{

    @Id // pk
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    @NonNull
    private String name;
    @NonNull
    private String email;
    @Enumerated(value = EnumType.STRING)
    private Gender gender;

}
