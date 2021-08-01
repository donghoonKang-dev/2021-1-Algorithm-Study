import sys
sys.setrecursionlimit(10**9)
N = int(sys.stdin.readline())
paper = []
for _ in range(N):
    paper.append(list(map(int, sys.stdin.readline().split())))
minusCount, zeroCount, plusCount = 0, 0, 0


def cuttingPaper(i, j, n):
    startNum = paper[i][j]
    flag = False
    if n != 1:
        for x in range(i, i+n):
            for y in range(j, j+n):
                if paper[x][y] != startNum:
                    flag = True
                    break
            if flag:
                break
    if flag:
        newN = n // 3
        for a in range(0, 3):
            for b in range(0, 3):
                cuttingPaper(i+a*newN, j+b*newN, newN)
    else:
        if startNum == -1:
            global minusCount
            minusCount = minusCount + 1
        elif startNum == 0:
            global zeroCount
            zeroCount = zeroCount + 1
        else:
            global plusCount
            plusCount = plusCount + 1


cuttingPaper(0, 0, N)

print(minusCount)
print(zeroCount)
print(plusCount)
