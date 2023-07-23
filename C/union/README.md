# 공용체(union)

![image](https://github.com/WonilLee211/TIL/assets/109330610/857a0d84-d07e-4162-8b52-3adb528b33ab)

- 메모리를 공유한다는 특징
- 공용체 내에 맴버들의 메모리 시작 주소가 동일하여 맴버의 값을 변경함으로써 다른 맴버의 값을 변경할 수 있다.

```c
#include <stdio.h>
union A {
    int i;
    char j;
};
int main() {
    union A a;
    a.i = 0x12345678;

    printf("%x", aj);
    
    return 0;
}
// 78
```
- 위와 같이 공동체의 i 맴버 값을 초기화했을 때 j 맴버의 값까지 초기화된 것을 볼 수 있음
- 리틀 엔디안 방식을 따르기 때문에 j 맴버의 값이 78로 초기화 됨.

## 빅 엔디안(Big Endian), 리틀 엔디안(little Endian)

### 빅 엔디안(Big Endian)

![image](https://github.com/WonilLee211/TIL/assets/109330610/0dc94107-cf96-4db2-b61e-2d3cb430d81e)

낮은 주소값에 상위 비트를 적는 방법

### 리틀 엔디안(little Endian)

![image](https://github.com/WonilLee211/TIL/assets/109330610/9be2ba85-43e2-4b1a-8006-baccab9940f4)

높은 주소값에 상위 비트를 적는 방식

대부분 `x86` 프로세스에서는 리틀 엔디안 방식 채용


`j` 의 형을 `short`으로 했다면, 0x5678 값으로 초기화됐을 것

컴파일러가 리틀 엔디안으로 저장된 것을 알고 있기 때문에 적절한 변환을 통해 값의 순서를 맞춰 읽게 됨

```c
#include <stdio.h>
union A {
  int i;
  short j;
};
int main() {
  union A a;
  a.i = 0x12345678;
  printf("%x", a.j);
  return 0;
}
// 5678
```

