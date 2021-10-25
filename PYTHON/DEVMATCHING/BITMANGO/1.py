def solution(board):
    answer = 0
    length = len(board)
    visited = [[0] * length for _ in range(length)]
    maxanswer = 0

    # 가로
    for i in range(length):
        for j in range(length):
            cnt, visited = count(board, i, j, visited)
            maxanswer += cnt
            # print(visited)
        # print(maxanswer)
        answer = max(maxanswer, answer)
        maxanswer = 0
        visited = [[0] * length for _ in range(length)]

    #세로
    for i in range(length):
        for j in range(length):
            cnt, visited = count(board, j, i, visited)
            maxanswer += cnt
            # print(visited)
        # print(maxanswer)
        answer = max(maxanswer, answer)
        maxanswer = 0
        visited = [[0] * length for _ in range(length)]

    return answer


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def count(board, x, y, visited):
    cnt = 1
    length = len(board)
    q = [(x, y)]
    if visited[x][y] == 1: return 0, visited
    visited[x][y] = 1
    while q:
        cx, cy = q.pop(0)
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < length and 0 <= ny < length:
                if visited[nx][ny] == 1:
                    continue

                if board[nx][ny] == board[cx][cy]:
                    # print(nx,ny)
                    cnt += 1
                    q.append((nx, ny))
                    visited[nx][ny] = 1

    return cnt, visited


board = ["ABBBBC", "AABAAC", "BCDDAC", "DCCDDE", "DCCEDE", "DDEEEB"]

print(solution(board))
