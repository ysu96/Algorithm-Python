from collections import deque

n= int(input())
k= int(input())
board = [[0]*n for _ in range(n)]

for i in range(k):
    r,c = map(int,input().split())
    board[r-1][c-1] = 1 #apple

l = int(input())
rotate = []
for i in range(l):
    x,c = input().split()
    rotate.append([int(x), c])

for i in range(l-1,0,-1):
    rotate[i][0] -= rotate[i-1][0]

def solution(board, rotate):
    snake = deque()
    snake.append((0,0))
    time = 0
    dir = ['L','U','R','D']
    # direction = {'L':(0,-1), 'U':(-1,0),'R':(0,1),'D':(1,0)}
    direction = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    cur_dir = 2
    x, y = 0, 0

    for i in rotate:
        for j in range(i[0]):
            time += 1
            x += direction[cur_dir][0]
            y += direction[cur_dir][1]

            if x<0 or x>=n or y<0 or y>=n:
                return time
            elif (x, y) in snake:
                return time
            else:
                snake.append((x, y))
                if board[x][y] != 1:
                    snake.popleft()
                else:
                    board[x][y] = 0

        if i[1] == 'L':
            cur_dir = (cur_dir + 3) % 4
        else:
            cur_dir = (cur_dir + 1) % 4

    while 1:
        time += 1
        x += direction[cur_dir][0]
        y += direction[cur_dir][1]

        if x < 0 or x >= n or y < 0 or y >= n:
            return time
        elif (x, y) in snake:
            return time
        else:
            snake.append((x, y))
            if board[x][y] != 1:
                snake.popleft()
            else:
                board[x][y] = 0

    return time

print(solution(board,rotate))




