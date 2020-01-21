i = int(input())
time = 1200
score = 0
while i >= 1440:
    score += 62
    i -= 1440
for s in range(i):
    time += 1
    if str(time).zfill(4)[2:] == '60':
        time += 40
    if str(time).zfill(4)[:2] == '13':
        time -= 1200
    time = str(time)
    if (int(time[0]) - int(time[1]) == int(time[1]) - int(time[2]) and len(time) == 3) or (int(time[0]) - int(time[1]) == int(time[1]) - int(time[2]) == int(time[2]) - int(time[3]) and len(time) == 4):
        score += 1
    time = int(time)
print(score)
