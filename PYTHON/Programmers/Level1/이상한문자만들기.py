def solution(s):
    answer = ''
    slist = s.split(' ')
    print(slist)
    length= len(s)
    for ss in slist:
        length = len(ss)
        for i in range(0, length):
            if (i % 2 == 0):
                answer += ss[i].upper()
            else:
                answer += ss[i].lower()
        answer+=' '

    return answer[:-1]

print(solution("try   hello world"))
print('A'.lower())