# Sol1
from itertools import permutations
import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
number_range = list(range(1, N+1))
answer = list(permutations(number_range, M))
for a in answer:
    a = list(map(str, a))
    b = ' '.join(a)
    print(b)

# Sol2
import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
num_range = list(range(1, N+1))
def f(arr, used, k):
    if(k==M):
        answer = list(map(str, arr))
        print(' '.join(answer))
        return
    for i in num_range:
        if(used[i-1] == 0):
            arr[k] = i
            used[i-1] = 1
            f(arr, used, k+1)
            used[i-1] = 0
used_raw = [0]*N
arr_raw = [0]*M
f(arr_raw, used_raw, 0)
