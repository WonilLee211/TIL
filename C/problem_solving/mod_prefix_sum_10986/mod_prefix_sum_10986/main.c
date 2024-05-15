//
//  main.c
//  mod_prefix_sum_10986
//
//  Created by Lee Wonil on 5/9/24.
// 아이디어 : 누적 값의 나머지를 저장해두고 나머지의 차가 0인 케이스 세기 !
// 1st : 시간 초과
// 2nd : 누적합의 나머지가 같은 값끼리 조합 수를 계산 >> 틀림
#include <stdio.h>

int main(void) {
    int N, M;
    scanf("%d %d", &N, &M);
    long mod_prefix_sums[N + 1];
    mod_prefix_sums[0] = 0;
    int cnt_same_mods[1000] = {0, };
    
    int input, res = 0;
    for (int i = 1; i <= N; i++){
        scanf("%d", &input);

        mod_prefix_sums[i] = (input + mod_prefix_sums[i - 1]) % M;
        
        cnt_same_mods[mod_prefix_sums[i]]++;
    }
        
    res += cnt_same_mods[0];
    for (int i = 0; i < M; i++){
        int num = cnt_same_mods[i];
        res += num * (num - 1) / 2;
    }
    printf("%d", res);
    
    return 0;
}
