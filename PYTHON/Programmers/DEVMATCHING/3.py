board = [[0] * 6 for _ in range(6)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def checkAndPop():
    isPop = False
    for i in range(6):
        for j in range(6):
            if board[i][j] != 0:
                color = board[i][j]
                x,y = i,j
                q = [(x,y)]
                result = [(x,y)]
                cnt = 1
                while len(q) != 0:
                    x, y = q.pop(0)

                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if (nx, ny) in result:
                            continue

                        if 0 <= nx < 6 and 0 <= ny < 6:
                            if board[nx][ny] == color:
                                cnt += 1
                                q.append((nx, ny))
                                result.append((nx, ny))
                if cnt >= 3:
                    while result:
                        x, y = result.pop(0)
                        board[x][y] = 0
                        isPop = True
    return isPop



def pushDown():
    for loc in range(6):
        for i in range(5,-1,-1):
            if board[i][loc] == 0:
                for j in range(i-1,-1,-1):
                    if board[j][loc] != 0:
                        board[i][loc] = board[j][loc]
                        board[j][loc] = 0
                        break


def solution(macaron):
    answer = []
    for mc in macaron:
        loc, color = mc[0]-1, mc[1]
        for i in range(5, -1, -1):
            if board[i][loc] == 0:
                board[i][loc] = color
                while checkAndPop():
                    print(mc, board)
                    pushDown()

                break



    for i in range(6):
        sss = ''
        for j in range(6):
            sss += str(board[i][j])
        answer.append(sss)

    return board


print(solution(	[[1, 1], [1, 2], [1, 4], [2, 1], [2, 2], [2, 3], [3, 4], [3, 1], [3, 2], [3, 3], [3, 4], [4, 4], [4, 3], [5, 4], [6, 1]]   ))
