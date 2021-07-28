s = input()
alpha = []
num = 0
for i in s:
    if i.isalpha():
        alpha.append(i)
    else:
        num += int(i)

alpha = sorted(alpha)

print(''.join(alpha),end='')
print(num)
