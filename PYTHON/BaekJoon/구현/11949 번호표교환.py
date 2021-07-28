n,m = map(int,input().split())
data = []
for _ in range(n):
    data.append(int(input()))

for i in range(1,m+1):
    for j in range(n-1):
        if data[j]%i > data[j+1]%i:
            data[j], data[j+1] = data[j+1], data[j]

for i in data:
    print(i)