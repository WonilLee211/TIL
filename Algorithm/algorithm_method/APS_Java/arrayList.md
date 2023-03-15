# 동적 배열

Java에서 배열을 선언하기 위해서는 다음과 같이 선언했었습니다.

`int[] a = new int[100];`

- 정적 배열이라고 부릅니다.
- 정적 배열의 경우에는 배열의 선언과 동시에 그 크기를 정해줘야 함
- 하지만 자주 길이가 바뀌는 경우라면, **명확히 메모리를 낭비**


## 동적 배열

- 정적 배열의 메모리 낭비를 해결하기 위한 자료구조
- 정확히 사용하고 싶은 만큼만 공간을 차지하여 사용하는 방식입니다.

```java

import java.util.ArrayList;

public class Main {
	public static void main(String[] args) {
		ArrayList<Integer> v = new ArrayList<>();
	}
}
```

## ArrayList를 이용할 때 자주 사용되는 메서드

맨 뒤에 데이터 E를 추가합니다.
- add(E)

index 위치에 있는 원소를 삭제합니다. 첫 번째 원소의 경우 remove(0), 맨 뒤에 있던 데이터를 삭제하기 위해서는 remove(name.size() - 1) 이 필요합니다.

- remove(index)

현재 ArrayList에 들어있는 데이터의 수를 반환합니다.

- size()

index 위치에 있는 원소를 조회합니다.

- get(index)

## 컨테이너 이터레이터

`Iterator<T> iterator = (기존 컨테이너 이름).iterator();`

```java
import java.util.ArrayList;
import java.util.Iterator;

public class Main {
    public static void main(String[] args) {
        ArrayList<Integer> v = new ArrayList<>();   // 정수를 관리할 ArrayList를 선언하고
        v.add(5);                                   // v : [5]
        v.add(2);                                   // v : [5, 2]
        v.add(9);                                   // v : [5, 2, 9]

        // Iterator를 이용한 Vector 컨테이너 내의 원소들 순회
        Iterator<Integer> iterator = v.iterator();  
        while(iterator.hasNext()) {
            Integer num = iterator.next();
            System.out.println(num);                // 5 2 9
        }
    }
}

```


## summary

1. 정적배열과 달리 동적배열은 길이를 동적으로 바꿀 수 있다.
2. 길이에 변동이 이쓴 경우 동적 배열을 사용하는 것이 메모리 사용에 있어 효율적
