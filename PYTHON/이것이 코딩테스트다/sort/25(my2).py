def solution(N, stages):
    stages_all = [0]*N
    stages_noclear = [0]*N
    for i in range(len(stages)):
        if stages[i] == N+1:
            for j in range(len(stages_all)):
                stages_all[j] += 1
        else:
            for j in range(stages[i]):
                stages_all[j] += 1

            stages_noclear[stages[i]-1] += 1

    fail = []
    print(stages_all)
    print(stages_noclear)
    for i in range(N):
        if stages_all[i] == 0:
            fail_rate = 0
        else:
            fail_rate = stages_noclear[i] / stages_all[i]
        fail.append((fail_rate,i+1))

    fail.sort(key= lambda a:(-a[0], a[1]))

    answer = []
    for f in fail:
        answer.append(f[1])
    return answer

N = 5
#현재 멈춰있는 스테이지
stages= [2,1,2,6,2,4,3,3]
#result = [3,4,2,1,5]
print(solution(N,stages))