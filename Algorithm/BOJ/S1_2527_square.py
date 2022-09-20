import sys
sys.stdin = open('input.txt')

for i in range(4):
    frm_c1, frm_r1, to_c1, to_r1, frm_c2, frm_r2, to_c2, to_r2 = map(int, input().split())

    sq1_r = set([ i for i in range(frm_r1, to_r1+1)])
    sq1_c = set([ i for i in range(frm_c1, to_c1+1)])
    sq2_r = set([ i for i in range(frm_r2, to_r2+1)])
    sq2_c = set([ i for i in range(frm_c2, to_c2+1)])

    result = None

    if len(sq1_c.intersection(sq2_c)) > 1 and len(sq1_r.intersection(sq2_r)) > 1:
        result = 'a'
    elif len(sq1_c.intersection(sq2_c)) > 1 and len(sq1_r.intersection(sq2_r)) == 1:
        result = 'b'
    elif len(sq1_c.intersection(sq2_c)) == 1 and len(sq1_r.intersection(sq2_r)) > 1:
        result = 'b'
    elif len(sq1_c.intersection(sq2_c)) == 1 and len(sq1_r.intersection(sq2_r)) == 1:
        result = 'c'
    else:
        result = 'd'

    print(result)