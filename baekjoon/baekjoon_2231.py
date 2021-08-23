import sys
N = sys.stdin.readline().strip()
answer = -1
N_len = len(N)
N_int = int(N)
delta = 9*N_len
if (N_int - delta) < 0:
    start = 0
else:
    start = N_int - delta
start_str = str(start)
for i in range(start, N_int):
    total = 0
    for j in range(len(str(i))):
        total += int(str(i)[j])
    total += i
    if total == N_int:
        answer = i
        break
print(max(answer, 0))
