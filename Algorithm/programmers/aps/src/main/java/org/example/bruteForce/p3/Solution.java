package org.example.bruteForce.p3;

/**
 * 로직
 * 1. brown + yellow는 넓이
 * 2. 넓이가 나눠지는 가로에 대해서
 * 3. 가로 * 2 + (세로 - 2) * 2가 brown과 같을 경우 정답
 **/
class Solution {
    public int[] solution(int brown, int yellow) {
        int area = brown + yellow;
        int bound = area / 2;
        int h;
        int[] answer = new int[]{0, 0};
        for (int i = 1; i <= bound; i++){
            if (area % i == 0){
                h = area / i;
                if (brown == (i * 2 + (h - 2) * 2)){
                    answer[0] = i;
                    answer[1] = h;
                }
            }
        }
        return answer;
    }
}