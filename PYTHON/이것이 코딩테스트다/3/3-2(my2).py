# 큰 수의 법칙
n,m,k = map(int,input().split())
data = list(map(int,input().split()))

data.sort()
first = data[-1]
second = data[-2]
result = 0

while 1:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1

    result += second
    m -= 1
    if m == 0:
        break

print(result)