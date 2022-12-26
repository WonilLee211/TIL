package com.jpa.fedeleo.bookmanager.repository;

import com.jpa.fedeleo.bookmanager.domain.BookAndAuthor;
import org.springframework.data.jpa.repository.JpaRepository;

public interface BookAndAuthorRepository extends JpaRepository<BookAndAuthor, Long> {
}

