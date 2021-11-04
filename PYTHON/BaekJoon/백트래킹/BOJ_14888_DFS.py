import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
ops = list(map(int,input().split()))

minimum = 1e9
maximum = -1e9

def dfs(depth, num, plus, minus, multiply, divide):
    global maximum, minimum
    if depth == n:
        maximum = max(maximum, num)
        minimum = min(minimum, num)
        return

    if plus:
        dfs(depth + 1, num+nums[depth], plus-1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, num-nums[depth],plus, minus-1, multiply, divide)
    if multiply:
        dfs(depth + 1, num * nums[depth],plus, minus, multiply-1, divide)
    if divide:
        dfs(depth + 1, int(num / nums[depth]), plus, minus, multiply, divide-1)

dfs(1, nums[0], ops[0], ops[1], ops[2], ops[3])

print(maximum)
print(minimum)