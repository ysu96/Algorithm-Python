def solution(numbers, hand):
    answer = ''
    graph = [[(i*3)+1, (i*3)+2, (i*3)+3] for i in range(4)]
    graph[3][1] = 0
    lx,ly = 3,0
    rx,ry = 3,2
    for number in numbers:
        for i in range(4):
            for j in range(3):
                if graph[i][j] == number:
                    if number in [1, 4, 7]:
                        lx = i
                        ly = j
                        answer += 'L'
                    elif number in [3,6,9]:
                        rx = i
                        ry = j
                        answer += 'R'
                    else:
                        ll = abs(i-lx)+abs(j-ly)
                        rr = abs(i-rx)+abs(j-ry)
                        if ll == rr:
                            if hand == "right":
                                rx = i
                                ry = j
                                answer += 'R'
                            else:
                                lx = i
                                ly = j
                                answer += 'L'
                        elif ll > rr:
                            rx = i
                            ry = j
                            answer += 'R'
                        else:
                            lx = i
                            ly = j
                            answer += 'L'

    return answer

# [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	"right"	"LRLLLRLLRRL"
numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
print(solution(numbers, hand))
# "LRLLLRLLRRL"
# [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]	"left"	"LRLLRRLLLRR"
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]	"right"	"LLRLLRLLRL"
