n,m = map(int,input().split())

d = [ [0]*m for _ in range(n) ] # 2차원 리스트 초기화 방법

x,y,direction = map(int,input().split())
d[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int,input().split())))

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction #전역변수 direction 사용
    direction -= 1
    if(direction == -1):
        direction = 3

count = 1
turn_time = 0

while(1):
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue

    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if(array[nx][ny] == 0):
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)