import java.util.*;
class Solution {
    int n;
    int lenWord;
    int minChange = Integer.MAX_VALUE;

    public int solution(String begin, String target, String[] words) {
        n = words.length;
        lenWord = begin.length();
        boolean[] visited = new boolean[n];

        if (!hasTarget(words, target)) return 0;
        dfs(0, visited, begin, target, words);
        return minChange;
    }
    private void dfs(int cnt, boolean[] visited, String w, String t, String[] words){
        if (minChange <= cnt) return;
        if (Objects.equals(w, t))
            minChange = Math.min(minChange, cnt);
        else {
            for (int i = 0; i < n; i++){
                if (visited[i] || countEqualChar(w, words[i]) != 1) continue;
                visited[i] = true;
                dfs(cnt + 1, visited, words[i], t, words);
                visited[i] = false;
            }
        }
    }
    private boolean hasTarget(String[] words, String target){
        for (String word : words){
            if (Objects.equals(target, word)) return true;
        }
        return false;
    }

    private int countEqualChar(String w1, String w2){
        int cnt = 0;
        for (int i = 0; i < lenWord; i++)
            if (!Objects.equals(w1.charAt(i), w2.charAt(i))) cnt++;
        return cnt;
    }
}