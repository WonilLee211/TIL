package org.example.sort.H_index;

import java.util.Arrays;

/**
 * 어떤 과학자가 발표한 논문 n편 중,
 * h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면
 * h의 최댓값이 이 과학자의 H-Index
 *
 * 로직
 * 1. 논문 별 인용 횟수 배열을 내림차순 정렬
 * 2. h index를 0부터 정렬된 배열과 비교하여 논문의 인용 횟수보다 작다면 1더하며 반복한다.
 * 3. h-index가 논문의 인용 수와 같거나 커진다면 멈춘다.
 */
class Solution {
    public int solution(int[] citations) {

        int n = citations.length;
        Arrays.sort(citations);
        for (int i = 0; i < n / 2; i++) {
            int temp = citations[i];
            citations[i] = citations[n - 1 - i];
            citations[n - 1 - i] = temp;
        }
        int h = 0;
        for (int i = 0; i < n; i++) {
            if (citations[i] > h) h++;
            else break;
        }
        return h;
    }
}