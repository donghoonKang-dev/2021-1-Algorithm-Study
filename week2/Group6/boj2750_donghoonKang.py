numbers = []
N = int(input())
for _ in range(N):
    numbers.append(int(input()))
numbers.sort()
for i in range(N):
    print(numbers[i])
