from itertools import combinations
n,m = map(int,input().split())
graph = []
chicken = []
house = []
for i in range(n):
    graph.append(list(map(int,input().split())))
    for j in range(n):
        if graph[i][j] == 2:
            chicken.append((i,j))
        if graph[i][j] == 1:
            house.append((i,j))

def cal_dist(c, house):
    result = 0

    for hx,hy in house:
        temp = int(1e9)
        for cx,cy in c:
            temp = min(temp, abs(hx-cx)+abs(hy-cy))
        result += temp
    return result



cc = combinations(chicken,m)
dist = int(1e9)

for c in cc:
    dist = min(dist, cal_dist(c,house))

print(dist)


