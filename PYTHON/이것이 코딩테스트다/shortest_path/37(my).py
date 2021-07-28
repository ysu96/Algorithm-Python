n = int(input())
m = int(input())
graph = [[1e9]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            graph[i][j] = 0

for i in range(m):
    a,b,cost = map(int,input().split())
    if cost < graph[a][b]:
        graph[a][b] = cost

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == 1e9:
            graph[i][j] = 0
        print(graph[i][j], end=' ')
    print()
