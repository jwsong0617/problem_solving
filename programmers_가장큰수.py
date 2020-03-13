import functools
def solution(numbers):
    answer = ''
    numbers_str = [str(number) for number in numbers]
    answer = ''.join(sorted(numbers_str,key=functools.cmp_to_key(lambda x,y:int(x+y)-int(y+x)),reverse=True))
    if(int(answer)==0):
        answer = '0'
    return answer