word = input()
answer = 0
chroatian_starting_c_candidates = ['c', 'd', 'l', 'n', 's', 'z']
chroatian_c_candidates = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
chroatian_temp_candidates = []
temp_count = 0
for c in word:
    if len(chroatian_temp_candidates) > 0:
        chroatian_temp_candidates.append(c)
        chroatian_temp = ''.join(chroatian_temp_candidates)
        if chroatian_temp == 'dz':
            temp_count += 1
            continue
        elif chroatian_temp in chroatian_c_candidates:
            answer += 1
            chroatian_temp_candidates = []
            temp_count = 0
        else:
            if c in chroatian_starting_c_candidates:
                answer += temp_count
                chroatian_temp_candidates = [c]
                temp_count = 1
            else:
                answer += temp_count+1
                chroatian_temp_candidates = []
                temp_count = 0
    elif c in chroatian_starting_c_candidates:
        chroatian_temp_candidates.append(c)
        temp_count += 1
    else:
        answer += 1
if len(chroatian_temp_candidates) > 0:
    answer += len(chroatian_temp_candidates)
print(answer)