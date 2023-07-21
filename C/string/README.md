# 문자열

- 널-종료 문자열(Null-terminated string)
- 문자열 활용
- 문자열 입력
- 버퍼(stdin)에 대한 이해
- 고질적인 `scanf` 문제에 대한 해결 및 이해



## 널-종료 문자열(Null-terminated string)

- 문자열은 `char` 배열에 저장함
- 실질적으로 메모리에 저장된 값은 각 문자에 해당하는 아스키 값
- 문자를 배열로 관리하기 때문에 초기에 문자열의 길이를 알아야 하는 번거로움이 있었음
- 이를 해결하기 위해 문자 끝에 종료문자를 추가함으로써 오늘 날의 문자열 형태를 구성
- 아스키코드 값은 0 이며 `\0₩`으로 표현함
- C 언어의 문자열 기본적인 형태
- 이를 통해 첫 번째 원소의 주소값을 기준으로 null이 나올 때까지 출력하게 됨

```c
#include <stdio.h>

int main() {
    // 아래 3 개는 모두 동일함
    char null_1 = '\0';
    char null_2 = 0;
    // NULL은 0이라고 정의되어 있는 상수이기에, null_3에 0이 저장됨
    char null_3 = (char)NULL;

    char not_null = '0';

    printf("NULL 의 정수(아스키) 값 : %d, %d, %d \n", null_1, null_2, null_3);
    printf("'0'의 정수(아스키) 값 : %d \n", not_null);

    return 0;
}
// NULL 의 정수(아스키) 값 : 0, 0, 0 
// '0' 의 정수(아스키) 값 : 48
```

## 문자열 활용

```c
#include <stdio.h>

int main() {
    char sentence_1[4] = {'P', 's', 'i', '\0'};
    char sentence_2[4] = {'P', 's', 'i', 0};
    char sentence_3[4] = {'P', 's', 'i', (char)NULL};
    char sentence_4[4] = {"Psi"};

    printf("sentence_1 : %s \n", sentence_1);
    printf("sentence_2 : %s \n", sentence_2);
    printf("sentence_3 : %s \n", sentence_3);
    printf("sentence_4 : %s \n", sentence_4);

    return 0;
}
// sentence_1 : Psi 
// sentence_2 : Psi 
// sentence_3 : Psi 
// sentence_4 : Psi 
```

- 배열의 크기를 문자의 길이와 같은 수만큼 할당하게 된다면, `NULL`자리가 없기 때문에 허용하지 않는 메모리 범위를 읽게 된다.
- 반드시 `NULL` 문자를 위한 공간을 하나 더 추가해야 함
 
 <br>

### `""` vs `''`

| `""` | `''` |
| :--: | :--: |
| 문자열(한 개 이상의 문자)를 지정할 때 사용 | 한 개의 문자를 지정할 때 사용 |
| "abc", "a" | 'a', '\0' |


<br>

### 문자열 바꾸기

```c
#include <stdio.h>
int main(){
    char word[] = {"long sentence"};

    printf("조직 이전 : %s \n", word);

    word[0] = 'a';
    word[1] = 'b';
    word[2] = 'c';
    word[3] = 'd';
    
    printf("조작 이후 : %s \n", word);

    return 0;
}
// 조작 이전 : long sentence 
// 조작 이후 : abcd sentence 
```

- 배열 안에 빈 칸은 컴파일러가 원소의 개수를 세어서 채워넣음



## 입력 버퍼, `stdin`, 입력 스트림

- 키보드로 치는 모든 정보를 개행 문자가 입력될 때까지 일시적으로 저장해두는 버퍼
- 여기서 컴퓨터는 `\n`까지 저장하게 됨


## `scanf` 함수의 고질적인 문제

### `scanf` 동작과정

1. 사용자의 입력을 **입력 버퍼(stdin)**에 저장
2. 입력 종료 시 scanf 함수는 입력버퍼로부터 숫자 획득
    - 여기서 입력 종료 시점은 `' ', '\n', '\t`
    - 참고로 `%d` 개열의 형식, 즉 수를 입력받는 형식은 수가 아닌 데이터가 오면 입력을 종료시킴. 하지만, 변수에는 값을 할당하지 않음
    - 수를 입력받는 형식에서 첫번째 공백이 입력되면, 숫자가 입력될 때까지 종료되지 않음
3. 획득한 숫자를 입력버퍼는 삭제(개행문자는 남게 됨)

<br>

### `%c` 타입의 `scanf` 함수의 오류

```c
#include <stdio.h>
int main() {
  int num;
  char c;

  printf("숫자를 입력하세요 : ");
  scanf("%d", &num);

  printf("문자를 입력하세요 : ");
  scanf("%c", &c);
  return 0;
}
// 숫자를 입력하세요 : 1
// 문자를 입력하세요 : 
```

두 `scanf` 함수를 실행했을 때 두 번째 함수가 무시된다. 이는, 첫 번째 `scanf`함수가 입력 버퍼에서 개행 문자까지 숫자를 가져온 후 지워버리기 때문에 개행 문자가 남는 문제.


이 때 `%c`타입의 `scanf` 함수는 이유를 불문하고 입력 버퍼에서 딱 한 개의 문자만을 가져오게 된다. 없다면 기다리고, 있다면 바로 가져오게 된다. 위 과정에서 입력 버퍼에 `\n`이 남아 있기 때문에 이를 가져오게 된다. 따라서, printf("%c 출력", c); 를 해보게 된다면 '출력'이 한 칸 개행(엔터가 쳐져서)되어 나타나게 됨

<br>

### `%s` 타입의 `scanf` 함수의 오류

```c
#include <stdio.h>
int main() {
  char str[30];
  int i;

  scanf("%d", &i);
  scanf("%s", str);

  printf("str : %s", str);

  return 0;
}
// 1
// asdfasfasdf
// str : asdfasfasdf
```

`%s`타입의 `scanf` 함수는 입력 버퍼에 남아있는 공백 문자(`' ', '\n', '\t'`)가 나올 때까지 모든 공백 문자를 무시함. 데이터를 가져오다가 공백 문자 직전 문자까지 가져옴. 여전히 입력 버퍼에 공백 문자는 남게 된다.

위 코드는 문제 없이 의도대로 동작하지만, **공백이 포함된 문자열**을 입력 후 `scanf`함수는 오류를 발생시킨다.

```c
#include <stdio.h>
int main() {
  char str1[10], str2[10];

  printf("문자열을 입력하세요 : ");
  scanf("%s", str1);
  printf("입력한 문자열 : %s \n", str1);

  printf("문자열을 입력하세요 : ");
  scanf("%s", str2);
  printf("입력한 문자열 : %s \n", str2);

  return 0;
}
// 문자열을 입력하세요 : hello baby
// 입력한 문자열 : hello 
// 문자열을 입력하세요 : 입력한 문자열 : baby 
```

`hello baby\n`라는 문자열이 입력 버퍼에 저장이 되어 있다. `scanf`함수는 `' '`문자가 입력되자마자 입력버퍼에서 공백 문자 이전까지의 데이터를 읽어 가져간다. 사용자가 입력을 완료한 후, 두 번째 `scanf`함수가 실행된다.

두 번쨰 `scanf`함수는 입력 버퍼에서 처음 공백 문자를 무시하고 다음 공백문자를 만날 때까지
데이터를 읽어 가져간다.

이로 인해, 의도하지 않은 형태로 프로그램이 동작하게 된다.

또한, 여전히, 입력 버퍼 상에 공백 문자가 남는 문제가 생긴다.

<br>

## 입력 버퍼에 남는 공백문자 문제 해결책

1. `fflush`
    - 프로그램 별 호환성 이슈
2. `getchar()`
    - 숫자형 `scanf` 와 문자형 `scanf`를 혼용할 경우 문제 발생
3. `%s` 형 `scanf`함수로 문자열 받은 뒤 첫 번째 원소 사용하기
4. `%c` 타입의 `scanf`함수 사용 지양

## `%s`형 `scanf` 함수의 문자열 내 공백이 있을 시 문제 해결책

- `scanf("%[^\n]", str);` 사용하기
    - 포맷을 개행문자로 지정함으로써 문자열 중간에 공백을 공백문자로 인식하지 않도록 설정