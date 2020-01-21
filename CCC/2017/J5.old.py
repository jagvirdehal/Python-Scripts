#i1 = int(input())
i2 = input().split(' ')
it = i2[:]
score = 0
score2 = 0
poss = []
for i in range(len(i2)):
    init = i2.pop()
    for i in i2:
        poss += str(int(init) + int(i))
poss2 = ''.join(poss)
poss3 = []
for i in poss:
    poss3 += i,str(poss2.count(i))
    for n in range(poss2.count(i)):
        poss.remove(i)
#print(str(len(it)/2))
n1 = set()
for w in list(''.join(poss3)[1::2]):
    n1.add(int(w))
print(poss3)
print(max(n1))
if ''.join(poss3)[1::2].find(str(max(n1))) != -1:
    print(''.join(poss3)[::2][''.join(poss3)[1::2].find(str(max(n1)))])
    poss3.remove(''.join(poss3)[::2][''.join(poss3)[1::2].find(str(int(len(it)/2)))])
    poss3.remove((str(int(len(it)/2))))
##for i in poss2:
##    posst = poss2[:]
##    posst.remove(i)
##    if i in posst:
##        score2 += 1
##    else:
##        poss2.remove(i)
##print(score2)
