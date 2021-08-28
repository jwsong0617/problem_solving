import sys


answer = 0
N = int(input())
for i in range(N):
    last_word = ''
    word_dict = {}
    word = input()
    for c in word:
        if c not in list(word_dict.keys()):
            word_dict[c] = 1
            if word_dict.get(last_word) is not None:
                word_dict[last_word] = -1
        else:
            if word_dict[c] == -1:
                word_dict[c] = 0
                break
            elif c != last_word:
                word_dict[last_word] = -1
        last_word = c
    if 0 not in word_dict.values():
        answer += 1
print(answer)