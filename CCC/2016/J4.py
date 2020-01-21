startTime = input()
minute = startTime[-2:]
hour = startTime[:2]
speed = int(20)
distance = int(0)
hour = int(hour)
minute = int(minute)
while distance < 120:
    if minute == 60:
        minute = 0
        hour = hour+1
    if 7 <= hour <= 9:
        speed = 1
    elif 15 <= hour <= 18:
        speed = 1
    else:
        speed = 2
    minute = minute + 2
    distance = distance + speed
    if minute == 60:
        minute = 0
        hour = hour+1
    if hour >= 24:
        hour = hour-24
print(str(hour).zfill(2)+':'+str(minute).zfill(2))
