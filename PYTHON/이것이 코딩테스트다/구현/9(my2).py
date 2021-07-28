def solution(s):
    length = len(s)
    limit = length // 2
    l = 1
    result = 1e9
    while l <= limit:
        new_s = s[:l]
        answer = ''
        count = 1

        for i in range(l, length, l):
            if s[i:i + l] == new_s:
                count += 1
            else:
                answer += str(count) + new_s if count > 1 else new_s
                count = 1
                new_s = s[i:i + l]

        answer += str(count) + new_s if count > 1 else new_s
        l += 1
        result = min(result, len(answer))

    return result


s = 'abcabcdede'
print(solution(s))