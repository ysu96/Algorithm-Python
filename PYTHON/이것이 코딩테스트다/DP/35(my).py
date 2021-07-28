n = int(input())
dp = []
num = 1
dp.append(num)

while len(dp) != n:
    num += 1
    temp = num

    while temp != 1:
        if temp % 2 == 0:
            temp = temp//2
        elif temp % 3 == 0:
            temp = temp//3
        elif temp % 5 == 0:
            temp = temp//5
        else:
            break

    if temp == 1:
        dp.append(num)
    else:
        continue

print(dp[n-1])