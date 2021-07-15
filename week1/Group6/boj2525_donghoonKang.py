A, B = map(int, input().split())
C = int(input())

hour = A
minute = B+C

if hour < 24 and minute <= 59:
    print(str(hour) + ' ' + str(minute))
else:
    upHour = minute // 60
    hour = (A + upHour) % 24
    minute = minute % 60
    print(str(hour) + ' ' + str(minute))
