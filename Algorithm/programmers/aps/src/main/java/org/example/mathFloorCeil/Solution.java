package org.example.mathFloorCeil;


/**
 * 두 원 사이의 정수 쌍
 * <p>
 * 로직
 * 1. 좌표 축에 있는 정수는 별도로 구한다. r2 - r1 + 1
 * 2. 두원의 방정식을 구한다. y = Math.sqrt(r ** 2 - x ** 2)
 * 3. 1 ~ r1까지 y2 - y1 사이 정수의 개수를 더한다.
 * 4. r1 + 1부터 r2 - 1까지 y2 - y1 사이 정수의 개수를 더한다.
 * 5. 결과에 4를 곱한다.
 * <p>
 * 여기서 주의할 점은 큰 원은 소수점을 버리고 작은점은 올림을 한다는 점이다.
 */

class Solution {
    static long R1SQUARE, R2SQUARE;

    public long solution(int r1, int r2) {
        R1SQUARE = (long) Math.pow(r1, 2);
        R2SQUARE = (long) Math.pow(r2, 2);

        long answer = 0;
        answer += r2 - r1 + 1;
        double to;
        for (int i = 1; i < r1; i++) {
            answer += Math.floor(circleEquation(i, R2SQUARE)) - Math.ceil(circleEquation(i, R1SQUARE)) + 1;

        }
        for (int i = r1; i < r2; i++) {
            answer += Math.floor(circleEquation(i, R2SQUARE));
        }
        return answer * 4;
    }

    private static double circleEquation(int x, long RSQUARE) {
        return (double) Math.sqrt(RSQUARE - Math.pow(x, 2));
    }
}