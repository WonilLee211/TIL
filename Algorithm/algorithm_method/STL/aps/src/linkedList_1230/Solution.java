package linkedList_1230;

import java.io.*;
import java.util.StringTokenizer;

public class Solution {

    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    static class Node {
        int data;
        Node next;

        public Node(int data){
            this.data = data;
            this.next = null;
        }
    }

    static class LinkedList{
        Node head;
        Node tail;

        public LinkedList(){
            this.head = null;
        }

        void insert(int idx, int[] dataList){
            Node cur = head;
            int start_idx = 0;
            if (idx == 0){
                if (head != null){
                    Node newNode = new Node(dataList[0]);
                    newNode.next = head;
                    head = newNode;
                }
                else head = new Node(dataList[0]);

                idx = 1;
                start_idx = 1;
            }

            for (int i = 1; i < idx; i++) cur = cur.next;

            for (int i = start_idx; i < dataList.length; i++){
                Node newNode = new Node(dataList[i]);
                newNode.next = cur.next;
                cur.next = newNode;
                cur = newNode;
            }
            if (cur.next == null){
                tail = cur;
            }
        }

        void delete(int idx, int cnt){

            Node cur = head;
            if (idx == 0){
                for (int i = 0; i < cnt; i++){
                    cur = cur.next;
                }
                head = cur;
                return;
            }
            for (int i = 1; i < idx ; i++){
                cur = cur.next;
            }
            Node end = cur;
            for (int i = 0; i < cnt; i++){
                cur = cur.next;
            }
            end.next = cur.next;
            if (end.next == null){
                tail = end;
            }
        }

        void add(int data){ // 제일 뒤에 추가하기
            Node cur = tail;
            Node newNode = new Node(data);
            tail.next = newNode;
            tail = newNode;
        }

        void print() throws Exception {  // 출력하기
            int cnt = 10;
            Node cur = head;
            while(--cnt >=0) {
                bw.write(cur.data +" ");
                cur = cur.next;
            }
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int testcase = 10;

        for (int tc = 1 ; tc <= testcase ; tc++ ){
            bw.append('#').append(String.valueOf(tc)).append(' ');

            LinkedList list = new LinkedList();
            int N = Integer.parseInt(br.readLine());
            StringTokenizer st = new StringTokenizer(br.readLine());
            int[] initArr = new int[N];

            for (int i = 0; i < N; i++){
                initArr[i] = Integer.parseInt(st.nextToken());
            }
            list.insert(0, initArr);

            int M = Integer.parseInt(st.nextToken());
            st = new StringTokenizer(br.readLine());

            for (int i = 0 ; i < M; i++){
                char cmd = st.nextToken().charAt(0);
                int x, y;
                switch (cmd){
                    case 'I':
                        x = Integer.parseInt(st.nextToken());
                        y = Integer.parseInt(st.nextToken());
                        int[] temp = new int[y];
                        for (int j = 0; j < y; j++) {
                            temp[j] = Integer.parseInt(st.nextToken());
                        }
                        list.insert(x, temp);
                        break;
                    case 'D':
                        x = Integer.parseInt(st.nextToken());
                        y = Integer.parseInt(st.nextToken());
                        list.delete(x, y);
                        break;
                    case 'A':
                        y = Integer.parseInt(st.nextToken());
                        for (int j = 0; j < y; j++) {
                            list.add(Integer.parseInt(st.nextToken()));
                        }
                        break;
                }
            }
            list.print();
            bw.write("\n");
        }
        bw.flush();
        br.close();
        bw.close();
    }
}
