package bfs;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class UserSolution {

    public final int MAX_N = 20;
    public final int MAX_HASH = 9999;

    public int n;
    public int[][] initMap = new int[MAX_N + 2][MAX_N + 2];
    public int[][] modifiedMap = new int[MAX_N + 2][MAX_N + 2];
    public List<Candidate>[] candidate = new List[MAX_HASH + 1];

    public class Candidate{
        int r;
        int c;
        boolean isHorizontal;
        boolean isReverse;
        public Candidate(int r, int c, boolean isHorizontal, boolean isReverse){
            this.r = r;
            this.c = c;
            this.isHorizontal = isHorizontal;
            this.isReverse = isReverse;
        }
    }
    // 어떤 구조물이 들어오더라도 한번에 후보군을 찾을 수 있게 해싱하는 것
    public void init(int N, int[][] mMap){
        n = N;

        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                modifiedMap[i + 1][j + 1] = initMap[i + 1][j + 1] = mMap[i][j];

        for (int i = 0; i <= MAX_HASH; i++)
            candidate[i] = new ArrayList<>();

        for (int length = 2; length <= 5; length++){ // mStructure길이 2~5 사이에 올 수 있는 모든 경우의 수 저장해 두기
            for (int i = 1; i <= n; i++){
                for (int j = 1; j + length - 1 <= n; j++){
                    int hash = 0;
                    for (int k = 0; k + 1 < length; k++) // 수평방향으로 mStructure가 그 길이만큼 고도 차이를 누적하고 후보군에 합하기
                        hash = hash * 10 + (initMap[i][j + k + 1] - initMap[i][j + k] + 5);
                    candidate[hash].add(new Candidate(i, j, true, false));

                    int reverseHash = 0;
                    for (int k = length - 1; k - 1 >= 0; k--)
                        reverseHash = reverseHash * 10 + (initMap[i][j + k - 1] - initMap[i][j + k] + 5);
                    if (reverseHash != hash)
                        candidate[reverseHash].add(new Candidate(i, j, true, true));
                }
            }
            for (int i = 0; i + length - 1 <= n; i++){ // 수직방향으로 mStructure가 그 길이만큼 고도 차이를 누적하고 후보군에 합하기
                for (int j  = 1; j <= n; j++){
                    int hash = 0;
                    for (int k = 0; k + 1 < length; k++)
                        hash = hash * 10 + (initMap[i + k + 1][j] - initMap[i + k][j] + 5);
                    candidate[hash].add(new Candidate(i, j, false, false));

                    int reverseHash = 0;
                    for (int k = length - 1; k - 1 >= 0; k--)
                        reverseHash = reverseHash * 10 + (initMap[i + k -1][j] - initMap[i + k][j] + 5);
                    if (reverseHash != hash)
                        candidate[reverseHash].add(new Candidate(i, j, false, true));

                }
            }
        }
    }

    /*
     구조물 mStructure를 1 개 설치했을 때 나타날 수 있는 경우의 수 반환
     설치 지역이 모두 동일하면 같은 경우로 취급
     설치지역이 1개라도 다르면 다른 경우로 취급

     구조물의 높이 차이 누적합으로 후보군 개수 반환
     */

    public int numberOfCandidate(int M, int[] mStructure){
        if (M == 1)
            return n * n;

        int hash = 0;
        for (int i = 0; i + 1 < M; i++)
            hash = hash * 10 + (mStructure[i] - mStructure[i + 1] + 5);
        return candidate[hash].size();
    }

    public boolean[][] check = new boolean[MAX_N + 2][MAX_N + 2];
    public int[] dx = {1, 0, -1, 0};
    public int[] dy = {0, -1, 0, 1};


    // 주어진 해수면에서 잠기지 않은 지역 수 반환
    public int unsubmergedArea(int[][] mMap, int mSeaLevel){

        Queue<int[]> q = new LinkedList<>();
        for(int i = 0; i <= n + 1; i++){ // 초기 변두리 인덱스 q에 담고 visited 표시
            for (int j = 0; j <= n + 1; j++){
                if (i == 0 || i == n + 1 || j == 0 || j == n + 1){
                    q.add(new int[]{i, j});
                    check[i][j] = true;
                }
                else
                    check[i][j] = false;
            }
        }
        while (!q.isEmpty()){
            int[] front = q.poll();
            for(int i = 0; i < 4; i++){
                int[] rear = {front[0] + dx[i], front[1] + dy[i]};
                if (rear[0] >= 1 && rear[0] <= n && rear[1] >= 1 && rear[1] <= n) { // 아직 잠기지 않은 곳인지
                    if (!check[rear[0]][rear[1]] && mMap[rear[0]][rear[1]] < mSeaLevel){ // 잠겨야 하는 곳인지
                        q.add(rear);
                        check[rear[0]][rear[1]] = true;
                    }
                }
            }
        }
        // 잠기지 않은 지역 갯수 반환
        int ret = 0;
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= n; j++)
                if (!check[i][j])
                    ret++;
        return ret;
    }
    // 해수면이 mSeaLevel만큼 상승하여도 바다에 잠기지 않고 남아 있는 지역 수가 최대가 되도록 구조물 설치했을 때 그 개수 반환
    public int maxArea(int M, int[] mStructure, int mSeaLevel){
        int ret = -1;
        if (M == 1){
            for (int i = 1; i <= n; i++){
                for (int j = 1; j <= n; j++){
                    modifiedMap[i][j] = initMap[i][j] + mStructure[0];
                    ret = Math.max(ret, unsubmergedArea(modifiedMap, mSeaLevel));
                    modifiedMap[i][j] = initMap[i][j];
                }
            }
            return ret;
        }

        int hash = 0;
        for (int i = 0; i + 1 < M; i++)
            hash = hash * 10 + (mStructure[i] - mStructure[i + 1] + 5);

        for (Candidate wall : candidate[hash]) { // 후보군 별 수평방향 수직 방향 구분
            if (wall.isHorizontal) { // 수평방향일 때 역순인지 아닌지에 따라 
                int height = mStructure[0] + (wall.isReverse ? initMap[wall.r][wall.c + M - 1] : initMap[wall.r][wall.c]);
                for (int i = 0; i < M; i++)
                    modifiedMap[wall.r][wall.c + i] = height;
                ret = Math.max(ret, unsubmergedArea(modifiedMap, mSeaLevel));
                for (int i = 0; i < M; i++)
                    modifiedMap[wall.r][wall.c + i] = initMap[wall.r][wall.c + i];
            }
            else {
                int height = mStructure[0] + (wall.isReverse ? initMap[wall.r + M - 1][wall.c] : initMap[wall.r][wall.c]);
                for (int i = 0; i < M; i++)
                    modifiedMap[wall.r + i][wall.c] = height;
                ret = Math.max(ret, unsubmergedArea(modifiedMap, mSeaLevel));
                for (int i = 0; i < M; i++)
                    modifiedMap[wall.r + i][wall.c] = initMap[wall.r + i][wall.c];
            }
        }
        return ret;
    }
}
