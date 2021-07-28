def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a>b:
        parent[a] = b
    else:
        parent[b] = a

n = int(input())
m = int(input())
parent = [i for i in range(n+1)]
edges = []

for _ in range(m):
    a,b = map(int,input().split())
    edges.append((a,b))

for _ in range(2):
    for a,b in edges:
        union_parent(parent,a,b)


answer = 0

for i in range(2,n+1):
    if parent[i] == 1:
        answer+=1
print(answer)

