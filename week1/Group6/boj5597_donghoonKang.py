students = []
noSubmit = []
for i in range(1, 31, 1):
    students.append(i)

for _ in range(28):
    tmp = int(input())
    if tmp in students:
        students.remove(tmp)
        continue

print(students[0])
print(students[1])
