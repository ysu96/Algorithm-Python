def hasZero(graph):
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == 0:
                return True
    return False

def solution(rows, columns):
    graph = [[0]*columns for _ in range(rows)]
    zeroCnt = rows*columns

    num = 1
    #1
    r, c = 0, 0
    graph[r][c] = num
    zeroCnt-=1
    # while hasZero(graph):
    while 1:
        if zeroCnt == 0:
            return graph
        #최근 수 짝수라면
        if num%2 == 0:
            if r+1 == rows: r = 0
            else: r = r+1
            num += 1

            # 사이클
            if graph[r][c] != 0:
                if graph[r][c]%2 == num%2:
                    return graph
            else:
                zeroCnt-=1

            graph[r][c] = num


        else:
            if c+1 == columns: c = 0
            else: c = c+1
            num += 1

            #사이클
            if graph[r][c] != 0:
                if graph[r][c]%2 == num%2:
                    return graph
            else:
                zeroCnt-=1

            graph[r][c] = num


solution(1000,1000)