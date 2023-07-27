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