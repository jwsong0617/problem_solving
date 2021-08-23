import sys
ws = [[[0]*50 for _ in range(50)] for _ in range(50)]


def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    elif a < b < c:
        if ws[a][b][c-1]:
            x = ws[a][b][c-1]
        else:
            x = w(a, b, c-1)
            ws[a][b][c - 1] = x
        if ws[a][b-1][c-1]:
            y = ws[a][b-1][c-1]
        else:
            y = w(a, b-1, c-1)
            ws[a][b - 1][c - 1] = y
        if ws[a][b-1][c]:
            z = ws[a][b-1][c]
        else:
            z = w(a, b - 1, c)
            ws[a][b - 1][c] = z
        return x + y - z
        # return w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        if ws[a-1][b][c]:
            v = ws[a-1][b][c]
        else:
            v = w(a-1, b, c)
            ws[a - 1][b][c] = v
        if ws[a-1][b-1][c]:
            x = ws[a-1][b-1][c]
        else:
            x = w(a-1, b-1, c)
            ws[a - 1][b - 1][c] = x
        if ws[a-1][b][c-1]:
            y = ws[a-1][b][c-1]
        else:
            y = w(a-1, b, c-1)
            ws[a - 1][b][c - 1] = y
        if ws[a-1][b-1][c-1]:
            z = ws[a-1][b-1][c-1]
        else:
            z = w(a-1, b-1, c-1)
            ws[a - 1][b - 1][c - 1] = z
        return v + x + y - z
        # return w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)


while True:
    _a, _b, _c = map(int, sys.stdin.readline().strip().split())
    if _a == -1 and _b == -1 and _c == -1:
        break
    else:
        value = w(_a, _b, _c)
        print('w('+str(_a)+', '+str(_b)+', '+str(_c)+') = '+str(value))
