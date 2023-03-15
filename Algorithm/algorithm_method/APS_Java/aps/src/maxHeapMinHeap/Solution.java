package maxHeapMinHeap;


import heap.Heap;

import java.io.*;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Solution {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static StringTokenizer st;
    static int T, N;
    static PriorityQueue<Long> maxHeap;
    static PriorityQueue<Long> minHeap;
    public static void main(String[] args) throws IOException {
        T = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= T; tc++){
            Long ans = 0L;
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            Long firstNum = Long.parseLong(st.nextToken());
            maxHeap = new PriorityQueue<>();
            minHeap = new PriorityQueue<>();
            maxHeap.add(firstNum);
            minHeap.add(-firstNum);
            for (int i =  0; i < N; i++ ){
                st = new StringTokenizer(br.readLine());
                Long num1 = Long.parseLong(st.nextToken());
                Long num2 = Long.parseLong(st.nextToken());
                ans = (ans + findMidNum(num1, num2)) / 20171109;
            }
        }
    }
    public static Long findMidNum(Long n1, Long n2){
        maxHeap.add(n1);
        maxHeap.add(n2);
        minHeap.add(-n1);
        minHeap.add(-n2);

        for


    }
}
