n,m = map(int,input().split())
num = []
for i in range(n):
    num.append(list(map(int,input().split())))

mins = []
for i in range(n):
    mins.append(min(num[i]))

print(max(mins))
