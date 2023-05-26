import java.util.*;
/**
 * dfs
 * 하나의 경로를 찾은 후 지금 보다 정렬이 잘되어 있으면 변경
 * 찾은 경로보다 정렬이 오름차순이 아닌 것들은 가지치기
 **/
class Solution {
    int n;
    String[] route;
    public String[] solution(String[][] tickets) {

        String[] answer = {};
        n = tickets.length;

        route = new String[n + 1];
        String[] comb = new String[n + 1];
        Arrays.fill(route, "");
        Arrays.fill(comb, "");


        comb[0] = "ICN";
        dfs(1, comb, new boolean[n],tickets);
        return route;
    }
    private void dfs(int depth, String[] comb, boolean[] visited,String[][] tickets){
        if (depth == n +1 && checkAcsOrder(comb))
            updateRoute(comb);
        else {
            for (int i = 0; i < n; i++){
                if (visited[i] || comb[depth - 1].compareTo(tickets[i][0]) != 0) continue;
                visited[i] = true;
                comb[depth] = tickets[i][1];
                dfs(depth + 1, comb, visited, tickets);
                visited[i] = false;
                comb[depth] = "";
            }
        }
    }
    private boolean checkAcsOrder(String[] comb){
        if (Objects.equals(route[0], "")) return true;

        for (int i = 0; i < n + 1; i++){
            if (comb[i].compareTo(route[i]) == 0) continue;
            else if (comb[i].compareTo(route[i]) < 0) return true;
            else return false;
        }
        return false;
    }
    private void updateRoute(String[] comb){
        for (int i = 0; i < n + 1; i++)
            route[i] = comb[i];
    }
}