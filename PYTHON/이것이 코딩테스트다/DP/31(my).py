
def find_gold(array,n,m):
    result = 0

    for i in range(n):
        if array[i][0] > result:
            result = array[i][0]
            x = i

    for i in range(1,m):
        if x-1 < 0:
            next = array[x][i]
            down = array[x+1][i]

            x = x if next >= down else x+1
            result += array[x][i]
        elif x+1 >= n:
            up = array[x-1][i]
            next = array[x][i]

            x = x if next >= up else x - 1
            result += array[x][i]
        else:
            up = array[x-1][i]
            next = array[x][i]
            down = array[x+1][i]
            if next >= up:
                if next >= down:
                    x = x
                else:
                    x = x+1
            else:
                if up>= down:
                    x = x-1
                else:
                    x = x+1
            result += array[x][i]

    return result


t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    array = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            array[i][j] = data[i * m + j]

    print(find_gold(array, n, m))
