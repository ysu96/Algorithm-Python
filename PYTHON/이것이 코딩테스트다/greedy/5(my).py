n,m = map(int,input().split())
balls = list(map(int,input().split()))
balls.sort()
result = 0
for x in balls:
    for y in balls:
        if x != y:
            result += 1

result //= 2
print(result)
