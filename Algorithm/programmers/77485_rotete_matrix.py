rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]

def rotate_matrix(query):
    fr_r, fr_c, to_r, to_c = query
    r, c = fr_r, fr_c

    rotate_num = []
    for i in range(4):
        while fr_r <= r + dr[i] <= to_r and fr_c <= c + dc[i] <= to_c:
            rotate_num.append(matrix[r][c])
            r, c = r + dr[i], c + dc[i]

    answer.append(min(rotate_num))
    m = len(rotate_num)

    j = 0
    r, c = fr_r, fr_c
    for i in range(4):
        while fr_r <= r + dr[i] <= to_r and fr_c <= c + dc[i] <= to_c:
            r, c = r + dr[i], c + dc[i]
            matrix[r][c] = rotate_num[j]
            j += 1
    print(matrix)
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

answer = []

matrix = [[]]
for i in range(rows):
    row = [0] * (columns + 1)
    for j in range(1, columns + 1):
        row[j] = i * columns + j
    matrix.append(row)

for query in queries:
    rotate_matrix(query)

print(answer)