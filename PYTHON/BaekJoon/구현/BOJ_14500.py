import sys
import copy
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

maximum = 0


def rotate(curgraph):
    tmp = [[0] * len(curgraph) for _ in range(len(curgraph[0]))]
    for i in range(len(curgraph)):
        for j in range(len(curgraph[0])):
            tmp[j][i] = curgraph[len(curgraph) - i - 1][j]

    return tmp


def reflection(curgraph):
    tmp = copy.deepcopy(curgraph)
    for i in range(len(curgraph)):
        for j in range(len(curgraph[0])):
            tmp[i][j] = curgraph[i][len(curgraph[0]) - 1 - j]
    return tmp

# 4 4
# 0 0 0 0
# 0 0 0 0
# 0 1 2 3
# 0 0 0 4
graph2 = rotate(graph)
graph3 = rotate(graph2)
graph4 = rotate(graph3)

graph5 = reflection(graph)
# for i in range(len(graph5)):
#     print(graph5[i])
graph6 = rotate(graph5)
graph7 = rotate(graph6)
graph8 = rotate(graph7)
# for i in range(len(graph5)):
#     print(graph6[i])
graphList = [graph, graph2, graph3, graph4, graph5, graph6, graph7, graph8]

# # 1x4 직사각형
# for i in range(n - 3):
#     for j in range(m):
#         sum = graph[i][j] + graph[i + 1][j] + graph[i + 2][j] + graph[i + 3][j]
#         maximum = max(maximum, sum)
# # rotate
# for i in range(m - 3):
#     for j in range(n):
#         sum = graph2[i][j] + graph2[i + 1][j] + graph2[i + 2][j] + graph2[i + 3][j]
#         maximum = max(maximum, sum)

# 기다란 애
for k in range(8):
    ngraph = graphList[k]
    row = len(ngraph)
    col = len(ngraph[0])
    for i in range(row - 3):
        for j in range(col):
            sum = ngraph[i][j] + ngraph[i + 1][j] + ngraph[i + 2][j] + ngraph[i + 3][j]
            maximum = max(maximum, sum)

# # 2x2 정사각형
# for i in range(n - 1):
#     for j in range(m - 1):
#         sum = graph[i][j] + graph[i][j + 1] + graph[i + 1][j] + graph[i + 1][j + 1]
#         maximum = max(maximum, sum)
# # rotate
# for i in range(m - 1):
#     for j in range(n - 1):
#         sum = graph2[i][j] + graph2[i][j + 1] + graph2[i + 1][j] + graph2[i + 1][j + 1]
#         maximum = max(maximum, sum)
# 정사각형
for k in range(8):
    ngraph = graphList[k]
    row = len(ngraph)
    col = len(ngraph[0])
    for i in range(row - 1):
        for j in range(col - 1):
            sum = ngraph[i][j] + ngraph[i][j + 1] + ngraph[i + 1][j] + ngraph[i + 1][j + 1]
            maximum = max(maximum, sum)

# 니은자
for k in range(8):
    ngraph = graphList[k]
    row = len(ngraph)
    col = len(ngraph[0])
    for i in range(row - 2):
        for j in range(col - 1):
            sum = graphList[k][i][j] + graphList[k][i + 1][j] + graphList[k][i + 2][j] + graphList[k][i + 2][j + 1]
            maximum = max(maximum, sum)

# 꼬불이
for k in range(8):
    ngraph = graphList[k]
    row = len(ngraph)
    col = len(ngraph[0])
    for i in range(row - 2):
        for j in range(col - 1):
            sum = graphList[k][i][j] + graphList[k][i + 1][j] + graphList[k][i + 1][j + 1] + graphList[k][i + 2][j + 1]
            maximum = max(maximum, sum)

# 뻐큐
for k in range(8):
    ngraph = graphList[k]
    row = len(ngraph)
    col = len(ngraph[0])
    for i in range(row - 1):
        for j in range(col - 2):
            sum = graphList[k][i][j] + graphList[k][i][j + 1] + graphList[k][i][j + 2] + graphList[k][i + 1][j + 1]
            maximum = max(maximum, sum)

print(maximum)
