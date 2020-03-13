#-*- coding:utf-8 -*-
# baekjoon_10871
N, X = list(map(int, input().split(' ')))
nums = list(map(int, input().split(' ')))
print(nums)
results = []
for num in nums:
    if(num < X):
        results.append(str(num))
print(' '.join(results))