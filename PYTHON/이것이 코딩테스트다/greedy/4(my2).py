n = int(input())
coins = list(map(int,input().split()))
coins.sort()

if coins[0] > 1:
    sum = 1

else:
    sum = coins[0]
    for i in range(1,n):
        if (sum+1) < coins[i]:
            break
        sum += coins[i]
    sum += 1

print(sum)