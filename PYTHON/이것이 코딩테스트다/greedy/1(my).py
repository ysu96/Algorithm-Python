n = int(input())
data = list(map(int,input().split()))

data.sort()
count = 0
tmp = []
result = 0
for i in range(n):
    count += 1
    if data[i] > count:
        continue
    else:
        result += 1
        count = 0

print(result)
