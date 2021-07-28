def solution(n, z, roads, queries):
    answer = []
    graph = [[1e9]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                graph[i][j] = z
    for a,b,w in roads:
        graph[a][b] = w

    dp = [-1]*(max(queries)+1)

    dp[0] = 0
    for i in range(1,z):
        for a,b,w in roads:
            if w == i:
                if a == 0:
                    dp[i] = 1
                    break
                else:
                    dp[i] = 2
                    break
            if w < i:
                



    for c in queries:
        if c == 0:

        if c == z:

        if c < z:

        if c > z:

    return answer

n= 5
z=5
roads = [[1,2,3],[0,3,2]]
queries = [0,1,2,3,4,5,6]
result = [0,-1,1,2,3,1,4]