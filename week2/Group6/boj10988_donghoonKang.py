word = input()
length = len(word)
mid = length // 2
flag = True

for i in range(mid):
    if word[i] == word[length-i-1]:
        continue
    else:
        flag = False
        break

if flag == True:
    print(1)
else:
    print(0)
