import sys
from itertools import permutations
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))
dd = {0:'+', 1:'-', 2:'*', 3:'/'}
oplist = []
for i in range(4):
    for _ in range(ops[i]):
        oplist.append(dd[i])


maxANS = -1e9
minANS = 1e9
cnd = set(permutations(oplist, n-1))
for cc in cnd:
    num = nums[0]
    for i in range(1,n):
        if  cc[i-1] == '/' and num <= 0 and nums[i] > 0:
            num = int(eval(str(num*-1) + cc[i - 1] + str(nums[i]))) * -1
        else:
            num = int(eval(str(num)+cc[i-1]+str(nums[i])))
    # print(num)
    maxANS = max(maxANS, num)
    minANS = min(minANS, num)

print(maxANS)
print(minANS)
print('-----------')
print(int(-4/-3))
print(int((4/-3)*-1))