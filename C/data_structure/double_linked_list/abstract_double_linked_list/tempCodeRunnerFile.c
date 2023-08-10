int InsertAtHead(const USERDATA *pParam)
// {
//     NODE *pNewNode = (NODE *)malloc(sizeof(NODE));
//     memset(pNewNode, 0, sizeof(NODE));

//     pNewNode->pData = pParam;

//     pNewNode->prev = g_pHead;
//     pNewNode->next = g_pHead->next;

//     g_pHead->next = pNewNode;
//     g_pHead->next->prev = pNewNode;

//     return ++g_nSize;
// }