def solution(gems):
    answer = []
    count = len(set(gems))
    l = count
    r = len(gems)
    length = len(gems)
    while l <= r:
        mid = (l+r)//2
        ok = False
        for i in range(length-mid+1):
            if len(set(gems[i:i+mid])) == count:
                r = mid-1
                a1 = i+1
                a2 = i+mid
                ok = True
                break
        print('a')
        if ok == False:
            l = mid+1


    return [a1,a2]

gems =["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
#["AA", "AB", "AC", "AA", "AC"]  #	[1, 3]
gems = ["XYZ", "XYZ", "XYZ"]	#[1, 1]
print(solution(gems))