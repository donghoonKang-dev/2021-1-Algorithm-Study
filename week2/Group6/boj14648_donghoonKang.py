import sys


def mySum(myList, x, y):
    numSum = 0
    for i in range(x, y+1):
        numSum = numSum + myList[i]
    return numSum


n, q = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

for _ in range(q):
    query = list(map(int, sys.stdin.readline().split()))
    if query[0] == 1:
        a = query[1]-1
        b = query[2]-1
        thisSum = mySum(numbers, a, b)
        print(thisSum)
        numbers[a], numbers[b] = numbers[b], numbers[a]
        continue
    else:
        a = query[1]-1
        b = query[2]-1
        c = query[3]-1
        d = query[4]-1
        abSum = mySum(numbers, a, b)
        cdSum = mySum(numbers, c, d)
        thisSum = abSum - cdSum
        print(thisSum)
        continue
