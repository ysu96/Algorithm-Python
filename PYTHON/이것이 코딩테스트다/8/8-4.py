d = [0]*100

def fibo(x):
    d[0] = 1
    d[1] = 1
    for i in range(2,x):
        d[i] = d[i-1] + d[i-2]
    return d[x-1]

print(fibo(6))