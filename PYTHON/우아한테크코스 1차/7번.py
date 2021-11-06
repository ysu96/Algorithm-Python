
def rotateClock(curgraph):
    tmp = [[0] * len(curgraph) for _ in range(len(curgraph[0]))]
    for i in range(len(curgraph)):
        for j in range(len(curgraph[0])):
            tmp[j][i] = curgraph[len(curgraph) - i - 1][j]

    return tmp

def rotateReverse(curgraph):
    tmp = [[0] * len(curgraph) for _ in range(len(curgraph[0]))]
    for i in range(len(curgraph)):
        for j in range(len(curgraph[0])):
            tmp[j][i] = curgraph[i][len(curgraph[0])-j-1]

    return tmp

def solution(grid, clockwise):
    answer = []
    #시계방향
    if clockwise:
        l = (len(grid)-1)*2 + 1 #마지막 줄 길이
        graph = [['-']*l for _ in range(len(grid))]

        #시계방향이면 왼쪽을 '-'로 채우기
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                graph[i][l-len(grid[i])+j] = grid[i][j]

        temp = rotateClock(graph)
        answer.append(temp[0][0])
        for i in range(1, len(temp),2):
            line = ''
            for j in range(len(temp[0])):

                if temp[i+1][j] != '-':
                    line+=temp[i+1][j]

                if temp[i][j] != '-':
                    line+=temp[i][j]
            answer.append(line)

    #반시계방향
    else:
        l = (len(grid) - 1) * 2 + 1  # 마지막 줄 길이
        graph = [['-'] * l for _ in range(len(grid))]

        #반시계방향이면 '-'를 오른쪽에 채우기
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                graph[i][j] = grid[i][j]

        temp = rotateReverse(graph)
        answer.append(temp[0][-1])

        for i in range(1, len(temp),2):
            line = ''
            for j in range(len(temp[0])):

                if temp[i][j] != '-':
                    line+=temp[i][j]

                if temp[i+1][j] != '-':
                    line+=temp[i+1][j]

            answer.append(line)

    return answer

print(solution(["1","234"], True))