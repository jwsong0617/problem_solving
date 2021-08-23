import sys
N = int(sys.stdin.readline().strip())
people = [0]*N
for i in range(N):
    people[i] = list(map(int, sys.stdin.readline().strip().split()))
    people[i].append(i)
answers = []
for i in range(N):
    rank = 1
    for j in range(N):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            rank += 1
    answers.append(rank)
print(*answers)
