def solution(x):
    answer = True
    # nx = list(map(int,str(x)))
    # total = sum(nx)
    # if(x% total != 0): answer=False
    # return answer
    return x%sum(list(map(int,str(x))))==0