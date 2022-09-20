'''
줄을 선 학생들이 차례로 뽑은 번호가 주어질 때
학생들이 최종적으로 줄을 선 순서를 출력하는 프로그램을 작성하시오.
'''

n = int(input())
arr = list(map(int, input().split()))
align = [1]

for i in range(1, n):
    align.insert(i -arr[i], i + 1)

print(*align)

'''
for i in range(1, n):
    # 인덱스 슬라이싱으로 뽑은 번호만큼 이동시켜서 입력하기
    align = align[:len(align) - arr[i]] + str(i + 1) + align[len(align) - arr[i]:]

for num in align:
    print(int(num), end=' ')

'''