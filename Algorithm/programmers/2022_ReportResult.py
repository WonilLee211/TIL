def solution(id_list, report, k):
    n = len(id_list)
    answer = [0] * n  # 유저별로 처리 결과 메일을 받은 횟수

    id_dict = {name: i for i, name in enumerate(id_list)}  # id_list의 이름 순서대로 id 값 할당
    reporters = [[] for i in range(n)]  # 자신을 신고한 username 저장

    for row in report:  # 신고내역
        frm, to = row.split()
        for user in id_list:
            if frm == user and user not in reporters[id_dict[to]]:  # 신고자가 이미 자신을 신고하지 않았을 때 저장
                reporters[id_dict[to]].append(user)
                break

    for row in reporters:  # 자신을 신고한 수가 k 이상 일 때
        if len(row) >= k:
            for name in row:
                answer[id_dict[name]] += 1  # 자신을 신고한 유저 id에 위치한 answer에 counting

    return answer