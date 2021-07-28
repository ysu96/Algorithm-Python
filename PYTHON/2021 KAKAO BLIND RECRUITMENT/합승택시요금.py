from collections import deque
def dijkstra(graph, start):
    distance = [1e9]*(len(graph)+1)
    distance[start] = 0
    q = deque([(start,0)])
    while q:
        now, dist = q.popleft()
        for next,cost in graph[now]:
            if distance[next] > dist+cost:
                distance[next] = dist+cost
                q.append((next,distance[next]))
    return distance
def solution(n, s, a, b, fares):
    answer = 0
    graph = [[] for _ in range(n+1)]
    for c,d,f in fares:
        graph[c].append((d,f))
        graph[d].append((c,f))

    dp = [[]] + [dijkstra(graph,i) for i in range(1, n + 1)]
    # print(dp)
    answer = 987654321
    for i in range(1, n + 1):
        answer = min(dp[i][a] + dp[i][b] + dp[i][s], answer)
    # print(answer)
    return answer

n=6
s=4
a=6
b=2
fares=[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
solution(n,s,a,b,fares)