#include <stdio.h>

int add_element(int (*arr)[2], int row);
int main(){
    int arr[3][2];
    int i, j;

    for (i = 0; i < 3; i++){
        for (j = 0; j < 2; j++){
            scanf("%d", &arr[i][j]);
        }
    }

    add_element(arr, 3);

    for (i = 0; i < 3; i++){
        for (j = 0; j < 2; j++){
            printf("arr[%d][%d] : %d \n", i, j, arr[i][j]);
        }
    }
    return 0;
}

int add_element(int (*arr)[2], int row) {
    int i, j;

    for (i = 0; i < row; i++){
        for (j = 0; j < 2; j++){
            arr[i][j]++;
        }
    }
    return 0;
}