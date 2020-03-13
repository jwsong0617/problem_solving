def binary_search_manual(arr, x):
    left = 0
    right = len(arr)-1
    while(left<=right):
        mid = int((left + right)/2)
        if(arr[mid] == x):
            return 1
        elif(arr[mid]<=x):
            left = mid+1
        elif(arr[mid]>=x):
            right = mid-1
    return 0 
N = input()
cards = list(map(int,input().split()))
cards.sort()
M = input()
test_cards = list(map(int,input().split()))
ans = list(map(lambda x: binary_search_manual(cards,x), test_cards))
print(' '.join(str(e) for e in ans))
