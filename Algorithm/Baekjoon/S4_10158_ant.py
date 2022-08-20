import sys
sys.stdin = open('input.txt')
'''
t 시간 후에 개미의 위치 좌표 (x,y) 출력하는 프로그램
제한 시간 매우 짧음

'''
# r와 c을 분리해서 생각
# 규칙성을 찾고 생략할 수 있는 부분 제거하기
def find_position(time_i, init_i, border):
    flag = 1
    idx = init_i
		# 시간마다 증가 감소 증가 규칙성에 따라 조건 걸기
    while flag != 5:
        if flag == 1 and time_i >= border - init_i:
            time_i -= border - init_i
            idx = border
            flag += 1

        elif flag == 2 and time_i >= border - init_i:
            time_i -= border - init_i
            idx = init_i
            flag += 1

        elif flag == 3 and time_i >= init_i:
            time_i -= init_i
            idx = 0
            flag += 1

        else:
            if flag == 1:
                idx += time_i
                break
            if flag == 2:
                idx -= time_i
                break
            if flag == 3:
                idx -= time_i
                break
            if flag == 4:
                idx += time_i
                break
    return idx

r, c = map(int, input().split())
init_r, init_c = map(int, input().split())
time = int(input())

time_r = time_c = time
# 행과 열의 범위의 두배값 시간마다 제자리로 돌아옴
time_r %= r * 2 #
time_c %= c * 2

now_r, now_c = init_r, init_c

if time_r != 0:
    now_r = find_position(time_r, init_r, r)
if time_c != 0:
    now_c = find_position(time_c, init_c, c)

print(now_r, now_c)