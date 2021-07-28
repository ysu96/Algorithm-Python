for _ in range(int(input())):
    n,m = map(int,input().split())
    array = list(map(int,input().split()))
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index + m])
        index += m

    for j in range(1,m):
        for i in range(n):
            if i-1 < 0:
                dp[i][j] = dp[i][j] + max(dp[i][j-1], dp[i+1][j-1])
            elif i+1 >= n:
                dp[i][j] = dp[i][j] + max(dp[i][j-1], dp[i-1][j-1])
            else:
                dp[i][j] = dp[i][j] + max(dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1])

    result = 0
    for i in range(n):
        result = max(dp[i][m-1], result)
    print(result)