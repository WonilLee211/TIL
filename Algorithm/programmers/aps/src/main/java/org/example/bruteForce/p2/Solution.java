package org.example.bruteForce.p2;

/**
 * 12345 5
 * 21232425 8
 * 3311224455 10
 * <p>
 * 논리
 * 1번 2번 3번
 * 정답을 돌면서 확인
 * 해당 인덱스 값을 1번2번3번 반복인덱스로 나눈 값과 각 번호별 정담과 비교
 * 일치하면 해당 번호에 cntAnswer++
 **/

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    public int[] solution(int[] answers) {
        int[] ans1 = new int[]{1, 2, 3, 4, 5};
        int[] ans2 = new int[]{2, 1, 2, 3, 2, 4, 2, 5};
        int[] ans3 = new int[]{3, 3, 1, 1, 2, 2, 4, 4, 5, 5};

        int p1 = 5;
        int p2 = 8;
        int p3 = 10;

        List<Integer> cnts = new ArrayList<>();
        for (int i = 0; i < 3; i++)
            cnts.add(0);

        int idx;
        for (int i = 0; i < answers.length; i++) {
            idx = i % p1;
            if (answers[i] == ans1[idx])
                cnts.set(0, cnts.get(0) + 1);
            idx = i % p2;
            if (answers[i] == ans2[idx])
                cnts.set(1, cnts.get(1) + 1);
            idx = i % p3;
            if (answers[i] == ans3[idx])
                cnts.set(2, cnts.get(2) + 1);
        }

        int maxV = Collections.max(cnts);
        List<Integer> answer = new ArrayList<>();
        for (int i = 0; i < 3; i++)
            if (maxV == cnts.get(i))
                answer.add(i + 1);

        int[] answerArray = new int[answer.size()];
        for (int i = 0; i < answer.size(); i++) {
            answerArray[i] = answer.get(i);
        }
        return answerArray;
    }
}