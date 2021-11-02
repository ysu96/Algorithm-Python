n = int(input())
dp = ['-']*(n+1)
dp[0] = 0
dp[1] = 1
def fibo(n):
    if n == 1:
        return 1
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
print(fibo(n))