import sys
from operator import itemgetter

N = int(sys.stdin.readline().strip())
schedules = []
for i in range(N):
    s, e = map(int, sys.stdin.readline().strip().split())
    schedules.append([s, e])
cur_time = 0
cnt = 0
for schedule in sorted(schedules, key=itemgetter(1, 0)):
    if schedule[0] < cur_time:
        continue
    else:
        cnt += 1
        cur_time = schedule[1]
print(cnt)