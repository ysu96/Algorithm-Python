n = int(input())
data = []
for i in range(n):
    data.append(list(map(int,input().split())))

result = 0
for i in range(1,n):
    for j in range(i+1):
        if j == 0:
            left_up = 0
            right_up = data[i-1][0]
        elif j == i:
            left_up = data[i-1][j-1]
            right_up = 0
        else:
            left_up = data[i-1][j-1]
            right_up = data[i-1][j]
        data[i][j] = data[i][j] + max(left_up,right_up)
for i in range(n):
    result = max(result, data[n-1][i])

print(result)