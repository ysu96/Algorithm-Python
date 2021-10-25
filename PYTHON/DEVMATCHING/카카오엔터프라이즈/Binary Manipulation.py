def solution(n):
    arr = list(map(int,bin(n)[2:]))
    print(arr)
    cnt = 0
    l = len(arr)

    while arr.count(0) != l:

        arr[-1] = 0 if arr[-1]==1 else 1
        cnt+=1
        print(arr)
        if arr.count(0) == l: return cnt

        for i in range(l-2, -1, -1):
            if arr[i+1] == 1 and (i == l-2 or arr[i+2:].count(1) == 0):
                arr[i] = 0 if arr[i]==1 else 1
                cnt+=1
                break

        print(arr)
    return cnt

print(solution(11))