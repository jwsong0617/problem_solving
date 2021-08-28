from collections import Counter


word = input()
word = word.lower()
c = Counter(word)
commons = c.most_common(2)
if len(commons) == 1:
    print(commons[0][0].capitalize())
else:
    if commons[0][1] == commons[1][1]:
        print("?")
    else:
        print(commons[0][0].capitalize())