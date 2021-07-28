n,x = map(int,input().split())
array = list(map(int,input().split()))
count = 0
left_index = 0
right_index = 0
def binary_search_left(start,end,target):
    global left_index
    if start>end:
        return None
    mid = (start+end)//2
    if array[mid] > target:
        binary_search_left(start,mid-1,target)
    elif array[mid] < target:
        binary_search_left(mid+1,end,target)
    elif array[mid] == target:
        left_index = mid
        binary_search_left(start, mid - 1, target)

def binary_search_right(start,end,target):
    global right_index
    if start>end:
        return
    mid = (start+end)//2
    if array[mid] > target:
        binary_search_right(start,mid-1,target)
    elif array[mid] < target:
        binary_search_right(mid+1,end,target)
    elif array[mid] == target:
        right_index = mid
        binary_search_right(mid+1, end, target)

binary_search_left(0,n-1,x)
binary_search_right(0,n-1,x)
print(right_index-left_index+1)



