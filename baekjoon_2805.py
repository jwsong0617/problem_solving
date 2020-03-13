woods = []
N, M = list(map(int,input().split()))
woods = list(map(int,input().split()))
def binary_search(arr, need_amount):
    left = 0
    right = max(arr)
    while(left<=right):        
        mid = int((left+right)/2)
#         print('mid:',mid)
        woods_cut_total = sum(map(lambda x:x-mid if x>mid else 0,arr))
        if(woods_cut_total < need_amount):  # 너무 적게 얻음 더 잘라야함
            right = mid-1
        else:  # 너무 많이 얻음 덜 잘라야함
            left = mid+1
    return right
print(binary_search(woods, M))