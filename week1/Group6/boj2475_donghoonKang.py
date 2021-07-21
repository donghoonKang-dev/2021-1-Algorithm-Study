numbers = list(map(int, input().split()))
one = numbers[0] ** 2
two = numbers[1] ** 2
three = numbers[2] ** 2
four = numbers[3] ** 2
five = numbers[4] ** 2
checkSum = (one + two + three + four + five) % 10
print(checkSum)
