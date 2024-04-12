# funxtion that calls itself
# best example can be factorial
def factorial(num):
    fact = None
    if num == 0 or num == 1:
        return 1
    else:
        fact = num * factorial(num - 1)
    
    return fact


facto = factorial(5)
print(f"{facto}")
