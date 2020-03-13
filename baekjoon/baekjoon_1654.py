K, N = map(int, input().split(' '))
lan_cables = [int(input()) for k in range(K)]
def binary_search(arr, x):
    left = 1
    right = max(arr)
    while(left <= right):
        mid = int((left+right)/2)
        n = sum(map(lambda x: x//mid, lan_cables))
        if(n >= x):
            left = mid+1
        else:
            right = mid-1
    return right
print(binary_search(lan_cables, N))
