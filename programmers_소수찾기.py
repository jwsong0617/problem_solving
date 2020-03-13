
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
import itertools
def is_prime(n):
    if(n<2):
        return False
    if(n in (2,3)):
        return True
    if(n%2 is 0 or n%3 is 0):
        return False
    if n<9:
        return True
    k,l=5,n*0.5
    while(k<=l):
        if n%k is 0 or n%(k+2) is 0:
            return False
        k+=6
    return True

def solution(numbers):
    answer = set()
    numbers_lst = list(numbers)
    for r in range(1,len(numbers)+1):        
        all_permutes = [''.join(x) for x in itertools.permutations(numbers_lst,r)]
        all_permutes_int = [int(x) for x in all_permutes]
        all_permutes_int_set = set([str(x) for x in all_permutes_int])
        answer = answer.union(all_permutes_int_set)
    answer = [int(x) for x in answer]
    answer = sum([is_prime(x) for x in answer])
    return answer
