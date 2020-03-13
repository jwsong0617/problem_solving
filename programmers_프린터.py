def solution(priorities, location):
    prior_q = []
    loc_q = []
    print_q = []    
    for i, elem in enumerate(priorities):
        prior_q += [elem]
        loc_q += [i]    
    while(prior_q):
        first_elem = prior_q[0]
        first_elem_loc = loc_q[0]
        if(first_elem != max(prior_q)):
            # print('\nfirst_elem != max(prior_q)')
            prior_q.pop(0)
            loc_q.pop(0)
            prior_q += [first_elem]
            loc_q += [first_elem_loc]
        else:
            # print('\nelse')
            prior_q.pop(0)
            loc_q.pop(0)
            print_q += [first_elem_loc]
    answer = print_q.index(location)+1
    return answer
