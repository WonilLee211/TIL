package maxHeapMinHeap;


import java.io.*;
import java.util.*;


class Solution {


    private static final int MOD = 20171109;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());

        for (int t = 1; t <= T; t++) {

            PriorityQueue<Integer> minH = new PriorityQueue<>((i1, i2) -> i1 - i2);
            PriorityQueue<Integer> maxH = new PriorityQueue<>((i1, i2) -> i2 - i1);

            StringTokenizer st = new StringTokenizer(br.readLine());

            int N = Integer.parseInt(st.nextToken());
            int A = Integer.parseInt(st.nextToken());

            minH.add(A);
            int answer = 0;
            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                int num1 = Integer.parseInt(st.nextToken());
                int num2 = Integer.parseInt(st.nextToken());

                if (num1 > num2) {
                    minH.add(num1);
                    maxH.add(num2);
                } else {
                    minH.add(num2);
                    maxH.add(num1);
                }

                while (minH.peek() < maxH.peek()) {
                    int minVal = minH.poll();
                    int maxVal = maxH.poll();
                    minH.add(maxVal);
                    maxH.add(minVal);
                }
                answer = (minH.peek() + answer) % MOD;

            }

            System.out.println("#" + t + " " + answer);
        }

    }
}

//
//public class hash.Solution {
//
//    static BufferedReader br;
//
//    static {
//        try {
//            br = new BufferedReader(new FileReader("C:\\Users\\multicampus\\Desktop\\LWI\\TIL\\Algorithm\\algorithm_method\\APS_Java\\aps\\src\\input.txt"));
//        } catch (FileNotFoundException e) {
//            throw new RuntimeException(e);
//        }
//    }
//
////    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
//    static StringTokenizer st;
//    static int T, N;
//    static PriorityQueue<Long> maxHeap;
//    static PriorityQueue<Long> minHeap;
//    public static void main(String[] args) throws IOException {
//        T = Integer.parseInt(br.readLine());
//        for (int tc = 1; tc <= T; tc++){
//            bw.append("#").append(String.valueOf(tc)).append(" ");
//            Long ans = 0L;
//            st = new StringTokenizer(br.readLine());
//            N = Integer.parseInt(st.nextToken());
//            Long firstNum = Long.parseLong(st.nextToken());
//            maxHeap = new PriorityQueue<>(Collections.reverseOrder());
//            minHeap = new PriorityQueue<>();
//            maxHeap.add(firstNum);
//            minHeap.add(firstNum);
//            for (int i =  0; i < N; i++ ){
//                st = new StringTokenizer(br.readLine());
//                for (int j =  0; j < 2; j++ ){
//                    Long num = Long.parseLong(st.nextToken());
//                    maxHeap.add(num);
//                    minHeap.add(num);
//                }
//                ans = (ans + findMidNum()) % 20171109;
//            }
//            bw.append(String.valueOf(ans));
//        }
//        bw.flush();
//        br.close();
//        bw.close();
//    }
//    public static Long findMidNum(){
//        Long[] maxH = (Long[]) maxHeap.toArray().clone();
//        Long[] minH = (Long[]) minHeap.toArray().clone();
//        int qSize = maxH.length;
//        Long midNum = null;
//        for (int i = 0; i < qSize; i++){
//            if (Objects.equals(maxH[i], minH[i])){
//                midNum = maxH[i];
//                break;
//            }
//        }
//        return midNum;
//    }
//}
