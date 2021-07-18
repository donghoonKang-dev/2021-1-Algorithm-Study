import sys

arr = []
answer = []

N, M = map(int, sys.stdin.readline().split())
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

K = int(sys.stdin.readline())
for _ in range(K):
    numSum = 0
    i, j, x, y = map(lambda num: int(num)-1, sys.stdin.readline().split())
    for a in range(i, x+1):
        for b in range(j, y+1):
            numSum = numSum + arr[a][b]
    answer.append(numSum)

for k in range(K):
    print(answer[k])
