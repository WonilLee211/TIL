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
@EntityListeners(value = {MyEntityListener.class, UserEntityListener.class})
//@Table(indexes = {@Index(columnList = "name")}, uniqueConstraints = {@UniqueConstraint(columnNames = {"email"})})
public class UserTable implements Auditable{

    @Id // pk
    @GeneratedValue // autoincrement,
    private Long id;
    @NonNull
    private String name;
    @NonNull
    private String email;
    @Column(updatable = false)
    private LocalDateTime createdAt;
    @Column(insertable = false)
    private LocalDateTime updatedAt;
    @Enumerated(value = EnumType.STRING)
    private Gender gender;

//    @Transient
//    private String testData;

//    @OneToMany(fetch= FetchType.EAGER)
//    private List<Addres s> address;

//    @PrePersist
//    public void prePersist(){
//        this.createdAt = LocalDateTime.now();
//        this.updatedAt = LocalDateTime.now();
//
//    }
//
//    @PreUpdate
//    public void PreUpdate(){
//        this.updatedAt = LocalDateTime.now();
//    }

//    @PostPersist
//    public void postPersist(){
//        System.out.println(">>> postPersist");
//    }
//    @PostUpdate
//    public void PostUpdate(){
//        System.out.println(">>> PostUpdate");
//    }
//
//    @PreRemove
//    public void PreRemove(){
//        System.out.println(">>> PreRemove");
//    }
//
//    @PostRemove
//    public void PostRemove(){
//        System.out.println(">>> PostRemove");
//    }
//
//    @PostLoad
//    public void PostLoad(){
//        System.out.println(">>> PostLoad");
//    }

}
