def answer():
    m = int(input())
    step = 0
    while (m > 0):
        sisa = m % 2
        if (sisa):
            step += 1
        m //= 2
    print(step)


answer()
