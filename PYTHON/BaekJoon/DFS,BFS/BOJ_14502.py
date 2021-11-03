import sys
from itertools import combinations
import copy

def virus():
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    queue = []
    temp = copy.deepcopy(graph)
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 2:
                queue.append((i, j))
                temp[i][j] = 999

                while queue:
                    x, y = queue.pop(0)
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < n and 0 <= ny < m:
                            if temp[nx][ny] == 0:
                                temp[nx][ny] = 999
                                queue.append((nx, ny))

    cnt = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                cnt += 1
    return cnt

input = sys.stdin.readline
n,m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

candi = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            candi.append((i,j))

candidates = combinations(candi,3)
first = 0
second = 0
third = 0
ans = 0

for c1,c2,c3 in candidates:
    graph[c1[0]][c1[1]] = 1
    graph[c2[0]][c2[1]] = 1
    graph[c3[0]][c3[1]] = 1

    ans = max(ans, virus())

    graph[c1[0]][c1[1]] = 0
    graph[c2[0]][c2[1]] = 0
    graph[c3[0]][c3[1]] = 0

print(ans)
