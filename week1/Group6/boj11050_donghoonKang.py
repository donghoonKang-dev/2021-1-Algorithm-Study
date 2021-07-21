def factorial(n):
    result = 1
    if n == 0:
        return result
    elif n == 1:
        return result
    else:
        for i in range(n, 0, -1):
            result = result * i
        return result


N, K = map(int, input().split())
NminusK = N - K
answer = factorial(N) / (factorial(K) * factorial(NminusK))
print(int(answer))
