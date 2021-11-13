def solution(A):
    A.sort(reverse=True)
    answer = 0
    isOdd = False
    isEven = False
    for i in range(len(A)):
        if A[i] % 2 == 0:
            if isEven == False:
                isEven = True
                answer+=A[i]
                if isOdd == True:
                    return answer

        else:
            if isOdd == False:
                isOdd = True
                answer+=A[i]
                if isEven == True:
                    return answer

    print(A)
    print(answer)
    return answer


solution([5,3,10,6,11])