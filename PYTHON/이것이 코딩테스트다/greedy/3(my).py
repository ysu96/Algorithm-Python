s = input()
num = 0
if s[0] == '0':
    s = s.strip('0')

else:
    s = s.strip('1')

while s:
    if s[0] == '0':
        s = s.strip('0')
        num += 1
    else:
        s= s.strip('1')
        num += 1
print(num)

