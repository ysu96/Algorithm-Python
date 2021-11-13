
def solution(S):
    # write your code in Python 3.6
    blocks = []
    tmp = S[0]
    cnt = 1
    answer = 0

    for i in range(1,len(S)):
        if S[i] == tmp:
            cnt += 1
        else:
            blocks.append(cnt)
            tmp = S[i]
            cnt = 1

    blocks.append(cnt)

    maxcnt = max(blocks)
    for b in blocks:
        answer += (maxcnt-b)

    print(answer)
    return answer



solution("bbbbbaaaaabbbbb")
