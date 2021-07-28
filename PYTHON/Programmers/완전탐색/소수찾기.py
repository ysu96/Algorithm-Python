from itertools import permutations
def check(num):
    if num == 1 or num == 0:
        return False

    for i in range(2,num):
        if num%i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    data = []
    for number in numbers:
        data.append(number)
    data.sort()
    candidates = []
    for i in range(1,len(data)+1):
        candidates += list(set(permutations(data,i)))
    result = []
    for candidate in candidates:
        num = int("".join(candidate))
        if check(num) and num not in result:
            result.append(num)
            answer += 1
    print(result)

    return answer