def solution(lottos, win_nums):
    zeroCnt = len([0 for i in lottos if i==0])
    # zeroCnt=lottos.count(0)
    count = 0
    for i in win_nums:
        for j in lottos:
            if j==0: continue
            if i==j: count+=1

    if count > 1:
        min = 7-count
    else:
        min = 6

    if (count+zeroCnt) < 2:
        max = 6
    else:
        max = 7-(count+zeroCnt)

    return [max, min]