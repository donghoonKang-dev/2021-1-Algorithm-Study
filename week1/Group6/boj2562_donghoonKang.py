numbers = [int(input()) for _ in range(9)]
maximum = 0
index = 1

for j in range(9):
    if j == 0:
        maximum = numbers[j]
        continue
    else:
        if maximum < numbers[j]:
            maximum = numbers[j]
            index = j + 1
            continue

print(maximum)
print(index)
