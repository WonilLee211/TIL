package org.example.sort.biggestNumber;

import java.util.Arrays;
import java.util.Objects;


/**
 * 가장 큰 수 만들기
 * 정수로 이루어진 배열을 값을 정렬하여 최대의 값으로 만들어야 함.
 * 이는 정렬을 어떻게 할 것인가를 생각하면 되는 문제.
 * 너무 어렵게 생각하고 솔루션을 떠올리지 못했다.
 *
 * 로직
 * 정수 배열을 문자열 배열로 변경
 * 문자열의 정렬 조건을 앞뒤 문자열 합의 대소로 역정렬
 * 정렬된 값들을 합치고 출력
 */
class Solution {
    public String solution(int[] numbers) {
        int n = numbers.length;

        String[] strs = new String[n];
        for (int i = 0; i < n; i++)
            strs[i] = String.valueOf(numbers[i]);

        String biggestNum = "";
        Arrays.sort(strs, (s1, s2) -> (s2 + s1).compareTo(s1 + s2));

        if (Objects.equals(strs[0], "0")) return "0";
        for (String s : strs)
            biggestNum += String.valueOf(s);
        return biggestNum;
    }
}