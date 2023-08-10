#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/* 관리 대상 데이터 */
typedef struct USERDATA
{
    char szName[64];
    char szPhone[64];
} USERDATA;
/* s노드 구조체 정의 */
typedef struct NODE
{
    // 관리 대상 자료
    USERDATA *pData;
    // 자료 구조
    struct NODE *prev;
    struct NODE *next;
} NODE;
/* 전역 dummy head, tail 포인터, 리스트 사이즈 변수 정의 */
NODE *g_pHead, *g_pTail;
int g_nSize;

void InitList(void);
void ReleaseList(void);
void PrintList(void);
int InsertAtHead(const USERDATA *nParam);
int InsertAtTail(const USERDATA *pParam);
void InsertBefore(NODE *pDstNode, const USERDATA *pParam);
int InsertAt(int idx, const USERDATA *pParam);
NODE *GetAt(int idx);
NODE *FindNodeBySzname(const char *pszName);
int DeleteNode(const char * pszName);
int DeleteNode(const char * pszName);
int GetSize(void);
int GetLength(void);
int IsEmpty(void);


/* 전역 변수 초기화 함수 */
void InitList(void)
{
    g_pHead = (NODE *)malloc(sizeof(NODE));
    g_pTail = (NODE *)malloc(sizeof(NODE));

    memset(g_pHead, 0, sizeof(NODE));
    memset(g_pTail, 0, sizeof(NODE));
    g_nSize = 0;
    
    g_pHead->next = g_pTail;
    g_pTail->prev = g_pHead;
}
/* 2중 연결 리스트 메모리 해제 함수 */
void ReleaseList(void)
{
    NODE *pTmp = g_pHead;
    while (pTmp != NULL)
    {
        NODE *pDelete = pTmp;
        pTmp = pTmp->next;

        printf("free(%p)\n", pDelete);
        free(pDelete->pData);
        free(pDelete);
    }
    
    free(g_pHead);
    free(g_pTail);
    g_nSize = 0;

    puts("ReleaseList()\n");
}
/* 2중 연결리스트 전체 출력 함수 */
void PrintList(void)
{
    int i = 0;
	printf("PrintList(): g_nSize %d, g_pHead [%p], g_pTail [%p]\n", g_nSize, g_pHead, g_pTail);
	NODE *pTmp = g_pHead;
    while (pTmp != NULL)
    {
        if (pTmp == g_pHead || pTmp == g_pTail)
        	printf("[%p] DUMMY [%p]\n", pTmp->prev, pTmp->next);
        else
        {
        	printf("index:%d [%p] %p, %s, %s [%p]\n", \
                i, pTmp->prev, pTmp, \
                pTmp->pData->szName, \
                pTmp->pData->szPhone, \
                pTmp->next);
            ++i;
        }
    	pTmp = pTmp->next;
    }
    putchar('\n');
}
/* 맨 앞 위치에 데이터 추가 함수 */
// nParam : 호출자가 메모리를 동적으로 할당한 후 값을 설정하여 전달
int InsertAtHead(const USERDATA *pParam)
{
    NODE *pNewNode = (NODE *)malloc(sizeof(NODE));
    memset(pNewNode, 0, sizeof(NODE));

    pNewNode->pData = (USERDATA *)pParam;

    pNewNode->prev = g_pHead;
    pNewNode->next = g_pHead->next;

    g_pHead->next = pNewNode;
    g_pHead->next->prev = pNewNode;

    return ++g_nSize;
}
/* 맨 뒷 부분 데이터 추가 함수 */
int InsertAtTail(const USERDATA *pParam)
{
    InsertBefore(g_pTail, pParam);
    return g_nSize;
}
/* 해당 노드 뒤에 새로운 노드를 추가하는 함수 */
void InsertBefore(NODE *pDstNode, const USERDATA *pParam)
{
    NODE *pPrev = pDstNode->prev;

    NODE *pNewNode = (NODE *)malloc(sizeof(NODE));
    memset(pNewNode, 0, sizeof(NODE));
    
    pNewNode->pData = (USERDATA *)pParam;

    pNewNode->prev = pPrev;
    pNewNode->next = pDstNode;

    pPrev->next = pNewNode;
    pPrev = pNewNode;

    g_nSize++;
}
/* 해당 인덱스에 새로운 노드를 추가하는 함수 */
int InsertAt(int idx, const USERDATA *pParam)
{
    int i = 0;
    NODE *pTmp = g_pHead->next;

    while (pTmp != g_pTail)
    {
        if (i == idx)
        {
            InsertBefore(pTmp, pParam);
            return g_nSize;
        }
        pTmp = pTmp->next;
        i++;
    }
    InsertAtTail(pParam);
    return g_nSize;
}
NODE *GetAt(int idx)
{
    int i = 0;
    NODE *pTmp = g_pHead->next;

    while (pTmp != g_pTail)
    {
        if (i == idx)
            return pTmp;
        
        pTmp = pTmp->next;
        i++;
    }
    return NULL;
}
/* pszName 데이터와 일치하는 노드 탐색 함수 */
NODE *FindNodeBySzname(const char *pszName)
{
    NODE *pTmp = g_pHead->next;
    while (pTmp != g_pTail)
    {
        if (strcmp(pTmp->pData->szName, pszName))
            return pTmp;
        pTmp = pTmp->next;
    }
    return NULL;
}
/* pszName 데이터와 일치하는 노드 삭제 함수 */
int DeleteNode(const char * pszName)
{
    NODE *pNode = FindNodeBySzname(pszName);

    pNode->prev->next = pNode->next;
    pNode->next->prev = pNode->prev;

    printf("DeleteNode[%p]\n", pNode);

    g_nSize--;

    free(pNode->pData);
    free(pNode);

    return 0;
}
/* 2중 연결 리스트의 전체 크기를 반환하는 함수 */
int GetSize(void)
{
	return g_nSize;
}
/* 2중 연결 리스트의 전체 크기를 반환하는 함수 */
int GetLength(void)
{
	return GetSize();
}
/* 2중 연결 리스트가 비어 있는지 확인하는 함수*/
int IsEmpty(void)
{
	return GetSize();
}
int main(void)
{
	InitList();

    USERDATA *pNewData = (USERDATA *)malloc(sizeof(USERDATA));
    memset(pNewData, 0, sizeof(USERDATA));
    strcpy(pNewData->szName, "BOLEE");
    strcpy(pNewData->szPhone, "010-1234-1234");
    InsertAtTail(pNewData);


    PrintList();
	ReleaseList();
    putchar('\n');

	return 0;
}