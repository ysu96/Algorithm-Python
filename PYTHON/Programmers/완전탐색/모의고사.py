def solution(answers):
    answer = []
    l = len(answers)
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]
    t1 = l // len(first)
    t2 = l // len(second)
    t3 = l // len(third)
    first = (first*(t1+1))[:l]
    second = (second*(t2+1))[:l]
    third = (third * (t3 + 1))[:l]

    answer1 = 0
    answer2 = 0
    answer3 = 0

    for i in range(l):
        if answers[i] == first[i]:
            answer1 += 1
        if answers[i] == second[i]:
            answer2 += 1
        if answers[i] == third[i]:
            answer3 += 1

    tmp = [(answer1,1), (answer2,2), (answer3,3)]
    tmp.sort(reverse=True)
    answer.append(tmp[0][1])
    for i in range(1,3):
        if tmp[i][0] == tmp[0][0]:
            answer.append(tmp[i][1])
        else:
            break
    answer.sort()
    return answer