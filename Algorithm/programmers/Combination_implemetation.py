def make_team(participants, weight_participants, weight, answer):
    m = len(participants)

    if answer[0] > m: # 현재 답의 참여 인원이 주어진 participants보다 많은 경우 제외
        return answer

    for r in range(1, 1 << m):
    
        # 팀 나누기
        team_a = []
        for c in range(m):
            if r & (1 << c):
                team_a.append(weight[participants[c]])

        if len(team_a) in [0, m]: # 한 팀으로 모두 몰린 경우 제외
            continue

        weight_team_a = sum(team_a)
        # 팀별 몸무게 총합이 같고, 현재 한 팀의 몸무게가 답보다 클 경우 갱신
        if weight_team_a == (weight_participants - weight_team_a) and answer[1] < weight_team_a:
            answer = [m, weight_team_a]

    return answer

def solution(weight):

    n = len(weight)
    answer = [0, 0]

    for i in range((1 << n) - 1, 0, -1): # 참가 인원이 가장 많은 경우부터 보기

        participants = []
        weight_participants = 0

        # 참가 인원 인덱스 구하기
        for j in range(n):
            if i & (1 << j):
                participants.append(j)
                weight_participants += weight[j]

        # 참가 인원별 팀 구성 후 answer 갱신
        answer = make_team(participants, weight_participants, weight, answer)

    return answer