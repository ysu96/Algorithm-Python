n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

for i in range(k):
    min_a = min(a)
    max_b = max(b)
    if min_a < max_b:
        a[a.index(min_a)], b[b.index(max_b)] = b[b.index(max_b)], a[a.index(min_a)]

print(sum(a))