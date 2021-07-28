def solution(numbers):
    l = len(numbers)
    numbers = list(map(str,numbers))


    numbers.sort(key=lambda a: a*3, reverse=True)
    answer = str(int("".join(numbers)))
    return answer