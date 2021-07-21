def combination(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in combination(arr[i+1:], r-1):
                yield [arr[i]] + next


while True:
    inputList = list(map(int, input().split()))
    k = inputList[0]
    if k == 0:
        break
    numberList = inputList[1:]

    for combi in combination(numberList, 6):
        print(' '.join(map(str, combi)))
    print()
