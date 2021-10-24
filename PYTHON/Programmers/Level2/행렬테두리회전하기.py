def solution(rows, columns, queries):
    answer = []
    graph = [[] for _ in range(rows)]
    cnt = 1

    for i in range(rows):
        for j in range(columns):
            graph[i].append(cnt)
            cnt+=1

    for x1,y1,x2,y2 in queries:
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1
        mins = []

        # 윗변
        for y in range(y2, y1, -1):
            graph[x1][y-1], graph[x1][y] = graph[x1][y], graph[x1][y-1]
            mins.append(graph[x1][y-1])
            mins.append(graph[x1][y])
        #왼쪽 변
        for x in range(x1,x2):
            graph[x][y1], graph[x+1][y1] = graph[x+1][y1], graph[x][y1]
            mins.append(graph[x][y1])
            mins.append(graph[x+1][y1])

        #아래 변
        for y in range(y1, y2):
            graph[x2][y], graph[x2][y+1] = graph[x2][y+1], graph[x2][y]
            mins.append(graph[x2][y])
            mins.append(graph[x2][y+1])

        #오른쪽 변
        for x in range(x2, x1+1, -1):
            graph[x][y2], graph[x-1][y2] = graph[x-1][y2], graph[x][y2]
            mins.append(graph[x][y2])
            mins.append(graph[x-1][y2])

        # for i in range(len(graph)):
        #     print(graph[i])
        #
        # print("--------------")
        mins = set(mins)
        minNum = min(mins)
        answer.append(minNum)

    return answer

print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))