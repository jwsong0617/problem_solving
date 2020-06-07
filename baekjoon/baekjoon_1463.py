N = int(input())
answers = [-1]*(N+1)
answers[1] = 0
for i in range(2, N+1):
    answers[i] = answers[i-1]+1
    if i % 2 == 0:
        answers[i] = min(answers[i], answers[int(i/2)]+1)
    if i % 3 == 0:
        answers[i] = min(answers[i], answers[int(i/3)]+1)
print(answers[N])