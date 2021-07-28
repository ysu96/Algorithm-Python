def solution(a, edges):
    answer = 0
    length = len(a)
    graph = [[] for _ in range(length)]
    new_graph = [[] for _ in range(length)]

    for i,j in edges:
        graph[i].append(j)
        graph[j].append(i)
        new_graph[i].append(j)
        new_graph[j].append(i)

    while 1:
        for i in range(length):
            if len(graph[i]) == 1:
                tmp = a[i]
                answer += abs(tmp)
                a[i] = 0
                a[graph[i][0]] += tmp

                new_graph[graph[i][0]].remove(i)
                new_graph[i].pop()

        graph = new_graph
        count = 0
        for i in range(length):
            if len(graph[i]) != 0:
                count += 1
        if count == 0:
            break

    if a.count(0) == length:
        return answer
    else:
        return -1

a =[-5,0,2,1,2]
edges = [[0,1],[3,4],[2,3],[0,3]]
print(solution(a,edges))





