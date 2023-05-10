package org.example.scheduling;
/**
 * 스케쥴링 문제
 * <p>
 * input
 * [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]
 * <p>
 * 로직
 * 1. targets을 종료 시점기준으로 오름차순으로 정렬한다.
 * 2. 종료 시점을 기록한다. 사용한 미사일 수를 1로 초기화한다.
 * 3. target들의 시작점을 확인한다.
 * 4. 현재 종료 시점보다 시작점이 같거나 크다면 미사일을 추가한다.
 * 5. 현재 종료 시점보다 시작점이 작다면 패스한다.
 */

import java.util.Arrays;

class Solution {
    public int solution(int[][] targets) {
        int answer = 1;
        // 1. 종료시점 기준 오름차순 정렬
        Arrays.sort(targets, (a1, a2) ->
                {
                    if (a1[1] == a2[1])
                        return a1[0] - a2[0];
                    return a1[1] - a2[1];
                }
        );
        int endT = targets[0][1];
        for (int[] target : targets) {
            if (target[0] >= endT) {
                endT = target[1];
                answer++;
            }
        }
        return answer;
    }
}