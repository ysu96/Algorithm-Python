s= input()
count1 = 0
count0 = 0

for i in range(1,len(s)):
    if s[i] != s[i-1]:
        if s[i] == '0':
            count1 += 1
        else:
            count0 += 1
if s[-1] == '0':
    count1 += 1
else:
    count0 += 1

result = min(count0,count1)
print(result)
