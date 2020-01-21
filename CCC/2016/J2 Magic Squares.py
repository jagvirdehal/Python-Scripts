notMagic = 0
w = 0
row1 = input().split()
row2 = input().split()
row3 = input().split()
row4 = input().split()
def addrow(list):
    s = int(list[0])+int(list[1])+int(list[2])+int(list[3])
    return s
def addcolumn(x):
    s = int(row1[x])+int(row2[x])+int(row3[x])+int(row4[x])
    return s
base = addrow(row1)
if addrow(row2) == base:
    w+=0
else:
    notMagic = 1
if addrow(row3) == base:
    w+=0
else:
    notMagic = 1
if addrow(row4) == base:
    w+=0
else:
    notMagic = 1
for i in range(0,4):
    if addcolumn(i) == base:
        w+=0
    else:
        notMagic = 1
    i+=1
if notMagic == 1:
    print('not magic')
else:
    print('magic')
