def solution(w,h):

    gcd = UC(w,h)
    answer = w*h - (w+h-gcd)

    return answer

def UC(x,y):
    while(y):
        x,y = y,x%y
    return x

print(solution(8, 12))