n = int(input())
move = input().split()

x,y = 1,1

for i in move:
    if(i == 'L'):
        if(y >1):
            y -= 1
    elif(i == 'R'):
        if(y < n):
            y += 1
    elif(i == 'U'):
        if(x > 1):
            x -= 1
    else:
        if(x < n):
            x += 1

print(x,y)