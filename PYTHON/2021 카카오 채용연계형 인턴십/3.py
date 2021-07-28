from bisect import bisect_left, bisect_right


def solution(n, k, cmd):
    data = dict()
    for i in range(n):
        data[i] = 'O'

    selected = k
    deleted = []
    #last index
    last = n-1
    for c in cmd:
        if c == 'C':
            deleted.append(selected) #삭제된 행 인덱스 추가
            data[selected] = 'X'

            if selected == last:
                # right_index = bisect_right(list(data.values()), 'O')
                # selected = right_index-1
                # last = selected

                while data[selected] == 'X':
                    selected -= 1
                last = selected
            else:

                while data[selected] == 'X':
                    selected += 1


        elif c == 'Z':
            popped = deleted.pop()
            if popped > last:
                last = popped
            data[popped] = 'O'


        else:
            dir, x = c.split()
            x = int(x)
            if dir == 'D':
                for i in range(x):
                    selected += 1

                    while data[selected] == 'X':
                        selected += 1
            else:
                for i in range(x):
                    selected -= 1
                    while data[selected] == 'X':
                        selected -= 1

    answer= ''.join(list(data.values()))
    return answer


n = 8
k = 2
cmd =["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
print(solution(n,k,cmd))
#"OOOOXOOO"
# 8	2	["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]	"OOXOXOOO"