plane = [
    input().split(),
    input().split(),
    input().split()
]

global unk, kno, col, row

unk = []
kno = []
col = [[],[],[]]
row = [[],[],[]]


def grid(tup):
    return plane[tup[0],tup[1]]

def refresh():
    global unk, kno, col, row
    unk = []
    kno = []
    col = [[], [], []]
    row = [[], [], []]
    for x in range(3):
        for y in range(3):
            loc = plane[x][y]
            pos = (x,y)
            if loc == 'X':
                unk.append(pos)
            else:
                kno.append(pos)
                row[x].append(pos)
                col[y].append(pos)
                plane[pos[0]][pos[1]] = int(plane[pos[0]][pos[1]])

refresh()

while unk:
    found = 0
    for i in unk:
        unkRow = i[0]
        unkCol = i[1]
        numRow = len(row[unkRow])
        numCol = len(col[unkCol])
        if numRow == 2:
            if unkCol == 0:
                plane[unkRow][unkCol] = plane[unkRow][1] - (plane[unkRow][2] - plane[unkRow][1])
                refresh()
                found += 1
            elif unkCol == 1:
                plane[unkRow][unkCol] = (plane[unkRow][2] + plane[unkRow][0]) / 2
                refresh()
                found += 1
            elif unkCol == 2:
                plane[unkRow][unkCol] = plane[unkRow][1] + (plane[unkRow][1] - plane[unkRow][0])
                refresh()
                found += 1
        elif numCol == 2:
            if unkRow == 0:
                plane[unkRow][unkCol] = plane[1][unkCol] - (plane[2][unkCol] - plane[1][unkCol])
                refresh()
                found += 1
            elif unkRow == 1:
                plane[unkRow][unkCol] = (plane[2][unkCol] + plane[0][unkCol]) / 2
                refresh()
                found += 1
            elif unkRow == 2:
                plane[unkRow][unkCol] = plane[1][unkCol] + (plane[1][unkCol] - plane[0][unkCol])
                refresh()
                found += 1
    if found == 0:
        i = unk[0]
        unkRow = i[0]
        unkCol = i[1]
        numRow = len(row[unkRow])
        numCol = len(col[unkCol])
        break

for i in range(3):
    for j in range(3):
        plane[i][j] = str(plane[i][j])

print(' '.join(plane[0]))
print(' '.join(plane[1]))
print(' '.join(plane[2]))

'''
8 9 10
16 X 20
24 X 30
'''

'''
14 X X
X X 18
X 16 X
'''