package samsungTest1.p1;

import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

public class Main {
    static BufferedReader br;

    static {
        try {
            br = new BufferedReader(new FileReader("C:\\Users\\multicampus\\Desktop\\LWI\\TIL\\Algorithm\\code tree\\untitled\\src\\input.txt"));
        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        }
    }

    //    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    static int sr, sc, er, ec, n, totalLength, minLenght;
    static List<Coin> coins = new ArrayList<>();
    static List<Coin> selectedCoins = new ArrayList<>();
    static int[][] visited;
    static char[][] map;

    public static class Coin{
        int r, c, num;
        public Coin(int r, int c, int num) {
            this.r = r;
            this.c = c;
            this.num = num;
        }

        public int getNum() {
            return this.num;
        }
    }
    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        map = new char[n][n];
        minLenght = 1<<9;
        for (int i = 0; i < n; i++){
            String w = br.readLine();
            for (int j = 0; j < n; j++){
                if (Objects.equals(w.charAt(j), 'E')){
                    er = i;
                    ec = j;
                }
                else if (Objects.equals(w.charAt(j), 'S')){
                    sr = i;
                    sc = j;
                }
                else if (!Objects.equals(w.charAt(j), '.') && !Objects.equals(w.charAt(j), '#'))
                    coins.add(new Coin(i, j, Integer.parseInt(String.valueOf(w.charAt(j)))));
                map[i][j] = w.charAt(j);
            }
        }
        selectCoin(0, 0);
        if (minLenght == 1<<9){
            System.out.println(-1);
        }
        else{
            System.out.println(minLenght);
        }

    }
    public static void selectCoin(int depth,int index) {

        if (depth == 3) {
            findEXIT();
            return;
        }
        if (index == coins.size()) {
            return;
        }
        selectedCoins.add(coins.get(index));
        selectCoin(depth + 1, index + 1);
        selectedCoins.remove(selectedCoins.size() - 1);
        selectCoin(depth, index + 1);
    }
    public static void findEXIT(){

        List<Coin> sortedCoin = selectedCoins.stream().sorted(Comparator.comparingInt(Coin::getNum)).collect(Collectors.toList());
        sortedCoin.add(0, new Coin(sr, sc, -1));
        sortedCoin.add(new Coin(er, ec, -1));
        totalLength = 0;
        for (int i = 0; i < sortedCoin.size()-1; i++){
            int res = bfs(sortedCoin.get(i), sortedCoin.get(i + 1));
            if (res == -1){
                return;
            }
            totalLength += res;
        }
        minLenght = Math.min(minLenght, totalLength);
    }
    public static int bfs(Coin fr, Coin to){
        int[] dr = {0, 0, -1, 1};
        int[] dc = {-1, 1, 0, 0};
        visited = new int[n][n];
        for (int i = 0; i < n; i++){
            for (int j = 0; j < n; j++){
                visited[i][j] = 0;
            }
        }
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{fr.r, fr.c});
        visited[fr.r][fr.c] = 1;
        while(!q.isEmpty()){
            int[] now = q.poll();
            if (now[0] == to.r && now[1] == to.c){
                return visited[to.r][to.c] - 1;
            }

            for(int i = 0; i < 4; i++){
                int nr = now[0] + dr[i];
                int nc = now[1] + dc[i];
                if (canGo(nr, nc)){
                    visited[nr][nc] = visited[now[0]][now[1]] + 1;
                    q.add(new int[]{nr, nc});
                }
            }
        }
        return - 1;
    }

    public static boolean canGo(int r, int c){
        return r >= 0 && r < n && c >= 0 && c < n && visited[r][c] == 0 && !Objects.equals(map[r][c], '#');
    }
}

