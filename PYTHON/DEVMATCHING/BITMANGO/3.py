def solution(n, capacity, files):
    answer = -1
    nn = len(capacity)
    dp = [[0]*100001 for _ in range(nn)]
    ddp(0, 0, dp, files, capacity)
    return answer

def ddp(now, c, dp, files, capacity): #고민하고 있는 상품의 인덱스  now번째 이전까지 담은 상품들의 총 무게
    if c > capacity:
        return 0
    if now == len(capacity):
        return 0
    if dp[now][c] != 0:
        return dp[now][c]

    tmp1 = files[now] + ddp(now + 1, c + files[now], dp, files)
    tmp2 = ddp(now + 1, c, dp, files)
    if tmp1 < capacity:
        dp[now][c] = tmp1
        return tmp1
    else:
        tmp2 =


    ans = max(tmp1, tmp2)
    dp[now][c] = ans
    return ans

