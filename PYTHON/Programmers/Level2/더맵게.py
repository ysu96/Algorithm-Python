import heapq
def solution(scoville, K):
    answer = 0
    heap = []
    for s in scoville:
        heapq.heappush(heap, s)

    while heap[0] < K:
        try:
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)
            heapq.heappush(heap, first + (second * 2))
            answer += 1
        except:
            return -1

    return answer


scoville = [1, 2, 3, 9, 10, 12]
k = 7
print(solution(scoville, k))
