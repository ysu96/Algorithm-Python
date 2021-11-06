def solution(ings, menu, sell):
    answer = 0
    ingsDic = {}
    for ing in ings:
        name = ing[0]
        price = int(ing[2:])
        ingsDic[name] = price

    profit = {}
    for m in menu:
        name, ingredients, price = m.split()
        total = 0
        for ingredient in ingredients:
            total += ingsDic[ingredient]

        profit[name] = int(price) - total

    for s in sell:
        name, count = s.split()
        answer+= profit[name] * int(count)

    return answer

ings = ["x 25", "y 20", "z 1000"]
menu = ["AAAA xyxy 15", "TTT yy 30", "BBBB xx 30"]
sell = ["BBBB 3", "TTT 2"]
solution(ings,menu,sell)