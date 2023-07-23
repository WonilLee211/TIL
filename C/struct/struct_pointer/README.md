# 구조체 포인터

- 구조체 포인터
- 구조체를 인자로 받기
- 구조체의 대입
- 구조체 안에 구조체


## 구조체 포인터

```c
#include <stdio.h>
struct TEST {
    int c, *pointer;
};
int main() {
    struct TEST t;
    struct TEST *pt = &t;
    int i = 0;

    // 구조체의 포인터가 i를 가리키도록 선언
    t.pointer = &t;
    // t의 맴버 pointer가 가리키는 변수의 값을 3으로 변경
    *t.pointer = 3;
    printf("i : %d \n", i);
    
    /*
    ->가 *보다 우선순위가 높아, 먼저 해석함
    즉, pt가 가리키는 구조체 변수의 pointer 맴버가 가리키는 값을 4로 바꾼다.
    */
    *pt->pointer = 4;
    printf("i : %d \n", i);

    return 0;
}
```

### 구조체 포인터 연습

```c
#include <stdio.h>
int add_one(int *a);
struct TEST {
    int c;
};
int main(){
    struct TEST t;
    struct TEST *pt = &t;

    //pt가 가리키는 구조체 변수 c맴버의 값을 0으로 함
    pt->c = 0;
    // add_one 함수의 인자에 t 구조체 변수의 맴버 c의 주소값을 전달
    add_one(&t.c);
    printf("t.c : %d \n", t.c);
    // add_one 함수의 인자에 pt가 가리키는 구조체 변수의 맴버 c의 주소값을 전달
    add_one(&pt->c);
    printf("t.c : %d \n", t.c);
    printf("pt->c : %d \n", pt->c);

    return 0;
}
int add_one(int *a){
    (*a)++;
    return 0;
}
```

## 구조체의 대입

```c
#include <stdio.h>
struct TEST {
  int i;
  char c;
};
int main(){
    struct TEST t1, t2;

    st.i = 1;
    st.c = 'c';

    t2 = t1;

    printf("st2.i : %d \n", st2.i);
    printf("st2.c : %c \n", st2.c);

    return 0;
}
// st2.i : 1 
// st2.c : c 
```
- `=`연산자가 가능하다

```c
#include <stdio.h>
int copy_str(char *dest, char *src);
struct TEST {
    int i;
    char str[20];
};
int main(){
    struct TEST a, b;
    
    b.i = 3;
    copy_str(b.str, "hello, world");

    a = b;

    printf("a.str : %s \n", a.str);
    printf("a.i : %d \n", a.i);

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
// a.str : hello, world 
// a.i : 3 
```

## 구조체 인자로 전달

- 구조체의 맴버 값을 변경하기 위해 구조체의 주소값을 인자로 전달해야 함.
```c
#include <stdio.h>
struct Human {
    int age, gender;
    char name[20];
};
int set_human(struct Human *a, int age, int gender, char *name);
int copy_str(char *dest, char *src);
int main(){
    struct Human human;
    
    set_human(&human, 10, 1, "Lee");

    printf("AGE : %d // Gender : %d // Name : %s \n", human.age, human.gender, human.name);

    return 0;
}
int set_human(struct Human *human, int age, int gender, char *name){
    human->age = age;
    human->gender = gender;
    copy_srtc(human->name, name);
    return 0;
}
int copy_str(char *dest, char *src){
    while(*src){
        *dest = *src;
        dest++;
        src++;
    }
    *dest = '\0';
    return 0;
}
// AGE : 10 // Gender : 1 // Name : Lee 
```

## 구조체 안에 구조체


```c
#include <stdio.h>
struct employee {
    int age, salary;
};
struct company {
    struct employee data;
    char name[10];
};
int main(){
    struct company Tmax;
    Tmax.data.age = 31;
    Tmax.data.salary = 3000000;

    printf("Tmax's age : %d \n", Kim.data.age);
    printf("Tmax's salary : %d$/year \n", Kim.data.salary);

    return 0;
}
// Tmax's age : 31 
// Tmax's salary : 3000000$/year 
```

## 구조체를 리턴하는 함수

```c
#include <stdio.h>
struct AA  function(int j);
struct AA {
    int i;
};
int main(){
    struct AA a;

    a = function(10);
    printf("a.i : %d \n", a.i);

    return 0;
}
struct AA function(int j){
    struct AA A;
    A.i = j;

    return A;
}
```

## 구조체 정의 방법 2

```c
#include <stdio.h>
char copy_str(char *dest, char *src);
int print_Obj_status(struct obj OBJ);
struct obj {
    char name[20];
    int x, y;
} Ball;
struct Human {
    int age, height, weight, gender;
} Lee = {31, 182, 75, 0}, Eve = {27, 166, 48, 1};
int main(){
    Ball.x = 3;
    Ball.y = 4;
    copy_str(Ball.name, "RED BALL");

    print_obj_status(Ball);

    /* ------------------------ */
    struct Human adam = {31, 182, 75, 0};

    return 0;
}
char copy_str(char *dest, char *src){
    while (*src){
        *dest = *src;
        dest++;
        src++;
    }
    *dest = '\0';

    return 1;
}
int print_Obj_status(struct obj OBJ){
    printf("Location of %s \n", OBJ.name);
    printf("( %d , %d ) \n", OBJ.x, OBJ.y);

    return 0;
}
// Location of RED BALL 
// ( 3 , 4 ) 
```