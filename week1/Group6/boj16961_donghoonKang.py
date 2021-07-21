import sys

Taps = [0 for l in range(366)]
Spaces = [0 for m in range(366)]
Totals = [0 for n in range(366)]
maxStay = 0

N = int(sys.stdin.readline())
for _ in range(N):
    A, bB, cC = sys.stdin.readline().split()
    B = int(bB)
    C = int(cC)
    if A == "T":
        for i in range(B, C+1):
            Taps[i-1] = Taps[i-1] + 1
    else:
        for j in range(B, C+1):
            Spaces[j-1] = Spaces[j-1] + 1
    stay = C - B + 1
    if stay > maxStay:
        maxStay = stay

# question1
answer1 = 0
for a in range(366):
    if Taps[a] > 0 or Spaces[a] > 0:
        answer1 = answer1 + 1
print(answer1)

# question2
for b in range(366):
    Totals[b] = Taps[b] + Spaces[b]
answer2 = max(Totals)
print(answer2)

# question3
answer3 = 0
for c in range(366):
    if Taps[c] == 0 or Spaces[c] == 0:
        continue
    elif Taps[c] != Spaces[c]:
        continue
    else:
        answer3 = answer3 + 1
print(answer3)

# question4
answer4 = 0
for d in range(366):
    if Taps[d] == 0 or Spaces[d] == 0:
        continue
    elif Taps[d] == Spaces[d]:
        if answer4 < Totals[d]:
            answer4 = Totals[d]
    else:
        continue
print(answer4)

# question5
print(maxStay)
