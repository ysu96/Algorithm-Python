def solution(n, arr1, arr2):
    answer = ['' for _ in range(n)]
    for i in range(n):
        print(str(bin(arr1[i]|arr2[i]))[2:])
        a1 = format(arr1[i], 'b')
        a2 = format(arr2[i], 'b')

        arr1[i] = list('0'*(n-len(a1)) + a1)
        arr2[i] = list('0'*(n-len(a2)) + a2)

    for i in range(n):
        for j in range(n):
            if arr1[i][j] == '1' or arr2[i][j] == '1':
                answer[i] += '#'
            else:
                answer[i] += ' '


    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))