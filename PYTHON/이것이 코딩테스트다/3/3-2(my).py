a = input().split()
n = int(a[0])
m = int(a[1])
k = int(a[2])

b = input().split()
num = []
for i in range(n):
    num.append(int(b[i]))

num.sort(reverse=True)

count = 0
kc = 0
for i in range(m):
    if kc == k:
        count += num[1]
        kc = 0
    else:
        count += num[0]
        kc += 1

print(count)
