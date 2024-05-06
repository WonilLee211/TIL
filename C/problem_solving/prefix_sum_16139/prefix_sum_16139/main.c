    //
    //  main.c
    //  prefix_sum_16139
    //
    //  Created by Lee Wonil on 5/5/24.
    //
    // 122 97
    #include <stdio.h>
    #include <string.h>
    #include <stdlib.h>

    int STR_MAX = 200001;

    int main(void) {
        char str[STR_MAX];
        int N;
        unsigned long str_len;
        
        scanf("%s", str);
        while (getchar() != '\n');
        scanf("%d", &N);
        while (getchar() != '\n');

        str_len = strlen(str);

        int **prefix_map = (int **)calloc(123, sizeof(int *));
        
        for (int i = 0; i < 123; i++){
            prefix_map[i] = (int *)calloc(str_len + 1, sizeof(int));
        }

        for (int i = 0; i < 123; i++){
            prefix_map[i][0] = 0;
        }
        
        for (int i = 0; i < str_len; i++){
            prefix_map[str[i]][i + 1] += 1;
            for (int j = 0; j < 123; j++){
                prefix_map[j][i + 2] += prefix_map[j][i + 1];
            }
        }
        
        char c[N];
        int fr[N], to[N];
        
        for (int i = 0; i < N; i++){
            scanf("%c %d %d", &c[i], &fr[i], &to[i]);
            while (getchar() != '\n');
            to[i]++;
        }
        for (int i = 0; i < N; i++){
            printf("%d\n", prefix_map[(int)c[i]][to[i]] - prefix_map[(int)c[i]][fr[i]]);
        }

        for (int i = 0; i < 123; i++){
            free(prefix_map[i]);
        }
        free(prefix_map);
        
        return 0;
    }
