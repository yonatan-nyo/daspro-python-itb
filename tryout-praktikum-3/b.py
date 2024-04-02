def factorial(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res


def productNumber(n):
    if (n//10 <= 0):
        return n
    return (n % 10) * productNumber(n//10)


def factoriaLOL(n):
    fact = factorial(n)
    return productNumber(fact)


def answer():
    n = int(input())
    # fact = factorial(n)
    # print(f"fact: {fact}")
    # print(f"productNumber: {productNumber(fact)}")
    if (n >= 5):
        print(0)
        return

    print(factoriaLOL(n))


answer()
