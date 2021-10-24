def solution(progresses, speeds):
    answer = []
    tmp = []
    for i in range(len(progresses)):
        left = 100 - progresses[i]
        days = left // speeds[i]
        if left % speeds[i] != 0:
            days+=1
        tmp.append(days)
    # print(tmp)
    left = tmp[0]
    cnt = 1
    for i in range(1,len(tmp)):
        if tmp[i] <= left:
            cnt+=1
            continue
        else:
            answer.append(cnt)
            cnt = 1
            left = tmp[i]
    answer.append(cnt)
    return answer


progresses = [93, 30, 55]
speeds = [1, 30, 5]	#[2, 1]
print(solution(progresses, speeds))
# [95, 90, 99, 99, 80, 99]	[1, 1, 1, 1, 1, 1]	[1, 3, 2]