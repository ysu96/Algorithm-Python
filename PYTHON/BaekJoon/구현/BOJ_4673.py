checklist = [False] * 10001
for i in range(1,10001):
    dn = i + sum(list(map(int,str(i))))
    if dn<= 10000:
        checklist[dn] = True

for i in range(1,10001):
    if checklist[i] == False:
        print(i)

