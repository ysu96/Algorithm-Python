import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[0] * m for _ in range(n)]
for i in range(n):
    string = input()
    for j in range(m):
        graph[i][j] = int(string[j])

queue = [(0, 0, 0)] #x,y,cnt
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
visited = [(0, 0)]

while queue:
    x, y, cnt = queue.pop(0)
    if (x, y) == (n - 1, m - 1):
        cnt += 1
        print(cnt)
        break
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 1:
                if (nx, ny) not in visited:
                    queue.append((nx, ny, cnt))
                    visited.append((nx, ny))
