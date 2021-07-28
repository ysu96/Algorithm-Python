#플로이드워셜 쓰자
def solution(n, results):
    answer = 0
    graph = [[1e9]*(n+1) for _ in range(n+1)]
    for a,b in results:
        graph[a][b] = 1
        # graph[b][a] = 1
    for i in range(1,n+1):
        graph[i][i] = 0
    for k in range(1,n+1):
        for a in range(1,n+1):
            for b in range(1,n+1):
                graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])


    for i in range(1,n+1):
        r = True
        for j in range(1,n+1):
            if graph[i][j] == 1e9 and graph[j][i] == 1e9:
                r = False
                break
        if r == True:
            answer += 1
    return answer


n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solution(n,results))