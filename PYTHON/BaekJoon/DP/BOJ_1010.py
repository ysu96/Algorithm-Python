#강 주변에서 다리를 짓기에 적합한 곳을 사이트라고 한다. 강의 서쪽에는 N개의 사이트가 있고 동쪽에는 M개의 사이트가 있다는 것을 알았다. (N ≤ M)
#서쪽의 사이트 개수만큼 (N개) 다리를 지으려고 한다. 다리끼리는 서로 겹쳐질 수 없다고 할 때 다리를 지을 수 있는 경우의 수를 구하는 프로그램을 작성하라.
#
# 입력
# 입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다. 그 다음 줄부터 각각의 테스트케이스에 대해 강의 서쪽과 동쪽에 있는 사이트의 개수 정수 N, M (0 < N ≤ M < 30)이 주어진다.
#
# 출력
# 각 테스트 케이스에 대해 주어진 조건하에 다리를 지을 수 있는 경우의 수를 출력한다.


# 서쪽에 1개, 동쪽에 n개 있을 때 다리는 n개 지을 수 있음
# 서쪽의 개수와 동쪽의 개수가 똑같으면 경우의 수는 1이다
# 서쪽 n, 동쪽 m이면 : (서쪽 n 동쪽 m-1 일떄의 경우의 수) + (서쪽 n-1, 동쪽 m-1 일 때의 경우의 수)
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1:
                dp[i][j] = j
                continue
            if i==j:
                dp[i][j] = 1
            else:
                if j>i:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j-1]

    print(dp[n][m])

