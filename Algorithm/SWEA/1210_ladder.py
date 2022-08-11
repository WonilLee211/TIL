'''
100 x 100 크기의 2차원 배열로 주어진 사다리에 대해서,
지정된 도착점에 대응되는 출발점 X를 반환하는 코드를 작성하라
'''

def entrance_search(ladder):

    for i in range(1, 101):
        if ladder[-1][i] == 2:
            exit_x = i-1 # 도착지점 x

    y = 99
    while y: # 출발지 도착할 때 까지
        if ladder[y][exit_x + 1]: # 오른쪽에 길이 있다면
            while ladder[y][exit_x + 1]: # 오른쪽 길이 1일 때 까지
                exit_x += 1 # 방향 이동
            y -= 1
            continue # 아래 구문 실행 방지

        if ladder[y][exit_x - 1]:
            while ladder[y][exit_x - 1]:
                exit_x -= 1
            y -= 1
            continue
        y -= 1

    return exit_x -1 # 임의로 행렬을 증가시킨 인덱스만큼 줄이기

if __name__=="__main__":


    for test_case in range(1, 11):
        # 행렬 양끝에 0을 추가해서 102 * 102 행렬로 만들기
        t = int(input())

        ladder_ = []
        for _ in range(100):
            sublist = [0] + list(map(int, input().split())) + [0]
            ladder_.append(sublist)

        print(f"#{test_case} {entrance_search(ladder_)}")