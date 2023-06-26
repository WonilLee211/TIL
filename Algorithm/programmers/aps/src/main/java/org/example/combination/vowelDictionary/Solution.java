package org.example.combination.vowelDictionary;

class Solution {
    char[] alphabet = new char[]{' ', 'A', 'E', 'I', 'O', 'U'};
    int N = 3906; // 5**5 + 5**4 ...  -- 사전 경우의 수
    int r = 0;

    public int solution(String word) {
        int i;
        char[][] dictionary = new char[N][5];
        char[] charInWord = new char[5];
        int len = word.length();

        combination(dictionary, 0);

        for (int j = 0; j < len; j++)
            charInWord[j] = word.charAt(j);

        boolean isMatched;
        for (i = 1; i < N; i++) {
            isMatched = true;
            char[] wordInDic = dictionary[i];
            for (int j = 0; j < 5; j++) {
                if (charInWord[j] != wordInDic[j]) {
                    isMatched = false;
                    break;
                }
            }
            if (isMatched)
                break;
        }

        return i;
    }
    // 사전 채우기
    private void combination(char[][] dic, int c) {
        if (r < N - 1 && c < 5) {
            for (int i = 0; i < 5; i++) {
                for (int j = 0; j < c; j++)
                    dic[r + 1][j] = dic[r][j];
                dic[r + 1][c] = alphabet[i + 1];
                r++;
                combination(dic, c + 1);
            }
        }
    }
}
