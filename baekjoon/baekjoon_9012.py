T = int(input())
for _ in range(T):
    arr = input()
    stk = []
    for e in arr:
        if len(stk) == 0 and e == ')':
            stk.append(e)
            break
        elif len(stk) != 0:
            if stk[-1] == '(' and e == ')':
                stk.pop()
                continue
        stk.append(e)
    if len(stk) != 0:
        print("NO")
    else:
        print("YES")