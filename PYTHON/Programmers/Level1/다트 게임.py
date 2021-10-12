def solution(dartResult):
    answer = []
    score = ""
    nscore = -1
    for i in range(0, len(dartResult)):
        if dartResult[i].isdigit():
            if nscore != -1:
                answer.append(nscore)
                nscore = -1

            # score = int(dartResult[i])
            score+=dartResult[i]

        elif dartResult[i].isalpha():
            nscore = int(score)
            score = ""
            if dartResult[i] == 'S':
                nscore = nscore**1
            elif dartResult[i] == 'D':
                nscore = nscore ** 2
            else:
                nscore = nscore ** 3

            if i == len(dartResult)-1:
                answer.append(nscore)

        else:
            if dartResult[i] == '*':
               nscore *= 2
               if len(answer) != 0:
                   answer[-1] *= 2
                   answer.append(nscore)
                   nscore = -1
            else:
                nscore*=-1
                answer.append(nscore)
                nscore = -1


    print(answer)
    return sum(answer)

print(solution("10S10S10S"))
# 다트 게임은 총 3번의 기회로 구성된다.
# 각 기회마다 얻을 수 있는 점수는 0점에서 10점까지이다.
# 점수와 함께 Single(S), Double(D), Triple(T) 영역이 존재하고 각 영역 당첨 시 점수에서 1제곱, 2제곱, 3제곱 (점수1 , 점수2 , 점수3 )으로 계산된다.
# 옵션으로 스타상(*) , 아차상(#)이 존재하며 스타상(*) 당첨 시 해당 점수와 바로 전에 얻은 점수를 각 2배로 만든다. 아차상(#) 당첨 시 해당 점수는 마이너스된다.
# 스타상(*)은 첫 번째 기회에서도 나올 수 있다. 이 경우 첫 번째 스타상(*)의 점수만 2배가 된다. (예제 4번 참고)
# 스타상(*)의 효과는 다른 스타상(*)의 효과와 중첩될 수 있다. 이 경우 중첩된 스타상(*) 점수는 4배가 된다. (예제 4번 참고)
# 스타상(*)의 효과는 아차상(#)의 효과와 중첩될 수 있다. 이 경우 중첩된 아차상(#)의 점수는 -2배가 된다. (예제 5번 참고)
# Single(S), Double(D), Triple(T)은 점수마다 하나씩 존재한다.
# 스타상(*), 아차상(#)은 점수마다 둘 중 하나만 존재할 수 있으며, 존재하지 않을 수도 있다.
# 1S2D*3T	37