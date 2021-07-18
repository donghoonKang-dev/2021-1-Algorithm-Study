import sys

numbers = []

N = int(sys.stdin.readline())
for _ in range(N):
    numbers.append(list(map(int, sys.stdin.readline().split())))

numbers.sort(key=lambda x: (x[0], x[1]))

for number in numbers:
    for item in number:
        print(item, end=' ')
    print()
