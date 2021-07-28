n,m = map(int,input().split())
graph = [[1e9]*(n+1) for _ in range(n+1)]

for i in range(m):
    a, b = map(int,input().split())
    graph[a][b] = 1

for i in range(1,n+1):
    graph[i][i] = 0

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

# print(graph)
for k in range(1,n+1):
    for i in range(1,n+1):
        print(graph[k][i], end= '   ')
    print()

find = True
count = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == 1e9 and graph[j][i] == 1e9:
            find = False

    if find == True:
        count += 1
    else:
        find = True


print(count)