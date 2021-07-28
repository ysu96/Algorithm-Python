n = int(input())
data = []
for i in range(n):
    name, grade = input().split()
    data.append((name,int(grade)))

def setting(data):
    return data[1]

data.sort(key=setting)
for i in data:
    print(i[0], end=' ')