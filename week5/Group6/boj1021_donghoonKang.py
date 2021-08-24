N, M = map(int, input().split())
orders = list(map(int,input().split()))
mainList = [i for i in range(1, N+1)]

count = 0

for i in range(M):
  length = len(mainList)
  position = mainList.index(orders[i])

  if position < length - position:
    while True:
      if mainList[0] == orders[i]:
        del mainList[0]
        break
      else:
        mainList.append(mainList[0])
        del mainList[0]
        count += 1
  else:
    while True:
      if mainList[0] == orders[i]:
        del mainList[0]
        break
      else:
        mainList.insert(0, mainList[-1])
        del mainList[-1]
        count += 1

print(count)
