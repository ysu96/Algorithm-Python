from itertools import combinations

n,m = map(int,input().split())
city = []
for _ in range(n):
    city.append(list(map(int,input().split())))

chicken = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 2:
            chicken.append((i,j))

lists = list(combinations(chicken,m))
result = 99999

#조합별로
for c in lists:
    new_result = 0
    for i in range(n):
        for j in range(n):
            final_dist = 99999
            if city[i][j] == 1:
                #closest
                for k in range(m):
                    dist = abs(i-c[k][0]) + abs(j-c[k][1])
                    final_dist = min(final_dist, dist)
                new_result += final_dist

    result = min(result, new_result)

print(result)