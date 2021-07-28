array = [7,5,9,0,2,5,4,2,6,7,4,8,9,6,1,3]

count = [0]*(max(array)+1)
for i in array:
    count[i] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')