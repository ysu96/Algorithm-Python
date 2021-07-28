import heapq

n = int(input())
count = 0
array = [1]

while 1:
    now = heapq.heappop(array)
    count += 1
    if count == n:
        print(now)
        break
    if now*2 not in array:
        heapq.heappush(array, now * 2)
    if now * 3 not in array:
        heapq.heappush(array, now * 3)
    if now * 5 not in array:
        heapq.heappush(array, now * 5)
