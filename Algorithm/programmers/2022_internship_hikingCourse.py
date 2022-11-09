'''
n : 지점의 수 1 ~ n 출입구, 쉽터 혹은 산봉우리
양방향 등산로
path = 등산로 정보 [i,j,w]
- i와 j를 연결하는 w 걸리는 시간
intensity : 휴식없이 이동해야 하는 시간
summits : 산봉우리 번호들
gates : 출입구 번호

출입구 중 한 곳에서 출발해서 산봉오리 중  한 곳만 방문한 뒤 다시 원래의 출구로 돌아오는 등산코스
- 출입구는 처음과 끝에, 봉우리는 한번만 포함되어야 함
이러한 규칙을 지키멶서 intensity가 최소가 되는 코스 정하기

[산봉우리 번호, intensity] 출력

논리
- 봉우리에서 입구까지 가는데 가장 작은 indensity로 가는 길
- bfs 탐색
- 백트래킹 : 현재 구한 indensity보다 크면 버리기
- 모든 봉우리에서 탐색 시작
- 봉우리가 있거나 방문했으면 pass
- 입구에 도착했으면 indensity 확인
'''

