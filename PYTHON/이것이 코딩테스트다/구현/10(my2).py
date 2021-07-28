def rotate(key):
    new_key = [[0]*(len(key)) for _ in range(len(key))]
    for i in range(len(key)):
        for j in range(len(key)):
            new_key[i][j] = key[j][len(key)-i-1]
    return new_key


def solution(key, lock):
    m = len(key)
    n = len(lock)
    new_lock = [[0]*(n*3) for _ in range(n*3)]
    for i in range(n):
        for j in range(n):
            if lock[i][j] == 1:
                new_lock[i+n][j+n] = 1


    for _ in range(4):

        for x in range(n*2):
            for y in range(n * 2):
                answer = True
                for i in range(m):
                    for j in range(m):
                        if key[i][j] == 1:
                            new_lock[x+i][y+j] += 1

                for i in range(n):
                    for j in range(n):
                        if new_lock[i+n][j+n] != 1:
                            answer = False

                if answer == True:
                    return True
                else:
                    for i in range(m):
                        for j in range(m):
                            if key[i][j] == 1:
                                new_lock[x + i][y + j] -= 1

        key = rotate(key)

    return False