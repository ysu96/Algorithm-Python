from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    orders.sort(key=len)

    for c in course:
        candidate = []
        for order in orders:

            order = sorted(order)

            if len(order) >= c:
                candidate += list(combinations(order,c))

                # print(c,candidates)

        aa = dict(Counter(candidate))
        print(aa)
        answer += [i for i in aa if aa[i] == aa[max(aa, key=aa.get)] and aa[i] >= 2]
        # print(answer)

    answer.sort()
    for i in range(len(answer)):
        tmp = ''
        for j in answer[i]:
            tmp += j
        answer[i] = tmp
    print(answer)




    return answer

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course=[2,3,4]
orders = ["XYZ", "XWY", "WXA"]
course =[2,3,4]

solution(orders,course)