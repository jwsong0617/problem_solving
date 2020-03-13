from collections import Counter
def solution(participant, completion):
    p_c = Counter(participant)
    c_c = Counter(completion)    
    answer = ''.join(list(p_c - c_c))
    return answer