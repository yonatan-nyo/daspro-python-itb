def answer():
    n = int(input())
    hasil = n
    step = 1
    spot = 0
    first1 = 0

    while (n > 0):
        sisa = n % 2

        if (not sisa):
            spot = step
        if (not first1 and sisa):
            first1 = step
        step += 1

        n //= 2

    if (spot > first1):
        hasil = hasil + 2**(spot-1) - 2**(first1-1)

    # print(f"spot: {spot}")
    # print(f"first1: {first1}")

    print(hasil)


answer()
