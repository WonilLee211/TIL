# 문자열 연산

- 문자열 리터럴(literal)에 대한 이해
- 문자열 다루기(복사, 합치기, 비교하기)

## 리터럴(literal)

- 소스 코드 상에서 고정된 값을 가지는 것
- C의 경우 큰 따옴표(`"`)로 묶인 것들을 문자열 리터럴(string literal)이라 함.
- 이러한 리터럴들은 프로그램이 실행될 때 메모리 상에서 별도의 공간에서 일괄 관리됨
- 프로그램이 메모리에 로드될 때 5 가지 종류의 영역(text segment, data segment, bss segment, heap, stack)이 존재함.
    - 코드, 상수, 리터럴 등은 text segment에 저장됨.
    - 일반적으로 text segment 내에 데이터는 수정이 불가능(운영체제, 컴파일러에 따라 상이)

`char *pstr = "IAmLiteral";`

- text segment에 저장되어 있는 "IAmLiteral" 문자열 리터럴의 주소값을 가리키는 포인터를 선언함

## 문자열 연산

- 문자열 내에 총 문자의 수를 세는 함수
    - 이미 구현함
- 문자열을 복사하는 함수
- 문자열을 병합하는 함수
- 문자열을 비교하는 함수

<br>

### 문자열을 복사하는 함수

- 복사가 성공적으로 왼료되었다면 1을 리턴
- a 문자열을 b로 복사

```c
// dest의 사이즈는 항상 src보다 커야 함
int copy_str(char *dest, char *src){
    while (*src){
        *dest = *str;
        src++;
        dest++;
    }
    *dest = '\0';
    return 1;
}
```

## 문자열 병합하는 함수

```c
#include <stdio.h>
// str2의 크기가 str1 배열에 포함될 만큼 충분히 작다.
int stradd(char *str1, char *str2){
    while(*str1){
        str1++;
    }
    while (*str2){
        *str1 = *str2;
        str1++;
        str2++;
    }
    *str1 = '\n';
    return 0;
}
```

## 문자열을 비교하는 함수

- 두 문자열이 동일한 값을 가지는 비교

```c
int compare(char *str1, char *str2){
    while (*str1){
        if (*str1 != *str2){
            return 0;
        }
        str1++;
        str2++;
    }
    if (*str2 == '\n'){
        return 1;
    }
    return 0;
}
```

## 도서 관리 프로그램

```c
#include <stdio.h>
int add_book(char (*book_name)[30], char (*auth_name)[30], char (*publ_name)[30], 
            int (*borrowed), int *num_total_book);
int search_book(char (*book_name)[30], char (*auth_name)[30], 
                char (*publ_name)[30], int *num_total_book);
int compare(char *str1, char *ctr2);
int borrow_book(int *borrowed);
int return_book(int *borrowed);
int main() {
    int user_choice, flag;
    int num_total_book = 0;
    /* 각각 책, 저자, 출판사를 저장할 배열 생성. 책의 최대 개수는 100 권*/
    char book_name[100][30], auth_name[100][30], publ_name[100][30];
    /* 빌렸는지 상태를 표시 */
    int borrowed[100];

    flag = 1;
    while(flag){
        printf("도서 관리 프로그램 \n");
        printf("메뉴를 선택하세요 \n");
        printf("1. 책을 새로 추가하기 \n");
        printf("2. 책을 검색하기 \n");
        printf("3. 책을 빌리기 \n");
        printf("4. 책을 반납하기 \n");
        printf("5. 프로그램 종료 \n");

        printf("당신의 선택은 : ");
        scanf("%d", &user_choice);
        switch (user_choice) {
            case 1:
                /* 책을 새로 추가하는 함수 호출 */
                add_book(book_name, auth_name, publ_name, borrowed, &num_total_book);
                break;
            case 2: 
                /* 책을 검색하는 함수 호출 */
                search_book(book_name, auth_name, publ_name, &num_total_book);
                break;
            case 3: 
                /* 책을 빌리는 함수 호출 */
                borrow_book(borrowed);
                break;
            case 4:
                /* 책을 반납하는 함수 호출 */
                return_book(borrowed);
                break;
            case 5:
                /* 프로그램을 종료한다. */
                flag = 0;
                break;
        }
    }
    return 0;
}
int add_book(char (*book_name)[30], char (*auth_name)[30], char (*publ_name)[30], 
            int (*borrowed), int *num_total_book){
    printf("추가할 책의 제목 : ");
    scanf("%s", book_name[*num_total_book]);
    printf("추가할 책의 저자 : ");
    scanf("%s", auth_name[*num_total_book]);
    printf("추가할 책의 출판사 : ");
    scanf("%s", publ_name[*num_total_book]);

    borrowed[*num_total_book] = 1;
    (*num_total_book)++;
    printf("추가 완료! \n");
    return 0;
}
int search_book(char (*book_name)[30], char (*auth_name)[30], 
                char (*publ_name)[30], int *num_total_book){
    int colomn;
    int i;
    char user_input[30];
    char (*pcolomn)[30];

    printf("어느 것으로 검색 할 것인가요? \n");
    printf("1. 책 제목 검색 \n");
    printf("2. 지은이 검색 \n");
    printf("3. 출판사 검색 \n");
    scanf("%d", &colomn);

    printf("검색할 단어를 입력해주세요 : ");
    scanf("%s", user_input);

    switch (colomn){
        case 1:
            pcolomn = book_name;
            break;
        case 2:
            pcolomn = auth_name;
            break;
        case 3:
            pcolomn = publ_name;
            break;
    }

    for (i = 0; i < *num_total_book; i++){
        if (compare(user_input, pcolomn[i])){
            printf("번호 : %d // 책 이름 : %s // 지은이 : %s // 출판사 : %s \n", i, book_name[i], auth_name[i], publ_name[i]);
            return 0;         
        }
    }
    return 0;
}
int compare(char *str1, char *str2){
    while (*str1){
        if (*str1 != *str2) return 0;

        str1++;
        str2++;
    }
    if (*str2 == '\0') return 1;
    return 0;
}
int borrow_book(int *borrowed){
    int book_num;

    printf("빌릴 책의 번호를 말해주세요 \n");
    printf("책 번호 : ");
    scanf("%d", &book_num);

    if (borrowed[book_num])
        printf("이미 대출된 책입니다! \n");
    else {
        printf("책이 성공적으로 대출되었습니다. \n");
        borrowed[book_num] = 1;
    }
    return 0;
}
int return_book(int *borrowed){
    int book_num;

    printf("반납할 책의 번호를 써주세요 \n");
    printf("책 번호 : ");
    scanf("%d", &book_num);

    if (borrowed[book_num] == 0)
        printf("이미 반납되어 있는 상태입니다\n");
    else {
        borrowed[book_num] = 0;
        printf("성공적으로 반납되었습니다\n");
    }
    return 0;
}
```

