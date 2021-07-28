n = int(input())
data = list(map(int,input().split()))
data.sort()
result = 0
temp = []
for i in range(n):
    temp.append(data[i])
    if data[i] <= len(temp):
        result += 1
        temp = []

print(result)
