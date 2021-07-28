n,m = map(int,input().split())
parent = [0]*(n+1)

def find_parent(parent,x):
    if parent[x] != x:
        return find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(n+1):
    parent[i] = i

result = []
for _ in range(m):
    cal, a, b = map(int,input().split())
    if cal == 0:
        union_parent(parent,a,b)
    else:
        a = find_parent(parent,a)
        b = find_parent(parent,b)
        if a==b:
            result.append("YES")
        else:
            result.append("NO")

for i in result:
    print(i, end=' ')
