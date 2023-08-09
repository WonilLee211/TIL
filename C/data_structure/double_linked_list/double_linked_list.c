#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/** 이중 연결 리스트
 * 더미 헤드/테일 노드를 넣는다
 * head.next = &tail이면 empty
 * 노드가 하나만 있어도 prev, next 포인터는 NULL이 아니다.
 **/

typedef struct NODE 
{
    char szData[64];
    struct NODE* prev;
    struct NODE* next;
} NODE;

NODE *g_pHead, *g_pTail;
int g_nSize;

void InitList(void);
void ReleaseList(void);
void PrintList(void);
int InsertAtHead(const char* pszData);
int InsertAtTail(const char* pszData);
NODE* FindNode(const char* pszData);
int DeleteNode(const char* pszData);
int GetSize(void);
int GetLength(void);
int IsEmpty(void);
void InsertBefore(NODE* pDstNode, const char *pszData);
int InsertAt(int idx, const char *pszData);

void InitList(void){
    g_pHead = (NODE*)malloc(sizeof(NODE));
    g_pTail = (NODE*)malloc(sizeof(NODE));
    g_nSize = 0;

    memset(g_pHead, 0, sizeof(NODE));
    memset(g_pTail, 0, sizeof(NODE));
    
    strcpy(g_pHead->szData, "Dummy Head");
    strcpy(g_pTail->szData, "Dummy Tail");

    g_pHead->next = g_pTail;
    g_pTail->prev = g_pHead;
}
void ReleaseList(void){
    NODE* pTmp = g_pHead;
    while (pTmp != NULL){
        NODE* pDelete = pTmp;
        free(pDelete);
        pTmp = pTmp->next;
    }
    g_pHead = NULL;
    g_pTail = NULL;
    g_nSize = 0;
}
void PrintList(void){
    printf("PrintList() : g_nSize[%d], g_pHead[%p], g_pTail[%p]\n", g_nSize, g_pHead, g_pTail);
    NODE* pTmp = g_pHead;
    while (pTmp != NULL){
        printf("prev[%p] [%p]%s next[%p]\n",pTmp->prev, pTmp, pTmp->szData, pTmp->next);
        pTmp = pTmp->next;
    }
}
/**
 * 2중 연결 리스트 노드 추가
 * - 추가할 노드의 prev, next를 설정한다.
 * - 노드의 삽입이 일어나는 지점의 prev 노드르 찾는다
 * - 첫 번째로 추가되는 노드와 이후 추가되는 방식은 구분한다. 
**/
int InsertAtHead(const char* pszData){
    NODE* pNewNode = (NODE*)malloc(sizeof(NODE));
    memset(pNewNode, 0, sizeof(NODE));
    strcpy(pNewNode->szData, pszData);
    
    pNewNode->next = g_pHead->next;
    pNewNode->prev = g_pHead;

    g_pHead->next = pNewNode;
    pNewNode->next->prev = pNewNode;

    return ++g_nSize;
}

int InsertAtTail(const char* pszData){
    NODE* pNewNode = (NODE*)malloc(sizeof(NODE));
    memset(pNewNode, 0, sizeof(NODE));
    strcpy(pNewNode->szData, pszData);
    
    pNewNode->prev = g_pTail->prev;
    pNewNode->next = g_pTail;

    g_pTail->prev = pNewNode;
    pNewNode->prev->next = pNewNode;

    return ++g_nSize;
}
NODE* FindNode(const char* pszData){
    NODE* pNode = g_pHead->next;
    while (pNode != g_pTail){
        if (strcmp(pNode->szData, pszData) == 0)
            return pNode;
        pNode = pNode->next;
    }
    return NULL;
}
int DeleteNode(const char* pszData){
    NODE* pNode = FindNode(pszData);

    pNode->prev->next = pNode->next;
    pNode->next->prev = pNode->prev;

    printf("DeleteNode() : %p \n", pNode);
    g_nSize--;

    free(pNode);
    return 0;
}
/* 2중 연결 리스트의 전체 크기를 반환하는 함수 */
int GetSize(void){
	return g_nSize;
}
/* 2중 연결 리스트의 전체 크기를 반환하는 함수 */
int GetLength(void){
	return GetSize();
}
/* 2중 연결 리스트가 비어 있는지 확인하는 함수*/
int IsEmpty(void){
	return GetSize();
}
void InsertBefore(NODE *pDstNode, const char *pszData){
    NODE* pPrev = pDstNode->prev;

    NODE *pNewNode = (NODE*)malloc(sizeof(NODE));
    memset(pNewNode, 0, sizeof(NODE));
    strcpy(pDstNode->szData, pszData);

    pNewNode->next = pDstNode;
    pNewNode->prev = pPrev;
    
    pPrev->next = pNewNode;
    pDstNode->prev = pNewNode;

    g_nSize++;
}
int InsertAt(int idx, const char *pszData){
    int i = 0;
    NODE *pTmp = g_pHead->next;
    while (pTmp != g_pTail){
        if (i == idx){
            InsertBefore(pTmp, pszData);
            return i;
        }
        pTmp = pTmp->next;
        i++;
    }
    InsertAtTail(pszData);
    return i;
}
NODE *GetAt(int idx){
    int i = 0;
    NODE *pTmp = g_pHead->next;
    while (pTmp != g_pTail){
        if (i == idx)
            return pTmp;
        pTmp = pTmp->next;
        i++;
    }
    return NULL;
}
int main(){

    InitList();

    InsertAtHead("TEST01");
    InsertAtHead("TEST02");
    InsertAtHead("TEST03");
    PrintList();
    putchar('\n');

    printf("FindNode(): %p\n", FindNode("TEST01"));
    printf("FindNode(): %p\n", FindNode("TEST02"));
    printf("FindNode(): %p\n", FindNode("TEST03"));
	putchar('\n');

    DeleteNode("TEST01");
    DeleteNode("TEST02");
    DeleteNode("TEST03");
	putchar('\n');

    PrintList();
	putchar('\n');

    InsertAtTail("TEST01");
    InsertAtTail("TEST02");
    InsertAtTail("TEST03");
	putchar('\n');

    PrintList();
    putchar('\n');

    printf("FindNode(): %p\n", FindNode("TEST01"));
    printf("FindNode(): %p\n", FindNode("TEST02"));
    printf("FindNode(): %p\n", FindNode("TEST03"));
	putchar('\n');

    DeleteNode("TEST02");
	putchar('\n');

    PrintList();
	putchar('\n');

    ReleaseList();
    putchar('\n');

    return 0;
}