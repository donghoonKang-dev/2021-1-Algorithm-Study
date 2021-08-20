from collections import deque

def printerQueue():
  N, M = map(int, input().split())
  queueList = list(map(int, input().split()))
  q = deque(queueList)

  printedCount = 0

  while len(q) > 0:
    thisMaxPriority = max(q)

    token = q.popleft()
    M = M - 1
    
    if token == thisMaxPriority:
      printedCount = printedCount + 1
      if M == -1:
        break
      else:
        M - 1
    else:
      if M < 0:
        M = len(q)
      q.append(token)

  print(printedCount)

T = int(input())

for _ in range(T):
  printerQueue()