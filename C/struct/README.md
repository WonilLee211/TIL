# 구조체

- about struct
- 구조체 포인터 및 `->` 연산자


## about struct

대상 정보 특성들을 모두 배열로 관리하기에 인자가 많아지는 단점이 있다. 관리 또한 매우 불편한 현실이다.

여러 문제를 해결하고자, 배열 한 개에 정보의 여러 특성을 저장할 수 있는 `구조체` 개념이 도입되었다.

<br>

### 정의

```c
struct 구조체_이름 {
    char str[10];
    int i;
};
```

- 구조체 내부에서 변수를 초기화할 수 없음

```c
#include <stdio.h>
struct Human {
    int age;    // 나이
    int height; // 키
    int weight; // 몸무게
};              // 세미콜론 붙이기
int main(){
    struct Human Psi;

    Psi.age = 99;
    Psi.height = 185;
    Psi.weight = 80;

    printf("Psi 에 대한 정보 \n");
    printf("나이   : %d \n", Psi.age);
    printf("키     : %d \n", Psi.height);
    printf("몸무게 : %d \n", Psi.weight);
    return 0;
}
// Psi 에 대한 정보 
// 나이   : 99 
// 키     : 185 
// 몸무게 : 80 
```
```c
#include <stdio.h>
int copy_str(char *dest, char * src);
struct Book {
    // 책 이름
    char name[30];
    // 저자
    char author[30];
    // 출판사
    char publ[30];
    // 대여 여부
    int borrowed;
};
int main(){
    struct Book Harry_Potter;

    copy_str(Harry_Potter.name, "Harry Potter");
    copy_str(Harry_Potter.author, "J.K. Rolling");
    copy_str(Harry_Potter.publ, "Scholastic");
    Harry_Potter.borrowed = 0;

    printf("책 이름 : %s \n", Harry_Potter.name);
    printf("저자 이름 : %s \n", Harry_Potter.author);
    printf("출판사 이름 : %s \n", Harry_Potter.publ);
    printf("대여 여부 : %d \n", Harry_Potter.borrowed);

    return 0;
}
int copy_str(char *dest, char *src){
    while (*src){
        *dest = *src;
        dest++;
        src++;
    }
    *dest = '\0';

    return 0;
}
// 책 이름 : Harry Potter 
// 저자 이름 : J.K. Rolling 
// 출판사 이름 : Scholastic 
// 대여 여부 : 0
```
```c
#include <stdio.h>
struct Book {
    char name[30];
    char author[30];
    char publ[30];
    int borrowed;
};
int main() {
    struct Book book_list[3];
    int i;

    for (i = 0; i < 3; i++){
        printf("책 %d 정보 입력 : ", i);
        scanf("%s%s%s", book_list[i].name, book_list[i].author, book_list,[i].publ);
        book_list[i].borrowed = 0;
    }

    for (i = 0; i < 3; i++){
        printf("------------------------------- \n");
        printf("책 %s 의 정보\n", book_list[i].name);
        printf("저자 : %s \n", book_list[i].auth);
        printf("출판사 : %s \n", book_list[i].publ);

        if (book_list[i].borrowed == 0) {
        printf("서적 보유 \n");
        } else {
        printf("서적 대여 \n");
        }
    }
    return 0;
}
```

## 구조체 포인터

```c
#include <stdio.h>
struct test {
    int a, b;
};
int main(){
    struct test st;
    struct test *pst;

    pst = &st;
    (*pst).a = 1;
    (*pst).b = 2;

    printf("st의 a 맴버 : %d \n", st.a);
    printf("st의 b 맴버 : %d \n", st.b);

    return 0;
}
```

- `pst`는 4byte를 차지하는 포인터
- 구조체 포인터에서 맴버에 접근하기 위해 (*)를 항상 작성해야 하는 번거로움이 있다.

## `->` 연산자

- 구조체 포인터를 사용할 때 `(*)`와 같은 불편한 표현을 대체하기 위한 연산자

```c
/* 구조체 포인터 */
#include <stdio.h>
struct test {
  int a, b;
};
int main() {
  struct test st;
  struct test *ptr;
  ptr = &st;
  ptr->a = 1;
  ptr->b = 2;
  printf("st 의 a 멤버 : %d \n", st.a);
  printf("st 의 b 멤버 : %d \n", st.b);
  return 0;
}
```