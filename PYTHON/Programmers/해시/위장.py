def solution(clothes):
    answer = 0
    hash = {}
    for cloth in clothes:
        hash[cloth[1]] = list()
    for cloth in clothes:
        hash[cloth[1]].append(cloth[0])
    answer = 1
    for c in hash:
        answer *= (len(hash[c])+1)
    answer -= 1


    return answer

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))