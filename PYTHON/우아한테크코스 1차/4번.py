def solution(s):
    answer = []
    first = s[0]
    cnt = 1
    # 뒤부터 연결된 원소 탐색
    for i in range(len(s)-1, 0, -1):
        if s[i] == first:
            cnt += 1
        else:
            break

    # 두 번째 원소부터
    for i in range(1, len(s)-cnt+1):
        if s[i] == first:
            cnt += 1
        else:
            answer.append(cnt)
            first = s[i]
            cnt = 1

    answer.append(cnt)
    answer.sort()

    return answer

print(solution("aaba"))