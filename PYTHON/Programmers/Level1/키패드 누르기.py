def solution(numbers, hand):
    answer = ''
    left = [3,0]
    right = [3,2]

    keypad = [[1,2,3], [4,5,6], [7,8,9], ['*',0,'#']]
    for n in numbers:
        for i in range(4):
            for j in range(3):
                if keypad[i][j] == n:
                    if n in [1,4,7]:
                        answer+='L'
                        left = [i,j]
                    elif n in [3,6,9]:
                        answer +='R'
                        right = [i,j]
                    else:
                        ldist = abs(left[0]-i) + abs(left[1]-j)
                        rdist = abs(right[0]-i) + abs(right[1]-j)
                        if ldist < rdist:
                            answer+='L'
                            left = [i,j]
                        elif rdist < ldist:
                            answer+='R'
                            right = [i,j]
                        else:
                            if hand == 'right':
                                answer+='R'
                                right = [i,j]
                            else:
                                answer+='L'
                                left = [i,j]
    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))	#"LRLLLRLLRRL"