package org.example.bruteForce.p1;

/**
 * 최소 직사각형
 * 로직
 * 1. 모든 카드들에 대해서 긴 모서리를 가로로 변경한다.
 * 2. 이후 가장 긴 세로를 구한다.
 * 3. 가장 긴 세로와 가장 긴 가로의 곱을 구한다.
 **/

class Solution {
    int maxV, maxH, n;

    public int solution(int[][] sizes) {
        n = sizes.length;

        for (int i = 0; i < n; i++)
            sizes = preprocessData(sizes);
        getMaxVH(sizes);
        return maxV * maxH;
    }

    private int[][] preprocessData(int[][] sizes) {
        for (int i = 0; i < n; i++) {
            if (sizes[i][0] < sizes[i][1])
                switchVerToHori(sizes[i]);
        }
        return sizes;
    }

    private void switchVerToHori(int[] size) {
        int temp;
        temp = size[1];
        size[1] = size[0];
        size[0] = temp;
    }

    private void getMaxVH(int[][] sizes) {
        for (int i = 0; i < n; i++) {
            maxH = Math.max(maxH, sizes[i][0]);
            maxV = Math.max(maxV, sizes[i][1]);
        }
    }
}