'''
점검 시간 1시간
1시간동안 이동할 수있는 거리 제각각
최소한의 친구들을 보내서 점검하기 나머지는 내부 공사 돕기
정북에서 시계 또는 반시계방향으로 돌기

취약지점의 위치가 담긴 배열 weak
각 친구가 이동할 수 있는 거리 dist
취약지점을 점검하기 위해 보내야하는 친구의 수 최솟값

n  = 1 ~ 200
weak = 1 ~ 15


논리
- 취약점 배열을 2배로 만들어서 시계방향으로만 탐색하기
- 친구의 순서도 결과에 영향을 주기 때문에 모든 순열을 탐색
- 시작점은 weak[0] / cnt = 1
- weak[0] + 친구[0]이 weak[1]보다 크면 cnt += 1
- weak[0] + 친구[0]이 weak[1]보다 작으면, weak[0] + 친구[0] + 친구[1]
- 만약 cnt == len(weak)일 때 친구 수 작은 수로 갱신
- 다돌았는데 cnt < len(weak)일 땐 pass
- 현재의 친구 수보다 커지면 break

weak
1 5 6 10 13 17 18 22
 457 11
  8 911
    9101317
      13 14 16
3124



'''

n = 6
weak = [1, 2, 4, 5]
dist =[1, 1]

m = len(weak)
num_friends = len(dist)
weak += [i + n for i in weak]
ans = len(dist) + 1

def check_wall(friends):
    global ans

    for i in range(m):
        now = weak[i] + friends[0]
        j = cnt = 1
        k = 1
        while k < len(dist):

            while now >= weak[i + j]:  # 현재가 취약 지점보다 클 때까지 취약지점 이동
                if j == m:
                    break
                j += 1

            if j < m:
                # 현재가 취약지점보다 작다면
                now = weak[i + j] + friends[k]
                j += 1
                k += 1
                cnt += 1

            if cnt > ans or j == m:
                break

        for friend in friends[1:]:
            while now >= weak[i + j]:  # 현재가 취약 지점보다 클 때까지 취약지점 이동
                if j == m:
                    break
                j += 1

            if j < m:
                # 현재가 취약지점보다 작다면
                now = weak[i + j] + friend
                j += 1
                cnt += 1

            if cnt > ans or j == m:
                break

        if j == m:
            ans = min(ans, cnt)


def perm(arr, d, visited):
    if d == num_friends:
        check_wall(arr)
    else:
        for i in range(num_friends):
            if visited & (1 << i):
                continue
            arr.append(dist[i])
            perm(arr, d + 1, visited ^ (1 << i))
            arr.pop()

perm([], 0, 0)

if ans == len(dist) + 1:
    ans = -1

print(ans)