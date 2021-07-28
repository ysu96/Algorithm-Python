def solution(t, r):
    answer = []
    tr = []
    #시간, 등급, 번호
    for i,time in enumerate(t):
        tr.append([time,r[i],i])
    tr.sort()
    nn = sorted(t)
    now_time = 0

    while tr:

        if min(nn) > now_time:
            now_time = min(nn)


        # print("tr:", tr)
        candidate = []
        for i in range(len(tr)):
            if tr[i][0] <= now_time:
                candidate.append(tr[i])

        # print("candidate1:",candidate)

        min_rate = 1e9
        for j in range(len(candidate)):
            if candidate[j][1] < min_rate:
                min_rate = candidate[j][1]

        # print(min_rate)

        candidate2 = []
        for i in range(len(candidate)):
            if candidate[i][1] == min_rate:
                candidate2.append(candidate[i])

        # print("candi2:",candidate2)

        candidate2.sort(key=lambda a:a[0])
        tr.remove(candidate2[0])
        nn.remove(candidate2[0][0])
        candidate3 = candidate2[0][2]
        answer.append(candidate3)
        now_time += 1

        # print(tr)
    # print(tr)
    return answer


t=[0,1,3,0]
r=[0,1,2,3]
#[0, 1, 3, 2]
print(solution(t,r))
# [7,6,8,1]	[0,1,2,3]	[3, 1, 0, 2]