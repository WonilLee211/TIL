'''
k개 골라서 상자에 담아 판매
수확한 귤 크기가 다름
크기별 차이 최소화
크기가 서로 다른 종류의 수 최소값 반환

1 ≤ k ≤ tangerine의 길이 ≤ 100,000
1 ≤ tangerine의 원소 ≤ 10,000,000

알고리즘
한번 탐색해서 원소별 중복값을 카운트
(-카운트, 원소) 형태로 heapq에 담아서 중복이 가장 큰 값부터 추출
누적카운트값이 k보다 커질때까지 반환 횟수 출력

'''

k = 6
tangerine = [1, 3, 2, 5, 4, 5, 2, 3]
key = set(tangerine)
cnt_ele_dict = {}

for i in key:
    cnt_ele_dict[i] = 0

for ele in tangerine:
    cnt_ele_dict[ele] += 1

new_list = sorted(list(cnt_ele_dict.items()), key = lambda x:x[1], reverse = True)
acc = 0
result = 0

for i, cnt in new_list:
    result += 1
    acc += cnt

    if k <= acc:
        break

print(result)