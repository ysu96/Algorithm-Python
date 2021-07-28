def solution(brown, yellow):
    a = (brown-4)//2
    for i in range(1,a):
        x = i
        y = a-i
        if x*y == yellow:
            x = x+2
            y = y+2
            if x>y:
                return [x,y]
            else:
                return [y,x]