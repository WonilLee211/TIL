import sys
<<<<<<< HEAD
sys.stdin =open('input.txt')

# a-f : 1-6
# c-e : 3-5
# b-d : 2-4

n = int(input())
linklist = []

for i in range(n):
    a, b, c, d, e, f = map(int, input().split())
=======
sys.stdin = open('input.txt')

n = int(input())

linklist = []

for i in range(N):
    a, b, c, d, e, f = map(int, input().split())
    linklist = [[a, 6], [b, 4], [c, 5], [d, 2], [e, 3], [f, 1]]



    # a-f 1-6
    # b-d 2-4
    # c-e 3-5

>>>>>>> 2bc358a9614404e2012a80e5b5dc647288d27534
