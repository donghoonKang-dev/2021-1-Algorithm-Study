N = int(input())
numbers = list(map(int, input().split()))
minimum = 0
maximum = 0

for i in range(N):
    if i == 0:
        minimum = numbers[i]
        continue
    else:
        if minimum > numbers[i]:
            minimum = numbers[i]
            continue

for j in range(N):
    if j == 0:
        maximum = numbers[j]
        continue
    else:
        if maximum < numbers[j]:
            maximum = numbers[j]
            continue

print(str(minimum) + ' ' + str(maximum))
