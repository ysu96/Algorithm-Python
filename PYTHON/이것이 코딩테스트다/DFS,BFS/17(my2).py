from collections import deque

n,k = map(int,input().split())
data = []
graph = []

for i in range(n):
    graph.append(list(map(int,input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            # (virus 종류, 시간, 위치x, 위치y)
            data.append((graph[i][j],0,i,j))

s,tx,ty = map(int,input().split())
data.sort()
q = deque(data)

dx = [-1,0,1,0]
dy = [0,1,0,-1]

while q:
    virus, time, x, y = q.popleft()
    if time == s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx>=0 and nx<n and ny>=0 and ny<n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus,time+1,nx,ny))

print(graph[tx-1][ty-1])