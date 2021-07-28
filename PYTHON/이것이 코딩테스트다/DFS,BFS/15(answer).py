from collections import deque

n,m,k,x = map(int,input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)

dist = [1e9]*(n+1)
dist[x] = 0
q = deque([x])

while q:
    now = q.popleft()
    for next in graph[now]:
        if dist[next] == 1e9:
            dist[next] = dist[now] + 1
            q.append(next)

check = False
for i in range(n+1):
    if dist[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)