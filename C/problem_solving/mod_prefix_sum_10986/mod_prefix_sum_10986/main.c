//
//  main.c
//  mod_prefix_sum_10986
//
//  Created by Lee Wonil on 5/9/24.
// 아이디어 : 누적 값의 나머지를 저장해두고 나머지의 차가 0인 케이스 세기 !
// 1st : 시간 초과

#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int N, M;
    scanf("%d %d", &N, &M);
    int mod_prefix_sums[N + 1];
    mod_prefix_sums[0] = 0;
    
    int input, res = 0;
    for (int i = 1; i <= N; i++){
        scanf("%d", &input);
        mod_prefix_sums[i] = (input + mod_prefix_sums[i - 1]) % M;

        for (int j = 0; j < i; j++){
            if ((mod_prefix_sums[i] - mod_prefix_sums[j]) == 0){
                res++;
            }
        }
        
    }
    printf("%d", res);
    
    return 0;
}
