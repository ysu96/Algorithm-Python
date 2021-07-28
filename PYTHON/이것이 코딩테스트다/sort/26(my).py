n = int(input())
data = []
for i in range(n):
    data.append(int(input()))

data.sort()

if len(data) <= 2:
    result = sum(data)

result = data[0]+data[1]
for i in data[2:]:
    temp = result + i
    result += temp

print(result)