package commonAncestor;

import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Solution {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static int V, E, A ,B, ans, cntChild;
    static Node[] nodes;
    static ArrayList<Integer> ancestorA, ancestorB;

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(br.readLine());
        int tc;
        for (tc = 1; tc <= T; tc++){
            StringTokenizer st = new StringTokenizer(br.readLine());

            V = Integer.parseInt(st.nextToken()); // 정점 수
            E = Integer.parseInt(st.nextToken()); // 간선 수
            A = Integer.parseInt(st.nextToken()); // 공통조상을 찾는 노드 1
            B = Integer.parseInt(st.nextToken()); // 공통조상을 찾는 노드 1
            nodes = new Node[V + 1];
            ancestorA = new ArrayList<>();
            ancestorB = new ArrayList<>();

            for (int i = 0; i < V + 1; i++) {
                nodes[i] = new Node();
            }

            st = new StringTokenizer(br.readLine());
            for (int i= 0; i < E ; i++){ //

                int parent = Integer.parseInt(st.nextToken());
                int child = Integer.parseInt(st.nextToken());

                nodes[parent].children.add(child);
                nodes[child].parent = parent;
            }

            transverse(A, ancestorA); // 조상들을 root부터 순서대로 배열에 담기
            transverse(B, ancestorB);

            for (int i = 0; i < V; i++){ // 공통 조상 찾기
                if (!ancestorA.get(i).equals(ancestorB.get(i))) break;
                ans = ancestorA.get(i);
            }
            cntChild = dfs(ans);
            bw.append("#").append(String.valueOf(tc)).append(" ")
                    .append(String.valueOf(ans)).append(" ").append(String.valueOf(cntChild));
            bw.write("\n");
        }
        bw.flush();
        br.close();
        bw.close();
    }

    public static int dfs(int node){
        if (nodes[node].children.size() == 0) return 1;
        int cnt = 1;
        for (int c : nodes[node].children){
            cnt += dfs(c);
        }
        return cnt;
    }
    public static void transverse(int node, ArrayList<Integer> ancestors){
        int parent = nodes[node].parent;
        if (parent != 0) transverse(parent, ancestors);
        ancestors.add(node);
    }

    public static class Node {

        List<Integer> children;
        int parent;

        public Node() {
            this.children = new ArrayList<>();
            this.parent = 0;
        }
    }
}
