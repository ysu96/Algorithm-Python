n = int(input())
data = list(map(int,input().split()))
m = int(input())
data_m = list(map(int,input().split()))

for i in data_m:
    if i in data:
        print("yes", end=' ')
    else:
        print("no", end=' ')