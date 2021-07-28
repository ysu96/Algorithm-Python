def balanced(s):
    left = 0
    for i in range(len(s)):
        if s[i] == '(':
            left+=1
        else:
            left-=1
        if left == 0:
            return i

def check(s):
    left = 0

    for i in s:
        if i == '(':
            left += 1
        else:
            left -= 1

            if left < 0:
                return False
    return True

def solution(p):
    answer = ''

    if p == '':
        return ''

    index = balanced(p)
    u,v = p[:index+1], p[index+1:]

    if check(u):
        answer = u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])

        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
    return answer
