def answer():
    b = int(input())
    n = int(input())
    p = int(input())

    harga = 25
    if (n == 1):
        harga = 100

    diskon = 0

    if (1 <= p <= 4):
        diskon = 0.1
    if (5 <= p <= 10):
        diskon = 0.15
    if (11 <= p <= 20):
        diskon = 0.2
    if (21 <= p <= 30):
        diskon = 0.25
    if (30 < p):
        diskon = 0.3

    kembalian = b - (harga*p*(1 - diskon))

    if (kembalian > 0):
        print("YA")
        # print(kembalian)
        print("{:.2f}".format(kembalian))
    else:
        print("TIDAK")
        # print(kembalian)
        print("{:.2f}".format(abs(kembalian)))


answer()
