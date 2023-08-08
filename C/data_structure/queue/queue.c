#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct NODE {
    char szData[64];
    struct NODE* next;
} NODE;

NODE g_head = { 0 };
NODE* g_pTail = 0;

int IsEmpty(){
    return g_head.next == NULL;
}
int InsertAtHead(char* pszData){
    NODE* pNode = (NODE*)malloc(sizeof(NODE));
    // 메모리 초기화
    memset(pNode, 0, sizeof(NODE));
    strcpy(pNode->szData, pszData);

    if (IsEmpty()){
        g_head.next = pNode;
        g_pTail = pNode;
    }
    else {
        pNode->next = g_head.next;
        g_head.next = pNode;  
    }
    return 1;
}

int InsertAtTail(char* pszData){
    NODE* pNode = (NODE*)malloc(sizeof(NODE));
    memset(pNode, 0, sizeof(NODE));
    strcpy(pNode->szData, pszData);

    if (IsEmpty())
        g_head.next = pNode;
    else 
        g_pTail->next = pNode;

    g_pTail = pNode;
    return 0;
}

void PrintList(void)
{
    NODE* pHead = g_head.next;

    while (pHead != NULL){
        printf("[%p] %s next[%p] \n", 
            pHead, pHead->szData, pHead->next);
        pHead = pHead->next;
    }
    putchar('\n');
}

void PushData(char *pszData){
    InsertAtHead(pszData);
}

int PopData(NODE* pPopNode){
    NODE* sp = g_head.next;
    if (IsEmpty()){
        strcpy(pPopNode->szData, "\n");
        return 0;
    }

    memcpy(pPopNode, sp, sizeof(NODE));

    g_head.next = sp->next;
    return 1;
}

int Enqueue(char* pszData){
    return InsertAtTail(pszData);
}
int Dequeue(NODE* pGetNode){
    return PopData(pGetNode);
}
void ReleaseList(void){
    printf("\nReleaseList()\n");
    NODE* pTmp = g_head.next;
    while (pTmp != NULL){
        NODE* pDelete = pTmp;
        pTmp = pTmp->next;

        printf("Delete : [%p] %s \n", pDelete, pDelete->szData);
        free(pDelete);
    }
    g_head.next = 0;
    g_pTail = 0;

}
NODE* FindData(char* pszData){
    NODE* node = g_head.next;
    while(node != 0){
        if (strcmp(node->szData, pszData) == 0){
            return node;
        }
        node = node->next;
    }
    return 0;
}
int DeleteData(char* pszData){
    NODE* pPrev = FindData(pszData);
    if (pPrev != 0){
        NODE* pDelete = pPrev->next;
        pPrev->next = pDelete->next;

        printf("DeleteData(): %s\n", pDelete->szData);

        if (pDelete == g_pTail)
            g_pTail = 0;
        
        free(pDelete);
        return 1;
    }
    return 0;
}
int main()
{
    Enqueue("TEST01");
    Enqueue("TEST02");
    Enqueue("TEST03");

    PrintList();

    NODE node = { 0 };
    Dequeue(&node);
    PrintList();
    printf("Dequeue : %s\n", node.szData);
    
    Dequeue(&node);
    PrintList();
    printf("Dequeue : %s\n", node.szData);
    
    Dequeue(&node);
    PrintList();
    printf("Dequeue : %s\n", node.szData);

    Dequeue(&node);
    PrintList();
    printf("Dequeue : %s\n", node.szData);

    Enqueue("TEST01");
    Enqueue("TEST02");
    Enqueue("TEST03");

    PrintList();

    ReleaseList();
    return 0;
}