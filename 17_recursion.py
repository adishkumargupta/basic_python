#call itself

#factorial
# 3! = 3*2*1 = 6
# 4! = 4*3*2*1=24

def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)

print(factorial(5)) # 120
