n, m = map(int,input().split())
data = list(map(int,input().split()))

data.sort()

def binary_search(array, target, start, end):
    if start > end: return None
    mid = (start+end)//2
    print(mid)
    tmp = 0
    for i in range(len(array)):
        if array[i] - mid > 0:
            tmp += array[i] - mid

    if target < tmp:
        return binary_search(array, target, mid+1, end)
    elif target > tmp:
        return binary_search(array, target, start, mid-1)
    else:
        return mid

result = binary_search(data, m, 0, data[-1])
print(result)
