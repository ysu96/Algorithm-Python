n = int(input())
houses = list(map(int,input().split()))
houses.sort()
result = 1e9

ant = 0
for i in range(n):
    temp = 0
    for j in range(n):
        temp += abs(houses[i] - houses[j])
    if result > temp:
        ant = houses[i]
        result = temp


print(ant)
