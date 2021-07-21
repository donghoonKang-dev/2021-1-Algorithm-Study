def cantor(n):
    if n == 0:
        token = '-'
        return token
    result = ''
    result = result + cantor(n-1)
    for _ in range(3**(n-1)):
        result = result + ' '
    result = result + cantor(n-1)
    return result


while True:
    try:
        Nstring = input()
        if Nstring == '':
            break
        answer = cantor(int(Nstring))
        print(answer)
    except EOFError:
        break
