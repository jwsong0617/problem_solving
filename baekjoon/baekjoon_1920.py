M = input()
nums = list(map(int, input().split(' ')))
N = input()
checks = list(map(int, input().split(' ')))
nums_sorted = sorted(nums)
def binary_search(sorted_arr, x):
    l = 0
    r = len(sorted_arr)-1
    while(l<=r):
        m = int((l+r)/2)
        if(sorted_arr[m] == x):
            return 1
        elif(sorted_arr[m]>x):
            r=m-1
        else:
            l=m+1
    return 0
ans = (list(map(lambda x:str(binary_search(nums_sorted, x)),checks)))
for i in ans:
    print(i)