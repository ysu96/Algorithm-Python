def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if completion[i] != participant[i]:
            return participant[i]

    return participant[-1]


import collections
a=["leo", "kiki", "eden"]
b=["kiki", "eden"]
print(list(collections.Counter(a)-collections.Counter(b)))