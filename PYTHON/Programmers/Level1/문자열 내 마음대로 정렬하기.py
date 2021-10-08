def solution(strings, n):
    answer = []
    return sorted(strings, key=lambda x : (x[1], x))

print(solution(["abzcd","cdzab","abzfg","abzaa","abzbb","bbzaa"], 2))