def binary_search(array,target,start,end):
    mid = start+end//2
    if start > end:
        return None

    if array[mid] < target:
        return binary_search(array, target, mid+1, end)
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return mid

n, target = list(map(int,input().split()))
array = list(map(int,input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
    print("nonono")
else:
    print(result+1)

