def manacher(s):
    A = []
    R = -1; p = -1
    for i in range(len(s)):
        if i <= R: A.append(min(A[2*p-i], R-i))
        else: A.append(0)
        while i-A[i]-1 >= 0 and i+A[i]+1 < len(s) and s[i-A[i]-1] == s[i+A[i]+1]: A[i]+= 1
        if i+A[i] > R: R = i+A[i]; p = i
    return A
s = ' '.join(input())
M = manacher(s)
maxr = 0
for i in range(len(M)):
    if i%2 == 0: cur = M[i]//2*2+1
    else: cur = (M[i]+1)//2*2
    maxr = max(maxr, cur)
print(maxr)