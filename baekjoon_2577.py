from functools import reduce
from collections import Counter
numbers = []
init = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0,}
c = Counter(init)
for i in range(3):
    n = int(input())
    numbers.append(n)
mult = reduce(lambda x, y: x*y,numbers)
c.update(str(mult))
print(*c.values(), sep='\n')