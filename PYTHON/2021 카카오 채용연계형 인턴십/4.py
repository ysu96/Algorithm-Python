from collections import deque
import heapq
def solution(n, start, end, roads, traps):
    graph = [[1e9]*(n+1) for _ in range(n+1)]
    distance = [1e9]*(n+1)
    distance[start] = 0
    cycle = [0] *(n+1)
    trap = [False] * (n + 1)
    for t in traps:
        trap[t] = True

    for i in range(1,n+1):
        graph[i][i] = 0

    for road in roads:
        a,b,cost = road
        graph[a][b] = min(cost, graph[a][b])

    no = []
    aa = []
    q = deque([(0,start)])
    while q:
        cost, now = q.popleft()

        if trap[now] == True:
            for i in range(1,n+1):
                graph[now][i],graph[i][now] = graph[i][now], graph[now][i]

        for i in range(1, n + 1):
            if cost + graph[now][i] < 1e9 and i != now:

                if i == end:
                    aa.append(cost + graph[now][i])
                    no.append(now)
                else:
                    if trap[i] == True and trap[now] == True:
                        cycle[i] += 1
                        if cycle[i] > 1:
                            continue
                    q.append((cost + graph[now][i], i))

    return max(aa)


n=4
start=1
end=4
roads= [[1, 2, 1], [3, 2, 1], [2, 4, 1]]
traps=[2, 3]

print(solution(n,start,end,roads,traps))
# result = 4