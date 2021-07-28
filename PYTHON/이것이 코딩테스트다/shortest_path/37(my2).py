n = int(input())
m = int(input())
graph = [[1e9]*(n+1) for _ in range(n+1)]

for i in range(m):
    a,b,c = map(int,input().split())
    graph[a][b] = min(graph[a][b], c)

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][k]+graph[k][j], graph[i][j])

for i in range(1,n+1):
    graph[i][i] = 0

for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == 1e9:
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()
