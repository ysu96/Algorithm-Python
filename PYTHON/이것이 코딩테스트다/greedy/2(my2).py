s = input()
result = 0

for i in range(len(s)):
    if int(s[i]) == 0 or int(s[i]) == 1 or result <= 1:
        result += int(s[i])
    else:
        result *= int(s[i])

print(result)