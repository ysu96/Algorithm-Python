def solution(maps, p, r):
    answer = 0
    n = len(maps)
    r = r//2
    for i in range(n+1):
        for j in range(n+1):
            #마법을 ij에서 사용하면
            # rr = j + r/2 if j+r/2 < 8 else 7
            # lr = j - r/2 if j-r/2 >=0 else 0
            # ur = i + r/2 if

            ii1 = i-r+1 if i-r+1>0 else 0
            ii2 = i+r-2 if i+r-2<n else n-1
            jj1 = j - r + 1 if j - r + 1 > 0 else 0
            jj2 = j + r - 2 if j + r - 2 < n else n - 1
            for x in range(-r, r):
                for y in range(-r, r):
                    ii = i + x
                    jj = j + y
                    if 0<=ii<n and 0<=jj<n:


    return answer


maps = [[1, 28, 41, 22, 25, 79, 4],
        [39, 20, 10, 17, 19, 18, 8],
        [21, 4, 13, 12, 9, 29, 19],
        [58, 1, 20, 5, 8, 16, 9],
        [5, 6, 15, 2, 39, 8, 29],
        [39, 7, 17, 5, 4, 49, 5],
        [74, 46, 8, 11, 25, 2, 11]]
p,r=19,	6	#17
print(solution(maps,p,r))