import sys

numbers = []
N = int(sys.stdin.readline())
for _ in range(N):
    numbers.append(int(sys.stdin.readline()))
numbers.sort(reverse=True)
for i in range(N):
    print(numbers[i])
