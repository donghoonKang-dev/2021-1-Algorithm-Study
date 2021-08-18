##입력받기
N = int(input())
postfixString = input()
operands = [0] * N
for i in range(N):
  operands[i] = int(input())

##스택준비
stack = []

for k in postfixString:
  if 'A' <= k <= 'Z':
    stack.append(operands[ord(k)-ord('A')])
  else:
    b = stack.pop()
    a = stack.pop()
    if k == '*':
      stack.append(a * b)
    elif k == '/':
      stack.append(a / b)
    elif k == '+':
      stack.append(a + b)
    elif k == '-':
      stack.append(a - b)

answer = stack[0]
print('%.2f'%answer)