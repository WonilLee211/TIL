import sys
sys.stdin = open('input.txt')

s = list(input())
string = []
acc = 0
for i in s:
    if i.isnumeric():
       acc += int(i)
    else:
        string.append(i)
string.sort()
ans = ''.join(string) + str(acc)
print(ans)