import bisect
def binary_search_n(arr, x):
    i = bisect.bisect_left(arr, x)
    if(i < len(arr) and arr[i] == x):
        return bisect.bisect_right(arr,x) - bisect.bisect_left(arr, x)         
    else:
        return 0
N = input()
cards = list(map(int,input().split()))
M = input()
test_cards = list(map(int,input().split()))
cards.sort()
ans = list(map(lambda x: binary_search_n(cards, x),test_cards))
print(' '.join(str(e) for e in ans))