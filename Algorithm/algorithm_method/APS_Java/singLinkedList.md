# 연결 리스트

- ArrayList에서 원소 추가, 삭제가 빈번할 때 O(n)의 시간 복잡도 손해를 줄이기 위해 고안된 자료 구조
- 한 노드에서 데이터와 연결되는 다음 노드 정보만 저장하는 자료구조
    - `연결 리스트에서 노드 : 노드의 값과 연결되는 노드 정보만 저장하는 하나의 창구`
- 단방향 연결 리스트와 양방향 연결리스트가 있음

## 단방향 연결리스트

### **노드 구성**

1. data : 값
2. next : 연결된 다음 노드

### **링크드 리스트 구성**

1. head : 가장 앞 node
2. tail : 가장 마지막 node

## 연산

### 1. 삽입

- tail 뒤쪽에 값을 삽입
```java

public void insert_end(int num){
    Node newNode = new Node(num); // 생성
    tail.next = newNode;          // 연결
    tail = newNode;               // tail 지정
}


```


- head 앞에 값을 삽입

```java

public void insert_front(int num){
    Node newNode = new Node(num); // 생성
    newNode,next = head;          // 연결
    head = newNode;               // head 지정
}


```


- head 뒤에 값을 삽입

```java

public void insert_middle(int idx, int num){
    Node newNode = new Node(num); // 생성
    Node cur = head;
    for (int i = 0; i < idx ; i++){
        cur = cur.next;
    }
    newNode.next = cur.next;
    cur.next = newNode;
    cur = newNode;
}


```

### 2. 삭제

- 해당 노드의 next를 null로 설정
- 또는 해당 노드의 next를 nextNode의 next로 설정

### 3. 탐색

- head에서부터 iterator 사용
