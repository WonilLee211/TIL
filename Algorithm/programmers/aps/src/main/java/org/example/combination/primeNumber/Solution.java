package org.example.combination.primeNumber;

/**
 * 소수 찾기
 *
 * 로직
 * 1. 주어진 숫자 문자열로 발생할 수 있는 모든 숫자를 조합한다.
 * 2. 조합한 숫자별로 중복 체크한 후 소수인지 판별한다.
 */
class Solution {
    int MAXNUM = 10000000;
    boolean[] visited = new boolean[MAXNUM];
    int answer;
    public int solution(String numbers) {
        visited[0] = true;
        visited[1] = true;
        answer = 0;
        for (int i = 1; i <= numbers.length(); i++)
            getCombs(i, numbers, "", new boolean[numbers.length()]);
        return answer;
    }
    private void getCombs(int depth, String nums, String curr, boolean[] used){
        if (curr.length() == depth && !visited[Integer.parseInt(curr)]){
            int temp = Integer.parseInt(curr);
            visited[temp] = true;
            if (isPrime(temp)) {
                answer++;
            }

        }
        else {
            for (int i = 0; i < nums.length(); i++){
                if (used[i]) continue;
                used[i] = true;
                getCombs(depth, nums, curr + nums.charAt(i), used);
                used[i] = false;
            }
        }
    }
    private boolean isPrime(int num){
        for (int i = 2; i * i <= num; i++)
            if (num % i == 0) return false;
        return true;
    }
}