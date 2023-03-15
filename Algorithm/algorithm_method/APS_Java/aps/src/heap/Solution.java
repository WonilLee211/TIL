package heap;


import java.io.*;
import java.util.StringTokenizer;

/** heap 연산
 * 1. 삽입
 * 2. 루트 삭제
 *
 */
public class Solution {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static StringTokenizer st;
    static int T, N;

    public static void main(String[] args) throws IOException {
        T = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= T; tc++) {
            bw.append("#").append(String.valueOf(tc));
            N = Integer.parseInt(br.readLine());
            Heap hp = new Heap();
            for (int i = 0; i < N; i++){
                st = new StringTokenizer(br.readLine());
                int op = Integer.parseInt(st.nextToken());
                if (op == 1) hp.add(Integer.parseInt(st.nextToken()));
                else if (op == 2){
                    if (hp.isEmpty()) bw.append(" ").append("-1");
                    else bw.append(" ").append(String.valueOf(hp.poll()));
                }
            }
            bw.append("\n");
        }
        bw.flush();
        br.close();
        bw.close();
    }
}
class Heap{
    int tail = 0;
    int[] heap;

    Heap() {
        heap = new int[100001];
    }

    void add(int num){
        heap[++tail] = num;
        int child = tail;

        while (child > 1) {
            int parent = child / 2;
            if (heap[parent] < heap[child]){
                int temp = heap[child];
                heap[child] = heap[parent];
                heap[parent] = temp;
                child = parent;

            }
            else return;
        }
    }

    void heapify(){
        int cur = 1;
        while ((cur * 2  + 1) <= tail){
            int larger = cur;
            int left = cur * 2;
            int right = cur * 2 + 1;

            if (heap[larger] < heap[left]) larger = left;
            if (heap[larger] < heap[right]) larger = right;
            if (larger != cur) {
                int temp = heap[cur];
                heap[cur] = heap[larger];
                heap[larger] = temp;
                cur = larger;
            }
            else {
                return;
            }
        }
    }

    int poll(){
        int top = 1;
        int res = heap[top];
        heap[top] = heap[tail];
        heap[tail] = 0;
        tail--;
        heapify();
        return res;
    }

    boolean isEmpty(){return tail == 0;}

}