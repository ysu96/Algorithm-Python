s = input()
result = 1
num = []

for i in s:
    num.append(int(i))

if len(num) == 1:
    print(num[0])

for i in range(len(num)):
    if num[i] == 1:
        if i == 0:
            num[1] += 1
        elif i == len(num)-1:
            num[len(num)-2] += 1
        else:
            if num[i-1] > num[i+1]:
                num[i+1] += 1
            else:
                num[i-1] += 1


for i in range(len(num)):
    if num[i] == 0 or num[i] == 1:
        continue
    result *= num[i]

print(result)

