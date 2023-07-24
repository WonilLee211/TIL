#include <stdio.h>

int bubble_sort(int* arr, int num_elements);
int swap(int* pele);
int main(){
    int n, i;

    printf("arr size : ");
    scanf("%d", &n);

    int arr[n];
    for (i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    printf("arr before sorted : ");
    for (i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    bubble_sort(arr, n);

    printf("arr after sorted : ");
    for (i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }

    return 0;
}
int bubble_sort(int* arr, int num_elements){
    int i, j;

    for (i = num_elements - 1; i > 0; i--){
        for (j = 0; j < i; j++){
            if (arr[j] > arr[j + 1]){
                swap(&arr[j]);
            }
        }
    }
    return 0;
}
int swap(int* pele) {
    int temp = *pele;
    *pele = *(pele + 1);
    *(pele + 1) = temp;

    return 0;
}