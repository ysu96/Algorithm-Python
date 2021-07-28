import heapq
n,m = map(int,input().split())
graph = [[1e9]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

distance = [1e9]*(n+1)
distance[1] = 0
q = []
heapq.heappush(q,(distance[1],1))

while q:
    dist, now = heapq.heappop(q)
    if dist > distance[now]:
        continue

    for i in range(1,n+1):

        if graph[now][i] == 1e9:
            continue
        cost = dist+1
        if cost < distance[i]:
            distance[i] = cost
            heapq.heappush(q, (cost, i))

print(distance[1:])
max_val = 0
max_index = 0
count = 0
for i in range(1,n+1):
    if distance[i] == 1e9:
        continue

    if distance[i] > max_val:
        max_val = distance[i]
        max_index = i
        count = 1
    elif distance[i] == max_val:
        count += 1

print(max_index, max_val, count)

