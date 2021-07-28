
import heapq
def solution(begin, target, words):
    answer = 0
    length = len(begin)
    if target not in words:
        return 0

    # 바꾼 횟수 , 시작 단어
    q = [(0,begin)]

    while q:
        count, now = heapq.heappop(q)
        if now in words:
            words.remove(now)

        if now == target:
            return count


        for word in words:
            mismatch = 0
            for i in range(length):
                if now[i] != word[i]:
                    mismatch += 1

            if mismatch == 1:
                heapq.heappush(q, (count+1, word))


    return 0