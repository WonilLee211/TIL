#include <stdio.h>
#include <stdbool.h>

/* 외판원 문제
 * n 개의 큰 도시가 있을 때
 * 한 도시에서 모든 도시를 한 번씩 방문하고 시작 도시로 돌아옴
 * 판매원이 여행해야 할 최소 거리를 구하는 문제
 *
 */

#define INF 2e9
#define MAX 30

int numCity, cntVisit; // 도시의 수
int dist[MAX][MAX]; // 두 도시간 거리를 저장하는 배열
int best = INF; // 지금까지 찾은 최적해
int path[MAX];
int visited[MAX];


/* 경로의 길이를 best 전역변수에 갱신
 * city : 현재 위치
 * cntVisit : 방문 횟수
 * currentLength : 지금까지 만든 경로의 길이
 */
void search(int here, int cntVisit, int currentLength);
void updateBest(int src);
void printPath(int distance);

void search(int here, int cntVisit, int currentLength){
    path[cntVisit] = here;
    visited[here] = true;
    if (cntVisit == numCity - 1){
        updateBest(currentLength + dist[here][path[0]]);
        printPath(currentLength + dist[here][path[0]]);
        visited[here] = false;
        path[cntVisit] = -1;
        return;
    }
    for (int next = 0; next < numCity; next++){
        if (visited[next] || dist[here][next] == 0) continue;
        search(next, cntVisit + 1, currentLength + dist[here][next]);
    }
    visited[here] = false;
    path[cntVisit] = -1;
}
void updateBest(int src){
    best = best < src ? best : src;
}
void printPath(int distance){
    for (int i = 0; i < numCity; i++)
        printf("%d ", path[i]);
    printf(": %d\n", distance);
    return;
}
int main(){
    scanf("%d", &numCity);
    for (int i = 0; i < numCity; i++){
        path[i] = -1;
        for (int j = 0; j < numCity; j++)
            scanf("%d", &dist[i][j]);
    }
    putchar('\n');
    for (int i = 0; i < numCity; i++){
        search(i, 0, 0);
    }
    printf(": %d\n", best);
    return 0;
}

