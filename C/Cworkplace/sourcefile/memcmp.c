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
    memcpy(parr[0], arr2, sizeof(int) * 10);
    memcpy(parr[1], arr3, sizeof(int) * 10);
    memcpy(parr[2], arr4, sizeof(int) * 10);
    
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
