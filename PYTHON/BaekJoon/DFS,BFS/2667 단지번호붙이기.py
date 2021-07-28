# 7
# 0110100
# 0110101
# 1110101
# 0000111
# 0100000
# 0111110
# 0111000


n = int(input())
graph = [[] for _ in range(n)]
for i in range(n):
    temp = input()
    for j in temp:
        graph[i].append(int(j))

visited = [[-1]*n for _ in range(n)]
index=1
dx = [-1,1,0,0]
dy = [0,0,-1,1]
a = set()
def dfs(graph, visited, index, x,y):
    if graph[x][y] == 1:
        visited[x][y] = index
        a.add(index)
    else:
        visited[x][y] = 0
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n:
            if visited[nx][ny] == -1:
                if graph[nx][ny] == 1:
                    dfs(graph,visited,index,nx,ny)
                else:
                    visited[nx][ny] = 0


for i in range(n):
    for j in range(n):
        if visited[i][j] == -1:
            dfs(graph,visited,index,i,j)
            index += 1
a = list(a)
result = [0]*len(a)
for i in range(n):
    for j in range(n):
        for k in range(len(a)):
            if visited[i][j] == a[k]:
                result[k] += 1

print(len(a))
result.sort()
for aa in result:
    print(aa)