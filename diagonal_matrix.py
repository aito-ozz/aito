n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]
new_list = [[] for _ in range(n + m - 1)]
new = []
for i in range(n + m -1):
    for k in range(n):
        for j in range(m):
            if k + j == i:
                new_list[i].append(str(k) + str(j))

for i in range(n + m - 1):
    new += new_list[i]

for i in range(n * m):
    for j in range(n):
        for k in range(m):
            if str(j) + str(k) == new[i]:
                matrix[j][k] = i + 1
                break

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end='')
    print()