package brute_force.brute_force_digGold;
import java.util.*;
import java.io.*;
/*
n×n크기의 이차원 영역에 파묻힌 금을 손해를 보지 않는 선에서 최대한 많이 채굴
 채굴은 반드시 마름모 모양으로 단 한 번
 마름모 모양을 지키는 한 이차원 영역을 벗어난 채굴도 가능하지만 이차원 영역 밖에 금은 존재하지 않음
 마름모 모양이란 특정 중심점을 기준으로 K번 이내로 상하좌우의 인접한 곳으로 이동하는 걸 반복했을 때
 갈 수 있는 모든 영역이 색칠되어 있는 모양을 의미
 \\codetreepublic\\problems\\19\\images\\10f00846-3d6d-420f-9838-f1c8756a3251.png
 이 때 채굴에 드는 비용은 마름모 안의 격자 갯수만큼 들어가며, 이는 K∗K+(K+1)∗(K+1)로 계산.
 금 한 개의 가격이 m일 때, 손해를 보지 않으면서 채굴할 수 있는 가장 많은 금의 개수를 출력


로직
1. grid 위치별로 k마다 구할 수 있는 골드 수 세고 손해인지 아닌지 판단하고 최대값 갱신하기

*/

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int n, m, ans;
    static int[][] grid = new int[20][20];

    public static void main(String[] args) throws Exception {
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        for (int i = 0; i < n; i++){
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) grid[i][j] = Integer.parseInt(st.nextToken());
        }

        for (int i = 0; i < n; i++){
            for (int j = 0; j < n; j++){
                for (int k = 0; k <= 2 * (n - 1); k++){
                    int countGold = mineGold(i, j, k);

                    if (countGold * m >= miningCost(k))
                        ans = Math.max(countGold, ans);
                }
            }
        }
        System.out.println(ans);
    }
    private static int mineGold(int r, int c, int k){
        int gold = 0;
        for (int i = 0; i < n; i++){
            for (int j = 0; j < n; j++){
                if (Math.abs(r - i) + Math.abs(c - j) <= k){
                    gold += grid[i][j];
                }
            }
        }
        return gold;
    }

    private static int miningCost(int k){
        return 2 * k * k + 2 * k + 1;
    }
}