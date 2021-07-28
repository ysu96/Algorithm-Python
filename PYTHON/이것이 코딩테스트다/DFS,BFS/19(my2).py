from itertools import permutations

n = int(input())
A = list(map(int,input().split()))
calculate = list(map(int,input().split()))
c = []
for _ in range(calculate[0]):
    c.append(1)
for _ in range(calculate[1]):
    c.append(2)
for _ in range(calculate[2]):
    c.append(3)
for _ in range(calculate[3]):
    c.append(4)

candidates = list(permutations(c,n-1))
# print(candidates)
max_answer = -1e9
min_answer = int(1e9)
for candidate in candidates:
    answer = A[0]
    for i in range(n-1):

        if candidate[i] == 1:
            answer += A[i+1]
        elif candidate[i] == 2:
            answer -= A[i+1]
        elif candidate[i] == 3:
            answer *= A[i+1]
        else:
            answer /= A[i+1]
            answer = int(answer)

    max_answer = max(max_answer, answer)
    min_answer = min(min_answer, answer)

print(max_answer)
print(min_answer)
