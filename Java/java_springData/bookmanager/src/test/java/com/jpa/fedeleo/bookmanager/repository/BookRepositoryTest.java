package com.jpa.fedeleo.bookmanager.repository;

import com.jpa.fedeleo.bookmanager.domain.Book;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
public class BookRepositoryTest {

    @Autowired
    private BookRepository bookRepository;

    @Test
    void BookTest(){
        Book book = new Book();
        book.setName("spring boot data");
        book.setAuthorId(1L);

        bookRepository.save(book);

        System.out.println(bookRepository.findAll() );

    }
}
