def solution(arr):
    answer = []
    one = arr.count(1)
    two = arr.count(2)
    three = arr.count(3)
    maxcnt = max(max(one,two), three)
    answer.append(maxcnt-one)
    answer.append(maxcnt-two)
    answer.append(maxcnt-three)

    return answer

print(solution([1,1]))