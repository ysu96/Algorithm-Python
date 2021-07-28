def solution(citations):
    answer = 0
    citations.sort()
    h = 0
    while 1:
        count = 0
        for c in citations:
            if c >= h:
                count += 1
        if count >= h:
            answer = h
        else:
            break
        h+=1

    return answer