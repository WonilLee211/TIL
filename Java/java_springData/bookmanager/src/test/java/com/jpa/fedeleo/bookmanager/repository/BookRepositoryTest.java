package com.jpa.fedeleo.bookmanager.repository;

import com.jpa.fedeleo.bookmanager.domain.Book;
import com.jpa.fedeleo.bookmanager.domain.Publisher;
import com.jpa.fedeleo.bookmanager.domain.Review;
import com.jpa.fedeleo.bookmanager.domain.UserTable;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.transaction.annotation.Transactional;

@SpringBootTest
public class BookRepositoryTest {

    @Autowired
    private BookRepository bookRepository;

    @Autowired
    private PublisherRepository publisherRepository;
    @Autowired
    private ReviewRepostory reviewRepostory;
    @Autowired
    private UserTableRepository userTableRepository;
    @Autowired
    private BookReviewInfoRepository bookReviewInfoRepository;

    @Test
    void BookTest(){
        Book book = new Book();
        book.setName("spring boot data");
//        book.setAuthorId(1L);

        bookRepository.save(book);

        System.out.println(bookRepository.findAll() );

    }

    @Test
    @Transactional // @OneToMany 필드 전체의 fetch 설정에서 FETCHTYPE을 EAGER 설정하지 않아도 됨
    void bookRelationTest(){
        givenBookAndReview();

        UserTable user = userTableRepository.findByEmail("martin@fastcampus.com");
        System.out.println("Review : " + user.getReviews());
        System.out.println("Book : " + user.getReviews().get(0).getBook());
        System.out.println("Publisher : " + user.getReviews().get(0).getBook().getPublisher());

    }

    @Test
     void bookCascadeTest(){
        Book book = new Book();
        book.setName("jpa cascade");

        Publisher publisher = new Publisher();
        publisher.setName("패스트캠퍼스");

        book.setPublisher(publisher);
        bookRepository.save(book);

        publisher.addBook(book);
        publisherRepository.save(publisher);

        System.out.println("books : " + bookRepository.findAll());
        System.out.println("publishers : " + publisherRepository.findAll());

        Book book1 = bookRepository.findById(1L).get();
        book1.getPublisher().setName("슬로우");

        bookRepository.save(book1);

        System.out.println("publisher : " + publisherRepository.findAll());

        Book book2 = bookRepository.findById(1L).get();
//        bookRepository.delete(book2);


        Book book3 = bookRepository.findById(1L).get();
        book3.setPublisher(null);

        bookRepository.save(book3);

        System.out.println("book : " + bookRepository.findAll());
        System.out.println("publishers : " + publisherRepository.findAll());
        System.out.println("book3 - publishers : " + bookRepository.findById(1L).get().getPublisher());

    }

    @Test
    void bookRemoveCascadeTest(){
        bookRepository.deleteById(1L);
        bookRepository.deleteById(2L);
        System.out.println("books : " + bookRepository.findAll());
        System.out.println("publishers : " + publisherRepository.findAll());


        bookRepository.findAll().forEach(book -> System.out.println(book.getPublisher()));

    }

    @Test
    void softDelete(){
        bookRepository.findAll().forEach(System.out::println);
        System.out.println(bookRepository.findById(3L));
    }

    private void givenBookAndReview() {
        UserTable user = givenUser();
        Publisher publisher = givenPublisher();
        Book book = givenBook(publisher);
        givenReview(user, book);

    }

    private Book givenBook(Publisher publisher) {
        Book book = new Book();
        book.setName("jpa 바이블");
        book.setPublisher(publisher);

        return bookRepository.save(book);
    }

    private Publisher givenPublisher(){
        Publisher publisher = new Publisher();
        publisher.setName("패스트 캠퍼스");
        return publisherRepository.save(publisher);
    }

    private UserTable givenUser(){
        return userTableRepository.findByEmail("martin@fastcampus.com");
    }

    private void givenReview(UserTable user, Book book) {
        Review review = new Review();
        review.setTitle("내 인생을 바꾼 책");
        review.setContent("꿀잼");
        review.setScore(5.0f);
        review.setUser(user);
        review.setBook(book);

        reviewRepostory.save(review);
    }
}
