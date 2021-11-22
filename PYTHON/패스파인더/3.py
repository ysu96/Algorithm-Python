[5,1,2,3,1,2], 1
2, [3,1,1,1]

def segment(x, space):
    # Write your code here
    mins = []
    min_num = 1e9
    second_min = 1e9
    startIdx = 0
    answer = 0
    # for i in range(len(space)-x+1):
    #     answer = max(min(space[i:i+x]), answer)
    #
    # return answer
    #
    for i in range(len(space)):

        if min_num > space[i]:
            second_min = min_num
            min_num = space[i]

        elif second_min > space[i]:
            second_min = space[i]


        if i - startIdx + 1 == x:
            mins.append(min_num)

            if min_num == space[startIdx]:
                min_num = second_min
                second_min = 1e9
            startIdx += 1

        # mins.append(min(space[i:i+x]))

    return max(mins)

vvv
print(segment(2, [1,2,3,1,2]))