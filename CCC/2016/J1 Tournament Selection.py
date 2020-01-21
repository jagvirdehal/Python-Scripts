gameOutcome0 = input().upper()
gameOutcome1 = input().upper()
gameOutcome2 = input().upper()
gameOutcome3 = input().upper()
gameOutcome4 = input().upper()
gameOutcome5 = input().upper()
gameOutcome = str(''.join([gameOutcome0,gameOutcome1,gameOutcome2,gameOutcome3,gameOutcome4,gameOutcome5])).upper()
wins = 0
for w in gameOutcome:
    if w == 'W':
        wins+=1
if wins == 5:
    group = 1
elif wins == 6:
    group = 1
elif wins == 3:
    group = 2
elif wins == 4:
    group = 2
elif wins == 1:
    group = 3
elif wins == 2:
    group = 3
else:
    group = -1
print(group)
