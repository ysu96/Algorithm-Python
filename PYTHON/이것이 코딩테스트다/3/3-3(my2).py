n,m = map(int,input().split())
datas = []
for i in range(n):
    data = list(map(int,input().split()))
    datas.append(min(data))

print(max(datas))
