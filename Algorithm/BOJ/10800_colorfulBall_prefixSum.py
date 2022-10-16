import sys
sys.stdin = open('input.txt')

'''
크기가 작거나 색이 다른 공만 더할 수 있는 문제
1. 입력받은 데이터를 크기를 기준으로 오름차순 정렬
2. 순차적으로 더해감
    - 크기가 해당 위치에서 같은 크기가 누적된 값과 같은 색이 누적된 값을 빼준다.
3. 만일 i 번째의 색과 크기가 i-1번째 공의 색과 크기가 모두 같을 경우
    - i-1번째 경과로 저장해야 한다.
  
'''
n = int(input())
nums =[0] * n
arr = []
for i in range(n):
    clr, size = map(int, input().split())
    arr.append([size, clr, i])
    nums[i] = [clr, size]

arr.sort()

clrs = [0] * 200001
sizes = [0] * 2001

ans = [0] * n
summ = 0
for i in range(n):
    clrs[arr[i][1]] += arr[i][0]
    sizes[arr[i][0]] += arr[i][0]
    summ += arr[i][0]
    idx = arr[i][2]

    ans[idx] = summ + arr[i][0] - clrs[arr[i][1]] - sizes[arr[i][0]]
    # 색과 크기가 동시에 같을 때 엣지케이스
    if i != 0 and arr[i][0] == arr[i-1][0] and arr[i][1] == arr[i-1][1]:
        ans[idx] = ans[arr[i-1][2]]

for i in range(n):
    print(ans[i])