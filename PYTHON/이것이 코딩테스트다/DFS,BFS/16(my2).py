from itertools import combinations
from collections import deque
n,m = map(int,input().split())
graph = []
virus = []
wall = []
empty = []
for a in range(n):
    graph.append(list(map(int,input().split())))
    for b in range(m):
        if graph[a][b] == 1:
            wall.append((a,b))
        elif graph[a][b] == 2:
            virus.append((a,b))
        else:
            empty.append((a,b))

new_wall = combinations(empty,3)
q = deque(virus)



dx = [-1,0,1,0]
dy = [0,1,0,-1]

def virus(graph):
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx<n and ny >= 0 and ny<m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 2
                    q.append((nx,ny))
                else:
                    continue

answer = 0

for nw in new_wall:
    for x,y in nw:
        graph[x][y] = 1
    count = 0
    virus(graph)
    print(graph)
    for a in range(n):
        for b in range(m):
            if graph[a][b] == 0:
                count += 1
    answer = max(answer,count)

    for x,y in nw:
        graph[x][y] = 0

print(answer)

