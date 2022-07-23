T = int(input())
for testcase in range(1, T+1):

    str_num, K = input().split()

    # 입력받은 str_num의 최대값인 경우 찾기
    li = list(int(s) for s in str_num)
    li = sorted(li, reverse = True)
    maxvalue = ''
    for n in li:
        maxvalue += str(n)
    # 입력받은 숫자열 amxvalue

    length = len(str_num)
    
    numlist = []
    numlist.append(str_num)

    cnt = 0      
    while cnt != int(K): # 반복가능한 횟수만큼
        cnt += 1
        caselist = [] # 반복 1회당 가능한 경우의 숫자열 저장장소
        for number in numlist: # ['12123', 31212'..] 형태 
            
            # 숫자 두 개를 골라서 교환하는 모든 경우의 수 구하기
            for i in range(length):
                for j in range(i + 1,length):
                    temp = list(number)
                    temp[i], temp[j] = temp[j], temp[i]
                    
                    case =''
                    for k in range(length):
                        case += temp[k]
                    
                    caselist.append(case)
        # 다음 반복에서 교환할 숫자열 리스트 최신화
        numlist = caselist

        # 반복 과정에서 maxvalue 찾았다면 stop
        if str(maxvalue) in numlist:
            break
    
    # 숫자열을 정수 타입으로 변경
    numlist = [int(num) for num in numlist]

    print(f"#{testcase} {max(numlist)}")
