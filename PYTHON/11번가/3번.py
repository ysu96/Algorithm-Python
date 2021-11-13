def solution(A):
    # write your code in Python 3.6
    tmp = A[0]
    cnt = 1
    answer = 0
    for i in range(1,len(A)):
        if A[i] == tmp:
            cnt += 1
        else:
            if tmp < cnt:
                answer += (cnt-tmp)
            elif tmp - cnt >= cnt:
                answer += cnt
            else:
                answer += (tmp-cnt)

            tmp = A[i]
            cnt = 1

    if tmp < cnt:
        answer += (cnt - tmp)
    elif tmp - cnt >= cnt:
        answer += cnt
    else:
        answer += (tmp - cnt)

    print(answer)
    return answer



solution([1,3,3,3,4,4,4,4])