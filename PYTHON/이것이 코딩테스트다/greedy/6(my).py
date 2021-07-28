def solution(food_times, k):
    n = len(food_times)
    tmp = 0
    for i in range(k):
        if food_times[(i+tmp) % n] == 0:
            tmp += 1

        food_times[(i+tmp)%n] -= 1
        answer = ((i+tmp+1) % n) +1




    return answer

