x = int(input())

if x<=5:
    if x==1: print(0)
    elif x==2 or x==3 or x==5: print(1)
    else: print(2)
else:
    d = [0]*(x+1)
    d[1] = 0
    d[2] = 1
    d[3] = 1
    d[4] = 2
    d[5] = 1
    for i in range(6,x+1):
        d[i] = d[i-1] + 1

        if(i%2 == 0):
            d[i] = min(d[i], d[i//2]+1)
        if i%3 == 0:
            d[i] = min(d[i], d[i//3]+1)
        if i%5 == 0:
            d[i] = min(d[i], d[i//5]+1)

print(d[x])

