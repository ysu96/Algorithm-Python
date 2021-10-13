def solution(board, moves):
    answer = 0
    bucket = [0]
    board_len = len(board)
    for i in moves:
        for j in range(0,board_len):
            if board[j][i-1] != 0:
                get = board[j][i-1]

                if bucket[-1] == get:
                    bucket.pop()
                    answer+=2
                else:
                    bucket.append(get)

                board[j][i-1] = 0
                break

    return answer

# board	moves	result
# [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]	[1,5,3,5,1,2,1,4]	4

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))