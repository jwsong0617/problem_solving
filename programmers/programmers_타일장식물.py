def solution(N):
    memo = {1:1, 2:1}
    def fibonacci(n):
        if n == 0:
            return 0
        if n not in memo:
            memo[n] = fibonacci(n-1) + fibonacci(n-2)
        return memo[n]
    fibonacci(N)
    a=list(memo.values())

    def sol(n):
        if n == 0:
            return 4
        else:
            return sol(n-1)+a[n]*2    
    answer = sol(N-1)
    return answer
