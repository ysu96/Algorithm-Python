n = int(input())
students = []
for _ in range(n):
    name, a, b, c = input().split()
    students.append((name,int(a),int(b),int(c)))

students.sort(key=lambda a : (-a[1],a[2], -a[3], a[0]))
for s in students:
    print(s[0])
