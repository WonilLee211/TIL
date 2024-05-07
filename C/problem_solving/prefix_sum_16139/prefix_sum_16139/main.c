//
//  main.c
//  prefix_sum_16139
//
//  Created by Lee Wonil on 5/5/24.

#include <stdio.h>
#include <string.h>

#define STR_MAX (200001)
#define ALPHA_CNT (25 + 1)
int prefix_map[ALPHA_CNT][STR_MAX];

int main(void) {
    char str[STR_MAX];
    int N;
    unsigned long str_len;
    
    scanf("%s", str);
    while (getchar() != '\n');
    scanf("%d", &N);
    while (getchar() != '\n');

    str_len = strlen(str);

    int idx;
    for (int i = 0; i < str_len; i++){
        idx = (int)str[i] - (int)'a';
        prefix_map[idx][i + 1] += 1;
        for (int j = 0; j < ALPHA_CNT; j++){
            prefix_map[j][i + 1] += prefix_map[j][i];
        }
    }
    
    char c[N];
    int fr[N], to[N];
    
    for (int i = 0; i < N; i++){
        scanf("%c %d %d", &c[i], &fr[i], &to[i]);
        while (getchar() != '\n');
        to[i]++;

        idx = (int)c[i] - (int)'a';
        printf("%d\n", prefix_map[idx][to[i]] - prefix_map[idx][fr[i]]);
    }

    return 0;
}
