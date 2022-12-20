


## error  trouble shooting

### JdbcSQLSyntaxErrorException

- User class 테스트 진행 과정에서 `Caused by: org.h2.jdbc.JdbcSQLSyntaxErrorException: Syntax error in SQL statement "drop table if exists [*]user CASCADE "; expected "identifier"; SQL statement:`
 발생
- 구글링읕 통해 공통적인 원인이 identifier, 예약어 문제였다.
- 그래서 User class를 UserTable로 변경해서 retry했더니 에러 해결.
- User는 예약어가 아닌데, 어떤 문제였는지 근본 원인이 뭐였을까..


### Hibernate 초기화 전 data.sql 먼저 실행되어 발생하는 오류

오류 내용

```
Caused by: org.springframework.beans.factory.BeanCreationException: Error creating bean with name 'dataSourceScriptDatabaseInitializer' defined in class path resource [org/springframework/boot/autoconfigure/sql/init/DataSourceInitializationConfiguration.class]: Invocation of init method failed; nested exception is org.springframework.jdbc.datasource.init.ScriptStatementFailedException: Failed to execute SQL script statement #1 of URL [file:/C:/Users/shbae/IdeaProjects/fastcampus/build/resources/main/data.sql]: call next value for hibernate_sequence; nested exception is org.h2.jdbc.JdbcSQLSyntaxErrorException: Sequence "HIBERNATE_SEQUENCE" not found; SQL statement:
call next value for hibernate_sequence [90036-200]~
```

- 위 오류는 Hibernate가 초기화되기 전에 data.sql이 먼저 실행되어서 발생하는 오류

- 해결방법  
    - application 설정파일에 `spring.jpa.defer-datasource-initialization: true`로 설정