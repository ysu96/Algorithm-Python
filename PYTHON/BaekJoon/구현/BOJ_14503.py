import sys
input = sys.stdin.readline
n,m = map(int, input().split())
r,c,d = map(int, input().split())
graph = []
cnt = 0
for _ in range(n):
    graph.append(list(map(int,input().split())))

queue = [(r,c,d)]
while 1:
    x,y, direction = queue.pop(0)
    if graph[x][y] == 0:
        cnt += 1
        graph[x][y] = 2 #clean complete

    #북쪽
    if direction == 0:
        #왼쪽, 아래쪽, 오른쪽, 위쪽 순서
        #왼쪽
        if graph[x][y-1] == 0:
            queue.append((x,y-1,3))
            continue

        #아래쪽
        if graph[x+1][y] == 0:
            queue.append((x+1,y,2))
            continue

        #오른쪽
        if graph[x][y+1] == 0:
            queue.append((x,y+1,1))
            continue

        #위쪽
        if graph[x-1][y] == 0:
            queue.append((x-1,y,0))
            continue

        if graph[x][y-1] != 0 and graph[x+1][y] != 0 and graph[x][y+1] != 0 and graph[x-1][y] != 0:
            if graph[x+1][y] == 1:
                print(cnt)
                break

            queue.append((x+1,y,direction)) # 한칸 후진
            continue

    #동쪽
    elif direction ==1:
        # 위, 왼쪽, 아래, 오른 순서

        # 위쪽
        if graph[x - 1][y] == 0:
            queue.append((x - 1, y, 0))
            continue

        # 왼쪽
        if graph[x][y - 1] == 0:
            queue.append((x, y - 1, 3))
            continue

        # 아래쪽
        if graph[x + 1][y] == 0:
            queue.append((x + 1, y, 2))
            continue

        # 오른쪽
        if graph[x][y + 1] == 0:
            queue.append((x, y + 1, 1))
            continue

        if graph[x][y - 1] != 0 and graph[x + 1][y] != 0 and graph[x][y + 1] != 0 and graph[x - 1][y] != 0:
            if graph[x][y-1] == 1:
                print(cnt)
                break

            queue.append((x, y-1, direction))  # 한칸 후진
            continue
    #남쪽
    elif direction == 2:
        # 오른쪽, 위쪽, 왼쪽, 아래쪽
        # 오른쪽
        if graph[x][y + 1] == 0:
            queue.append((x, y + 1, 1))
            continue
        # 위쪽
        if graph[x - 1][y] == 0:
            queue.append((x - 1, y, 0))
            continue
        # 왼쪽
        if graph[x][y - 1] == 0:
            queue.append((x, y - 1, 3))
            continue
        # 아래쪽
        if graph[x + 1][y] == 0:
            queue.append((x + 1, y, 2))
            continue

        if graph[x][y - 1] != 0 and graph[x + 1][y] != 0 and graph[x][y + 1] != 0 and graph[x - 1][y] != 0:
            if graph[x-1][y] == 1:
                print(cnt)
                break

            queue.append((x - 1, y, direction))  # 한칸 후진
            continue
    #서쪽
    else:
        #아래, 오른, 위, 왼
        # 아래쪽
        if graph[x + 1][y] == 0:
            queue.append((x + 1, y, 2))
            continue
        # 오른쪽
        if graph[x][y + 1] == 0:
            queue.append((x, y + 1, 1))
            continue
        # 위쪽
        if graph[x - 1][y] == 0:
            queue.append((x - 1, y, 0))
            continue
        # 왼쪽
        if graph[x][y - 1] == 0:
            queue.append((x, y - 1, 3))
            continue

        if graph[x][y - 1] != 0 and graph[x + 1][y] != 0 and graph[x][y + 1] != 0 and graph[x - 1][y] != 0:
            if graph[x][y+1] == 1:
                print(cnt)
                break

            queue.append((x, y+1, direction))  # 한칸 후진
            continue




