i = [input(),input(),input()]
car = [int(i[0].split(' ')[0]),int(i[0].split(' ')[1])]
dest = [int(i[1].split(' ')[0]),int(i[1].split(' ')[1])]
batt = int(i[2])
for i in range(batt):
    if car[0] > dest[0]:
        car[0] -= 1
    elif car[0] < dest[0]:
        car[0] += 1
    elif car[1] > dest[1]:
        car[1] -= 1
    elif car[1] < dest[1]:
        car[1] += 1
    else:
        car[0] += 1
if car == dest:
    print('Y')
else:
    print('N')
