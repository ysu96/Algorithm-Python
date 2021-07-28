def solution(food_times, k):
    answer = 0
    sorted_food_times = sorted(food_times)

    # n_somthing means number of something
    n_remain_foods = len(food_times)
    accumulated_time = 0
    jump_time = 0
    period_time = 0

    for time in sorted_food_times:
        jump_time = time - period_time
        accumulated_time += jump_time * n_remain_foods
        if k < accumulated_time:
            accumulated_time -= jump_time * n_remain_foods
            break
        period_time = time
        n_remain_foods -= 1

    if n_remain_foods == 0:
        return -1
    k -= accumulated_time
    remain_iteration = k % n_remain_foods;

    # li = [i for i in range(1, len(food_times) + 1)]
    li = []
    for idx, value in enumerate(food_times):
        if value > period_time:
            li.append(idx + 1)

    answer = li[remain_iteration]

    return answer