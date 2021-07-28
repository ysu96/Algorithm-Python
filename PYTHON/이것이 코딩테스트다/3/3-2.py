n,m,k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

c = m//(k+1)
cc = m%(k+1)
result = c*(first*k + second) + cc*first
print(result)
