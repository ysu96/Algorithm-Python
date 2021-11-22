from itertools import combinations
def countSubstrings(input_str):
    # Write your code here
    alphaDict = {'a':1, 'b':1,
                 'c':2, 'd':2, 'e':2,
                 'f':3, 'g':3, 'h':3,
                 'i':4,'j':4,'k':4,
                 'l':5,'m':5,'n':5,
                 'o':6,'p':6,'q':6,
                 'r':7,'s':7,'t':7,
                 'u':8,'v':8,'w':8,
                 'x':9,'y':9,'z':9}
    answer = 0
fsdfdsfvvvvv

    for i in range(len(input_str)):
        for j in range(0,len(input_str)-i):
            # print(input_str[j:j+i+1])
            new_str = input_str[j:j+i+1]

            length = len(new_str)
            # total = sum(list(map(int, new_str)))
            total = 0
            # print(total)
            for k in range(length):
                total += alphaDict[new_str[k]]

            if total%length == 0:
                answer += 1
    print(answer)
    return answer
input_str = "bef"
countSubstrings(input_str)