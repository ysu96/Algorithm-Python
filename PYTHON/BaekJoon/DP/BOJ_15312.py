cnt = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1 ]
A = input()
B = input()
shake = []
length = len(A)
for i in range(length):
    shake.append(cnt[ord(A[i])-65])
    shake.append(cnt[ord(B[i])-65])

while len(shake) > 2:
    for i in range(len(shake)-1):
        shake[i] = (shake[i]+shake[i+1]) % 10
    shake = shake[:-1]

ans = ''
for s in shake:
    ans += str(s)
print(ans)


