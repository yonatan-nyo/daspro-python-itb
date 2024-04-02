def printStars(n):
    out = ""
    for i in range(1, n):
        out += " "
    for i in range(n):
        out += "*"
    print(out)


def answer():
    n = int(input())
    for i in range(1, n+2):
        printStars(i)
    for i in range(n, 0, -1):
        printStars(i)


answer()
