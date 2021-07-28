def factorial_recursive(n):
    if n <= 1: return 1
    return factorial_recursive(n-1) * n

def factorial_iterative(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

print("반복 : ",factorial_iterative(5))
print("재귀 : ",factorial_recursive(5))
