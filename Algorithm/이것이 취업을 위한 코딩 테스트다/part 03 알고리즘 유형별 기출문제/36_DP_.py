'''
편집거리
a 문자를 b로 바꾸기 위해서 삽입 교체 삭제 중 연산을 선택하여 최소 연산을 구하라

논리
- 각 위치에서 문자가 같다면 왼쪽 값 가져오기
- 각 위치에서 문자가 다르다면
    - 왼쪽(삽입), 왼쪽위(삭제), 위(교체) 중에 최소 값의 + 1 값을 저장
- 이해 못함.
'''

word1 = input()
word2 = input()

n, m = len(word1), len(word2)

dp = [[0] * (n + 1) for i in range(m + 1)]
for i in range(m + 1):
    dp[i][0] = i
for i in range(n + 1):
    dp[0][i] = i

for i in range(1, m + 1):
    for j in range(1, n + 1):
        if word1[j - 1] == word2[i - 1]:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])

print(dp[-1][-1])