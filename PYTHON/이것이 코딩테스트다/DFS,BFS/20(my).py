from itertools import combinations

n = int(input())
graph = []
teachers =[]
students =[]
for i in range(n):
    graph.append(list(input().split()))
    for j in range(n):
        if graph[i][j] == 'S':
            students.append((i,j))
        elif graph[i][j] == 'T':
            teachers.append((i,j))




def check(tx,ty):
    for i in range(tx,-1,-1):

        if graph[i][ty] == 'O':
            break
        elif graph[i][ty] == 'S':
            return False
        else:
            continue

    for i in range(tx,n):
        
        if graph[i][ty] == 'O':
            break
        elif graph[i][ty] == 'S':
            return False
        else:
            continue

    for i in range(ty,-1,-1):

        if graph[tx][i] == 'O':
            break
        elif graph[tx][i] == 'S':
            return False
        else:
            continue

    for i in range(ty,n):
        if graph[tx][i] == 'O':
            break
        elif graph[tx][i] == 'S':
            return False
        else:
            continue

    return True

def solution(count):
    if count == 3:
        for tx,ty in teachers:

            if not check(tx,ty):
                return False
        return True


    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'X':
                graph[i][j] = 'O'
                count += 1
                if solution(count):
                    return True

                graph[i][j] = 'X'
                count -= 1

    return False

if solution(0):
    print("YES")
else:
    print("NO")

