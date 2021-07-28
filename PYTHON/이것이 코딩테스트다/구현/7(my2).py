n = input()
left = n[:len(n)//2]
right = n[len(n)//2:]
left_sum = 0
right_sum = 0
for i in left:
    left_sum += int(i)
for i in right:
    right_sum += int(i)

if right_sum == left_sum:
    print("LUCKY")
else:
    print("READY")
