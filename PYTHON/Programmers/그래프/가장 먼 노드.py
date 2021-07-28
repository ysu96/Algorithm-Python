from collections import deque
def solution(n, edge):

    distance = [1e9] * (n+1)
    distance[1] = 0
    distance[0] = 0
    start = 1
    q = deque([start])

    graph = [[] for _ in range(n+1)]
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    while q:
        now = q.popleft()
        for g in graph[now]:
            if distance[g]>distance[now]+1:
                distance[g] = distance[now]+1
                q.append(g)

    # print(distance)
    max_dist = max(distance)
    answer = distance.count(max_dist)

    return answer


# def solution(n, edge):
#
#     distance = [1e9] * (n+1)
#     distance[1] = 0
#     distance[0] = 0
#     start = 1
#     graph = [[] for _ in range(n+1)]
#     for e in edge:
#         graph[e[0]].append(e[1])
#         graph[e[1]].append(e[0])
#
#     def dijkstra(graph, start, distance):
#         now = start
#         for g in graph[now]:
#             if distance[g] > distance[now] + 1:
#                 distance[g] = distance[now]+1
#                 dijkstra(graph, g, distance)
#
#     dijkstra(graph,start, distance)
#     # print(distance)
#     max_dist = max(distance)
#     answer = distance.count(max_dist)
#
#     return answer



n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n,edge))
