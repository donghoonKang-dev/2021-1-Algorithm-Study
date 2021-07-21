N = int(input())
result = 0

if N == 1:
    result = 5
else:
    n = N-1
    npow = n ** 2
    result = (5 + (3 * npow + 11 * n)//2) % 45678

print(result)
