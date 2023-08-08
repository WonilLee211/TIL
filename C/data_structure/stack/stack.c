#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct NODE {
    char szData[64];
    struct NODE* next;
} NODE;

NODE* g_pHead = NULL;

int InsertAtHead(char* pszData){
    NODE* pNode = (NODE*)malloc(sizeof(NODE));
    // 메모리 초기화
    memset(pNode, 0, sizeof(NODE));
    strcpy(pNode->szData, pszData);

    if (g_pHead == NULL){
        g_pHead = pNode;
    }
    else {
        pNode->next = g_pHead;
        g_pHead = pNode;  
    }
    return 1;
}

void PrintList(void)
{
    NODE* pHead = g_pHead;
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

int IsEmpty(){
    if (g_pHead == NULL)
        return 1;
    return 0;
}

int PopData(NODE* pPopNode){
    NODE* sp = g_pHead;
    if (IsEmpty())
        return 0;

    memcpy(pPopNode, sp, sizeof(NODE));

    g_pHead = sp->next;
    free(sp);

    return 1;
}

int main()
{
    PushData("TEST01");
    PushData("TEST02");
    PushData("TEST03");

    NODE node = { 0 };
    PopData(&node);
    printf("Pop : %s\n", node.szData);
    PopData(&node);
    printf("Pop : %s\n", node.szData);
    PopData(&node);
    printf("Pop : %s\n", node.szData);

    return 0;
}