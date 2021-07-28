def solution(N, stages):
    answer = []
    ss = [0]*(N+2)
    challenger = [0]*(N+2)

    for i in range(len(stages)):
        ss[stages[i]] += 1
    for i in range(1,N+2):
        temp = 0
        for j in range(i,N+2):
            temp += ss[j]
        challenger[i] = temp

    ss = ss[1:-1]
    challenger = challenger[1:-1]
    fail = []
    for i in range(len(ss)):
        fail_rate = ss[i] / challenger[i]
        fail.append((fail_rate,i+1))
    fail.sort(key=lambda x:(-x[0],x[1]))
    nf = []
    for i in range(len(fail)):
        nf.append(fail[i][1])

    return nf

N = 5
stages= [2,1,2,6,2,4,3,3]
print(solution(N,stages))
