import re
from collections import Counter
def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    bi1 = [str1[i:i+2] for i in range(len(str1)-1)]
    bi2 = [str2[i:i+2] for i in range(len(str2)-1)]
    bis = [bi1,bi2]
    new_bis = []
    
    # string preprocessing
    for bi in bis:
        print(bi)
        new_bi = []
        for i, elem in enumerate(bi):    
            p = re.compile(r'[^a-zA-Z]', re.IGNORECASE | re.UNICODE)        
            m = p.search(elem)
            # print('elem',elem)
            if m:    
                bi[i] = ''    
            else:
                new_bi.append(elem)
        new_bis.append(new_bi)
    # https://dbader.org/blog/sets-and-multiset-in-python
    # https://docs.python.org/2/library/collections.html
    # multi set

    multisets = []
    for new_bi in new_bis:
        multiset = Counter()
        for new_elem in new_bi:
            multiset.update({new_elem})
        multisets.append(multiset)
    if(sum(multisets[0].values()) == 0 and sum(multisets[1].values()) == 0):
        # print('both null set')
        jaccard = 1*65536
    else:
        intersection = multisets[0] & multisets[1]
        union = multisets[0] | multisets[1]
        jaccard = int((sum(intersection.values())/sum(union.values()))*65536)
    # print(jaccard)
    return jaccard