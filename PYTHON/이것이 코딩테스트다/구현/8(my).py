s = list(input())
string = []
number = []
for i in s:
    if i >= 'A' and i <= 'Z':
        string.append(i)
    else:
        number.append(int(i))

string.sort()
number.sort()
for i in string:
    print(i,end='')
print(sum(number))