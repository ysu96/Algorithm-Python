from itertools import combinations

def check(graph, teachers):
    for tx, ty in teachers:
        for i in range(tx, -1, -1):
            if graph[i][ty] == 'O':
                break
            elif graph[i][ty] == 'S':
                return False
            else:
                continue

        for i in range(tx, n):
            if graph[i][ty] == 'O':
                break
            elif graph[i][ty] == 'S':
                return False
            else:
                continue

        for i in range(ty, -1, -1):
            if graph[tx][i] == 'O':
                break
            elif graph[tx][i] == 'S':
                return False
            else:
                continue

        for i in range(ty, n):
            if graph[tx][i] == 'O':
                break
            elif graph[tx][i] == 'S':
                return False
            else:
                continue

    return True

n = int(input())
graph = []
teachers = []
empty = []


for i in range(n):
    graph.append(list(input().split()))
    for j in range(n):
        if graph[i][j] == "T":
            teachers.append((i,j))
        elif graph[i][j] == "X":
            empty.append((i,j))

candidates = list(combinations(empty,3))
is_possible = False
for candidate in candidates:
    for cx,cy in candidate:
        graph[cx][cy] = "O"
    if check(graph,teachers) == True:
        is_possible = True
    for cx,cy in candidate:
        graph[cx][cy] = "X"

if is_possible:
    print("YES")
else:
    print("NO")









