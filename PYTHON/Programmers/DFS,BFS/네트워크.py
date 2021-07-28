def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, computers):
    answer = 1
    parent = [0]*n
    for i in range(n):
        parent[i] = i

    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                union_parent(parent,i,j)
    #
    # parent.sort()
    for i in range(n):
        parent[i] = find_parent(parent,i)

    answer = len(set(parent))

    return answer



n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n,computers))
# result = 2
# 3	[[1, 1, 0], [1, 1, 1], [0, 1, 1]]	1