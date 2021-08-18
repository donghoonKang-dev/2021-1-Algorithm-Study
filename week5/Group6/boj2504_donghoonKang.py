inputString = list(input())
stack = []
result = 0

for token in inputString:
    if token == '(' or token == '[':
        stack.append(token)
        continue
    elif token == ')':
        num = 0
        while len(stack) != 0:
            tmp = stack.pop()
            if tmp == '(':
                if num == 0:
                    stack.append(2)
                else:
                    stack.append(2*num)
                break
            elif tmp == '[':
                print(0)
                exit(0)
            else:
                num = num + int(tmp)
    elif token == ']':
        num = 0
        while len(stack) != 0:
            tmp = stack.pop()
            if tmp == '[':
                if num == 0:
                    stack.append(3)
                else:
                    stack.append(3*num)
                break
            elif tmp == '(':
                print(0)
                exit(0)
            else:
                num = num + int(tmp)

for i in stack:
    if i == '(' or i == '[':
        print(0)
        exit(0)
    else:
        result += i

print(result)