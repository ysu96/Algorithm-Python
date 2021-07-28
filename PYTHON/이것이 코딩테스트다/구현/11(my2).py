from collections import deque
n = int(input())
k = int(input())
dx = [0,-1,0,1]
dy = [1,0,-1,0]
graph = [[0]*(n) for _ in range(n)]
for _ in range(k):
    a,b = map(int,input().split())
    graph[a-1][b-1] = 1

l = int(input())
moves = []
for _ in range(l):
    x,c = input().split()
    moves.append((int(x),c))

snake = [(0,0)]
head = (0,0)
result = 0
direction = 0
end = False
for t,c in moves:
    t -= result
    for i in range(t):
        x,y = head
        nx = x + dx[direction]
        ny = y + dy[direction]
        result += 1
        if nx<0 or nx>=n or ny<0 or ny>=n or (nx,ny) in snake:
            end = True
            break

        if graph[nx][ny] != 1:
            snake.pop(0)

        snake.append((nx,ny))
        head = (nx,ny)

    if end:
        break

    if c=='L':
        direction = (direction+1)%4
    else:
        direction = (direction-1)%4

print(result)

