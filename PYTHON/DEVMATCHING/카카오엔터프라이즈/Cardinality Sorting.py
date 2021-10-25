def solution(nums):
    answer = []
    bcs = []
    for n in nums:
        bn = bin(n)[2:]
        bc.append((bn.count('1'), n))

    bcs.sort(key=lambda x : (x[0], x[1]))

    for bcc in bcs:
        answer.append(bcc[1])

    print(answer)
    return answer

solution([31,15,7,3,2])