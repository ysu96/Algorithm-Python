a = input()
b = input()

length_a = len(a)
length_b = len(b)

dp = [[1e9]*(length_a+1) for _ in range(length_b+1)]
for i in range(length_a+1):
    dp[0][i] = i
for i in range(length_b+1):
    dp[i][0] = i

for i in range(1,length_b+1):
    for j in range(1,length_a+1):
        if b[i-1] == a[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

print(dp[length_b][length_a])

