import heapq

n,m = map(int,input().split())
graph = [[1e9]*(n+1) for _ in range(n+1)]
distance = [1e9]*(n+1)
for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for i in range(1,n+1):
    graph[i][i] = 0

#1번 출발, 1번까지 거리 = 0
q = [(0,1)]

while q:
    dist, now = heapq.heappop(q)
    if dist > distance[now]:
        continue

    for i in range(1,len(graph[now])):
        cost = graph[now][i] + dist
        if cost < distance[i]:
            distance[i] = cost
            heapq.heappush(q,(cost,i))

max_node = 0
max_distance = 0
result = []

for i in range(1,n+1):
    if distance[i] > max_distance:
        max_node = i
        max_distance = distance[i]
        result = [max_node]
    elif distance[i] == max_distance:
        result.append(i)

print(max_node, max_distance, len(result))

