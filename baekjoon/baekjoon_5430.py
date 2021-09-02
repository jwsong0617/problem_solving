T = int(input())
for _ in range(T):
    p = input()
    n = int(input())
    array = input()
    q = list(array[1:-1].split(','))
    reversed_flag = False
    l, r = 0, 0
    p = p.replace('RR','')    
    for f in p:
        if f == "R":
            reversed_flag = not reversed_flag
        elif f == "D":
            if reversed_flag:
                r+=1
            else:
                l+=1
    if l+r <= n:
        res = q[l:n-r]
        if reversed_flag:
            print('['+','.join(res[::-1])+']')
        else:
            print('['+','.join(res)+']')
    else:
        print('error')