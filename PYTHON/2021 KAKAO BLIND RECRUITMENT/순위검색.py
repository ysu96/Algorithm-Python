def solution(info, query):
    answer = []
    info_n = []
    info_dict = dict()
    for a in ['python','java','cpp','-']:
        for b in ['frontend','backend','-']:
            for c in ['junior','senior','-']:
                for d in ['chicken','pizza','-']:
                    info_dict[a+b+c+d] = []


    for i in info:
        i = i.split()
        for a in [i[0],'-']:
            for b in [i[1],'-']:
                for c in [i[2], '-']:
                    for d in [i[3], '-']:
                        info_dict[a+b+c+d].append(int(i[4]))

    for d in info_dict:
        info_dict[d].sort()

    for q in query:
        qq = [i for i in q.split() if i!="and"]
        ll = info_dict[qq[0]+qq[1]+qq[2]+qq[3]]
        find = int(qq[4])
        left = 0
        right = len(ll)
        while left < right:
            mid = (left+right)//2
            if ll[mid] >= find:
                right = mid
            else:
                left = mid+1
        answer.append(len(ll)-left)
    return answer

info = ["java backend junior pizza 150",
        "python frontend senior chicken 210",
        "python frontend senior chicken 150",
        "cpp backend senior pizza 260",
        "java backend junior chicken 80",
        "python backend senior chicken 50"]

query = ["java and backend and junior and pizza 100",
         "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250",
         "- and backend and senior and - 150",
         "- and - and - and chicken 100",
         "- and - and - and - 150"]
print(solution(info,query))
