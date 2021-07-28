n = int(input())
d = [0]*n
d[0] = 1
d[1] = 3
d[2] = 5
for i in range(3,n):
    d[i] = (d[i-1] + d[i-2]*2) % 796796

print(d[n-1])

