def solution(phone_book):
    sorted_phone_book = sorted(phone_book, key=lambda x:len(x))
    length = len(sorted_phone_book)
    for i in range(length):
        prefix = sorted_phone_book[i]
        prefix_len = len(prefix)
        for j in range(i+1,length):
            if(prefix == sorted_phone_book[j][:prefix_len]):
                return False
    return True