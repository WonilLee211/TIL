# 메모리 동적할당 + 메모리 활용

- 구조체의 동적 할당
- 노드, LinkedList
- 메모리 관리 함수(memmove, memcpy, memcmp)함수의 사용


## 구조체 동적할당

```c
#include <stdio.h>
#include <stdlib.h>
struct Something {
    int a, b;
};
int main(){
    struct Something *arr;
    int size, i;

    printf("원하는 구조체 배열의 크기 : ");
    scanf("%d", &size);

    arr = (struct Something *)malloc(sizeof(struct Something) * size);

    for (i = 0; i < size; i++){
        printf("arr[%d].a : ", i);
        scanf("%d", &arr[i].a;)
        printf("arr[%d].b : ", i);
        scanf("%d", &arr[i].b;)
    }

    for (i = 0; i < size; i++)
        printf("arr[&d].a : %d, arr[%d].b = %d \n", i, arr[i].a, i, arr[i].b);

    free(arr);

    return 0;
}
// 원하시는 구조체 배열의 크기 : 2
// arr[0].a : 1
// arr[0].b : 2
// arr[1].a : 3
// arr[1].b : 4
// arr[0].a : 1 , arr[0].b : 2 
// arr[1].a : 3 , arr[1].b : 4 
```

## 노드, LinkedList

![image](https://github.com/WonilLee211/TIL/assets/109330610/34546309-6717-4a8b-a223-401ac5d51abb)

배열에서 불가능했던 배열 중간에 새 원소를 집어넣을 수 있는 형태


```c
#include <stdio.h>
#include <stdlib.h>
struct Node* createNode(int data);
struct Node* insertNode(struct Node* curNode, int data);
void destroyNode(struct Node* destroy, struct Node* head);
void printNodeFrom(struct Node* from);

struct Node {
  int data;              /* 데이터 */
  struct Node* nextNode; /* 다음 노드를 가리키는 부분 */
};
int main() {
  struct Node* Node1 = createNode(100);
  struct Node* Node2 = insertNode(Node1, 200);
  struct Node* Node3 = insertNode(Node2, 300);
  /* Node 2 뒤에 Node4 넣기 */
  struct Node* Node4 = insertNode(Node2, 400);

  printNodeFrom(Node1);
  return 0;
}
// node 생성 함수  
struct Node* createNode(int data){
    struct Node* node = (struct Node *)malloc(sizeof(struct Node));

    node->data = data;
    node->nextNode = NULL;

    return node;
}
// node 삽입 함수
struct Node* insertNode(struct Node *curNode, int data){
    struct Node *newNode, *afterNode;
    afterNode = curNode->nextNode;

    newNode = (struct Node *)malloc(sizeof(struct Node));

    newNode->data = data;
    newNode->nextNode = afterNode;

    curNode->nextNode = newNode;

    return newNode;
}
// 노드 파괴 함수
void destroyNode(struct Node *destroy, struct Node *head){
    
    if (destroy == head){
        free(destroy);
        return;
    }

    struct Node *next = head;
        
    while(next){
        if (destroy == next->nextNode)
            next->nextNode = destroy->nextNode;
        next = next->nextNode;
    }
    free(destroy);
}
void printNodeFrom(struct Node *from){
    while(from){
        printf("노드의 데이터 : %d \n", from->data);
        from = from->nextNode;
    }
}
```

## 메모리 관리 함수

`<string.h>`에 정의된 메모리를 직접 관리하는 함수들

1. `memmove`
2. `memcpy`
3. `memcmp`
4. `memset`

<br>

### 1. `memcpy`

`memcpy(&dest, &src, 복사할 길이 + 1);`

메모리의 특정한 부분으로 얼마까지의 부분을 다른 메모리 영역으로 복사해주는 함수

아래와 같이 문자열 복사에 사용할 수 있음

> 참고 : 문자열 복사를 전문으로 하는 함수, `strcpy(char *dest, char src);`

```c
#include <stdio.h>
#include <string.h>
int main(){
    char str[50] = "I love Chewing C hahaha";
    char str2;
    char str3;

    memcpy(str2, str, strlen(str) + 1);
    memcpy(str3, "hello", 6);

    printf("%s \n", str);
    printf("%s \n", str2);
    printf("%s \n", str3);

    return 0;
}
// I love Chewing C hahaha 
// I love Chewing C hahaha 
// hello 
```

<br>

### 2. `memmove`

`void* memmove(void* dest, const void* src, size_t n);`
- `dest`: 복사한 데이터를 저장할 메모리 블록의 시작 주소를 가리키는 포인터
- `src` : 복사할 데이터가 있는 메모리 블록의 시작 주소를 가리키는 포인터
- `n` : 복사할 바이트 수를 나타내는 값으로, `src`에서 `dest`로 복사할 바이트의 개수를 지정



메모리의 특정 블록의 내용을 다른 블록으로 옮겨주는 함수

`memcpy`와 차이점
- 두 메모리 블록이 겹치더라도 안전하게 복사를 수행
- 겹친느 부분을 중간에 임시공간에 복사한 후 목적지로 이동하여 안전하게 복사함

```c
#include <stdio.h>
#include <string.h>
int main(){
  char str[50] = "I love Chewing C hahaha";

  printf("%s \n", str);
  printf("memmove 이후 \n");
  memmove(str + strlen(str), str + 17, 6);
  printf("%s \n", str);

  return 0;
}
// I love Chewing C hahaha 
// memmove 이후 
// I love Chewing C hahahahahaha 
```

- 위 코드는 `str`의 18번째 자리에서 6개를 `str`의 27번째 자리부터 복사해 넣는다는 의미


<br>

### 3. `memcmp`

`int memcmp(const void* ptr1, const void* ptr2, size_t num);`

두 개의 메모리 블록을 주어진 바이트 크기만큼 비교하는 함수

- `ptr1` : 첫 번째 메모리 블록의 시작 주소를 가리키는 포인터
- `ptr2` : 두 번째 메모리 블록의 시작 주소를 가리키는 포인터
- `num` : 비교할 원소의 형 단위 바이트 수 지정


`return`

- `0`: 두 메모리 블록이 `num`바이트만큼 완전히 동일함
- `음수 값` : `ptr1`이 `ptr2`보다 작은 값을 가진 바이트를 처음으로 발견한 위치에서 아스키코드 값 차이
- `양수 값` : `ptr1`이 `ptr2`보다 큰 값을 가진 바이트를 처음으로 발견한 위치에서 아스키코드 값 차이


```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(){
    int **parr, i;
    int arr[10] = {1, 2, 3, 4, 5};
    int arr2[10] = {1, 2, 3, 4, 5};
    int arr3[10] = {1, 2, 3, 4, 4};
    int arr4[10] = {1, 2, 3, 5, 4};
    
    parr = (int **)malloc(sizeof(int *) * 3);
    for (i = 0; i < 3; i++){
        parr[i] = (int *)malloc(sizeof(int) * 10);
    }

    /* 학습했던 아래 방식은 컴파일되지 않거나 에러가 발생한다.
    parr[0] = arr2;
    parr[1] = arr3;
    parr[2] = arr4;
    */
    memcpy(parr[0], arr2, sizeof(int) * 10);
    memcpy(parr[1], arr3, sizeof(int) * 10);
    memcpy(parr[2], arr4, sizeof(int) * 10);
    *(parr)
    for (i = 0; i < 3; i++){
        if(memcmp(arr, parr[i], sizeof(int) * 5) == 0){
            printf("arr 과 arr%d 는 일치! \n", i + 2);
        }
        else if (memcmp(arr, parr[i], sizeof(int) * 5) > 0){
            printf("arr는 arr%d 보다 큰 값을 먼저 갖고 있음 \n", i + 2);
        }
        else {
            printf("arr는 arr%d 보다 작은 값을 먼저 갖고 있음 \n", i + 2);
        }
    }
    for (i = 0; i < 3; i++)
        free(parr[i]);
    
    free(parr);
    
    
    return 0;
}
// arr 과 arr2 는 일치! 
// arr는 arr3 보다 큰 값을 먼저 갖고 있음 
// arr는 arr4 보다 작은 값을 먼저 갖고 있음 
```