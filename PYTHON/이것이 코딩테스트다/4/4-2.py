n = int(input())

m = 60
s = 60
count = 0
for i in range(n+1):
    for j in range(m):
        for k in range(s):
            if('3' in str(i) + str(j) + str(k)):
                count += 1

print(count)