package com.jpa.fedeleo.bookmanager.domain;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.time.LocalDateTime;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class User {
    private String name;
    private String email;
    private LocalDateTime createdAt;
    private LocalDateTime updatedAt;



}
