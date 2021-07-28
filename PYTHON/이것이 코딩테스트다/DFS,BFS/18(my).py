def check(p):
    countL = 0
    countR = 0
    countA = 0
    for i in p:
        if i == '(':
            countL += 1
        else:
            countR += 1
            if countR > countL:
                return False
            else:
                countL -= 1
                countR -= 1
                countA += 1
    if countA == len(p)/2:
        return True
    else:
        return False

def divide(p):
    countL = 0
    countR = 0
    u = ''
    v = ''
    for i in range(len(p)):
        if p[i] == '(':
            countL += 1
            u+=p[i]
        else:
            countR += 1
            u+=p[i]

        if countL == countR:
            v = p[i+1:]
            break

    return u,v

def solution(p):
    answer = ''
    while 1:
        if p == '':
            return ''

        u,v = divide(p)
        if check(u):
            answer += u
            answer += solution(v)
            return answer
        else:
            temp = '('
            temp += solution(v)
            temp += ')'
            new_u = u[1:len(u)-1]
            new_u2 = ''
            for i in range(len(new_u)):
                if new_u[i] == '(':
                    new_u2 += ')'
                else:
                    new_u2 += '('
            temp += new_u2
            return temp

print(solution("()))((()"))

