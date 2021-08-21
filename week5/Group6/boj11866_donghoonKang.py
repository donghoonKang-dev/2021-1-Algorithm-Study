from collections import deque

N, K = map(int, input().split())

answer = []

d = deque()
for i in range(1,N+1):
  d.append(i)

for j in range(N):
  for k in range(1,K+1):
    if k == K:
      t = d.popleft()
      answer.append(t)
    else:
      t = d.popleft()
      d.append(t)

print('<', end='')
for l in range(N):
  if l == N-1:
    print('%d'%(answer[l]), end='')
  else:
    print('%d, '%(answer[l]), end='')
print('>')