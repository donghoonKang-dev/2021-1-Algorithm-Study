import sys
arr = []
N = int(sys.stdin.readline())
for _ in range(N):
    arr.append(sys.stdin.readline())


def quadTree(x, y, size):
    if size == 1:
        return str(arr[x][y])
    else:
        result = []
        for i in range(x, x+size):
            for j in range(y, y+size):
                if arr[i][j] != arr[x][y]:
                    nextSize = size // 2
                    result.append('(')
                    result.extend(quadTree(x, y, nextSize))
                    result.extend(quadTree(x, y+nextSize, nextSize))
                    result.extend(quadTree(x+nextSize, y, nextSize))
                    result.extend(quadTree(x+nextSize, y+nextSize, nextSize))
                    result.append(')')
                    return result
    return str(arr[x][y])


print(''.join(quadTree(0, 0, N)))
