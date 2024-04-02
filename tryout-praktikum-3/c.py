def answer():
    r, l, c = map(int, input().split())
    sumbuY = c-l

    if (r == 0 or sumbuY == 0):
        print("SUMBU")
        return

    if (sumbuY > 0):
        print("EMPAT")
        return
    if (sumbuY < 0):
        print("SATU")
        return


t = int(input())
for i in range(t):
    answer()
