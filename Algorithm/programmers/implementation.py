'''


'''
from collections import deque
companies = ["A fabdec 2", "B cebdfa 2", "C ecfadb 2"]
applicants = ["a BAC 1", "b BAC 3", "c BCA 2", "d ABC 3", "e BCA 3", "f ABC 2"]
n, m = len(companies), len(applicants)
comp = []
appli = deque()
selected_dict = {}
rejected = []

for i in range(n):
    name, rank, num = companies[i].split(" ")
    comp.append([name, list(rank), int(num)])
    selected_dict[name] = []

for i in range(m):
    name, rank, num = applicants[i].split(" ")
    appli.append([name, list(rank[-1::-1]), int(num)])
    rejected.append(name)



while True:
    k = len(appli)
    for i in range(k):
        name, rank, num = appli.popleft()


        if num > 0:
            if name in rejected:
                selected_dict[rank.pop()].append(name)
                appli.append([name, rank, num - 1])
            else:
                appli.append([name, rank, num])

    rejected = []
    for j in range(n):
        select_appli = []
        cnt = 0
        name, rank, num = comp[j]

        for a in rank:
            if a in selected_dict[name]:
                select_appli.append(a)
                cnt += 1
            if cnt == num:
                break

        for a in selected_dict[name]:
            if a not in select_appli:
                rejected.append(a)

        selected_dict[name] = select_appli

    if len(rejected) == 0:
        break


answer = []

for i in sorted(selected_dict.keys()):
    temp = i + "_"
    for v in sorted(selected_dict[i]):
        temp += v
    answer.append(temp)
print(answer)