//
//  main.c
//  prefix_sum4
//
//  Created by Lee Wonil on 5/4/24.
//

#include <stdio.h>

int main(void) {
    int N, M;
    scanf("%d %d", &N, &M);
    
    int prefix_sum[N + 1];
    prefix_sum[0] = 0;
    
    for (int i = 1; i <= N; i++){
        scanf("%d", &prefix_sum[i]);
        
        prefix_sum[i] += prefix_sum[i - 1];
    }

    for (int k = 0; k < M; k++){
        int i, j;
        scanf("%d %d", &i, &j);
        
        printf("%d\n", prefix_sum[j] - prefix_sum[i-1]);
    }
    return 0;
}
 
