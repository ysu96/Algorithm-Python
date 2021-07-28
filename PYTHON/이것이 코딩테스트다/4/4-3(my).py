pos = input()
cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

y = int(pos[1])
for i in range(len(cols)):
    if(cols[i] == pos[0]):
        x = i+1

count = 0

if(x+2 < 8):
    if(y+1 < 8):
        count += 1
    if(y-1 > 0):
        count += 1

if(x-2 > 0):
    if(y+1 < 8):
        count += 1
    if(y-1 > 0):
        count += 1

if(y+2 < 8):
    if(x+1 < 8):
        count += 1
    if(x-1 > 0):
        count += 1

if(y-2 > 0):
    if(x+1 < 8):
        count += 1
    if(x-1 > 0):
        count += 1

print(count)