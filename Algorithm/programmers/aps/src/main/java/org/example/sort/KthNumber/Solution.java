package org.example.sort.KthNumber;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        int[] arr = new int[array.length + 1];
        arr[0] = 0;
        for (int i = 1; i <= array.length; i++)
            arr[i] = array[i - 1];

        List<Integer> subList;
        for (int k = 0; k < commands.length; k++) {
            int[] c = commands[k];
            int i = 1;
            subList = new ArrayList<>();
            subList.add(0);
            for (int j = c[0]; j <= c[1]; j++)
                subList.add(arr[j]);

            Collections.sort(subList);

            answer[k] = subList.get(c[2]);
        }

        return answer;
    }
}