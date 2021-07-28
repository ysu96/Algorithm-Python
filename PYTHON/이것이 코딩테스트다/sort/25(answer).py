def solution(N, stages):
    answer = []
    length = len(stages)

    #스테이지 번호를 1부터 N까지 증가시키며
    for i in range(1,N+1):
        #해당 스테이지에 있는 사람 수 계산
        count = stages.count(i)

        if length == 0:
            fail = 0
        else:
            fail = count / length

        answer.append((i,fail))
        length -= count

    answer = sorted(answer, key=lambda t: t[1], reverse=True)
    answer = [i[0] for i in answer]
    return answer