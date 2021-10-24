black = [[0] * 32] * 32
def recursion(start, end, depth, s, turn):
    sx = start[0]
    sy = start[1]
    if s == 'b':
        for i in range(sx, end[0]):
            for j in range(sy, end[1]):
                black[i][j] = 1
        return turn+1
    elif s== 'w':
        return turn +1


                #ny = sy+ 32 / (2 ** depth)

def solution(s1, s2):

    currentRoot = [[0,0]]
    depth = 0
    cnt = 0
    turn = 1

    start = [0,0]
    end = [32,32]
    for i in range(len(s1)):
        if s1[i] == 'p':
            depth += 1
            if turn == 1:
                nx = start[0]
                ny = start[1] + 32 / (2 ** depth)
            elif turn == 2:
                nx = start[0]
                ny = start[1]
            elif turn == 3:
                nx = start[0] + 32 / (2 ** depth)
                ny = start[1]
            else:
                nx = start[0] + 32 / (2 ** depth)
                ny = start[1] + 32 / (2 ** depth)

            start = [nx,ny]

        else:
            turn = recursion(start, end, depth, s1[i], turn)
            if turn > 4:
                turn = 1




s1 = "ppwwwbpbbwwbw"
s2 = "pwbwpwwbw"
ans = "ppwwwbbbpwwbw"
solution(s1,s2)
#640