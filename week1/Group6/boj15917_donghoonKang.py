import sys

Q = int(sys.stdin.readline())
qList = []
answerList = []

for _ in range(Q):
    q = int(sys.stdin.readline())
    qList.append(q)

for i in range(Q):
    tmp = qList[i]
    if (tmp & (-tmp)) == tmp:
        answerList.append(1)
    else:
        answerList.append(0)

for j in range(Q):
    print(answerList[j])
