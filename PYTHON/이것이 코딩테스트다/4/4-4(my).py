############# 망    함 ##############

n, m = map(int, input().split())
x,y,d = map(int, input().split())
maps = []
for i in range(n):
    maps.append(list(map(int, input().split())))


def turn():
    global d
    if (d > 0):
        d = d - 1
    else:
        d = 3


def num_count():
    global x,y,d,maps
    steps = [(-1,0), (0,1), (1,0), (0,-1)]
    count = 0

    while(1):
        turn()
        # second
        dx = x + steps[d][0]
        dy = y + steps[d][1]

        if(maps[dx][dy] == 0): # 가보지 않은 칸 존재
            x = dx
            y = dy
            count += 1
            break

            if(i == 3): # 4방향 다 돈 경우
                dx = x - steps[d][0]
                dy = y - steps[d][1]
                if(maps[dx][dy] == 1):
                    return count
                else:
                    x = dx
                    y = dy

print(num_count(x,y,d))