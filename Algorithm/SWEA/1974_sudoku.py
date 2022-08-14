
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    # 스도쿠 받기 9X9
    sudoku = [list(map(int, input().split())) for i in range(9)]

    # 3X3으로 스도쿠 나눠서 list(set)으로 만들기
    # 기준 점에서 3x3 요소들 가져와서 set으로 저장하는 함수
    def threeSudoku(matrix, r, c):

        arrset = set()

        for i in range(3):
            for j in range(3):
                arrset.add(matrix[r + i][c + j])
        return arrset


    # 0,0 0,3 0,6/ 3,0 3,3 3,6/ 6,0 6,3 6,6 포인트별로
    # 검증해야 하는 행 3개와 열3개를 받아오는 함수
    def compareRC(matrix, r, c):
        cprlist = []

        # 행부분 저장
        for i in range(3):
            temp = set()
            for j in range(9):
                temp.add(matrix[r + i][j])
            cprlist.append(temp)

        # 열부분 저장
        for i in range(3):
            temp1 = set()
            for j in range(9):
                temp1.add(matrix[j][c + i])
            cprlist.append(temp1)

        ## 입력된 포인트에서 비교해야하는 행과 열을 set형태로 리스트에 저장
        return cprlist

    # 스도쿠의 0,0 0,3 0,6/ 3,0 3,3 3,6/ 6,0 6,3 6,6 포인트별로 3x3 스도쿠와 비교 행렬 비교하기
    CtrRow = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    ans = True

    for r in range(3):
        for c in range(3):
            minsudoku = threeSudoku(sudoku, r * 3, c * 3)
            cpr_RC =  compareRC(sudoku, r * 3, c * 3)
            for cpr in cpr_RC:
                # 비교행렬과 다른지, 1~9까지 담겨있는지 확인
                if cpr != minsudoku or minsudoku != CtrRow or cpr != CtrRow:
                    ans = False
                    break

    if ans:
        print(f"#{test_case}", 1)
    else:
        print(f"#{test_case}", 0)