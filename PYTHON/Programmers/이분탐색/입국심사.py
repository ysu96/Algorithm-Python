

def solution(n, times):
    start = 1
    end = n * max(times)
    answer = 0

    while start <= end:
        mid = (start + end) // 2
        tsum = sum([mid // t for t in times])

        if tsum >= n:
            answer = mid
            end = mid-1

        elif tsum < n:
            start = mid+1

    return answer

n =6
times = [7, 10]
print(solution(n,times))