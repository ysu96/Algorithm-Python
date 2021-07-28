from bisect import bisect_left,bisect_right

def count_by_range(array,left_value,right_value):
    left = bisect_left(array,0,len(array),left_value)
    right = bisect_right(array,0,len(array),right_value)
    return right-left

array=[[] for _ in range(10001)]
reversed_array = [[] for _ in range(10001)]

def solution(words, queries):
    answer = []
    for word in words:
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1])

    for i in range(10001):
        array[i].sort()
        reversed_array[i].sort()

    for q in queries:
        if q[0] != '?':
            res = count_by_range(array[len(q)], q.replace('?', 'a'), q.replace('?','z'))
        else:
            res = count_by_range(reversed_array[len(q)], q[::-1].replace('?','a'), q[::-1].replace('?','z'))
        answer.append(res)


    return answer