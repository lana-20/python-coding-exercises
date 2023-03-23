# 5! = 5 * 4 * 3 * 2 * 1 = 120 -> descending order
# 5! = 5 * (5-1) * (5-2) * (5-3) * (5-4) = 120

def factorial(n):
    #  if n == 0 or n == 1:
    #     return 1
    # else:
    #     return n * factorial(n - 1)     # 5 * 4 * 3 * 2 * 1

    # Ternary Operator
    return 1 if (n == 0 or n == 1) else n * factorial(n-1)


n = 5
print("Factorial of", n, "is", factorial(n))

