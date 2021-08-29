from collections import Counter

a = Counter(input())
b = Counter(input())
for key in b.keys():
    if a.get(key) is not None:
        a[key] = a.get(key)-b.get(key)
    else:
        a[key] = -b.get(key)
# print(a)
print(sum(map(abs, filter(lambda x: x != 0, a.values()))))