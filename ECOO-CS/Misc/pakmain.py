ip = [int(input()),input().split()]
sort = []
score = 0
for i in range(len(ip[1])):
    ip[1][i] = int(ip[1][i])
checker = ip[1][:]
def addlast():
    sort.append(ip[1][-1])
    ip[1].pop()
def remlast():
    ip[1].insert(-1,sort[-1])
    sort.pop()
if ip[1][-1] != ip[0]:
    addlast()
    score += 1
while ip[1] != sorted(checker):
    if sort == [] and ip[1][-1] != ip[0] and ip[1][-1]+1 != ip[1][0] and ip[1][-1]-1 != ip[1][-2]:
        addlast()
        ip[1].insert(0,ip[1].pop())
        score += 1
    elif sort != []:
        if sort[-1]+1 < ip[1][-1] and ip[1][-1] != ip[0] and ip[1][-1]+1 != ip[1][0] and ip[1][-1]-1 != ip[1][-2]:
            addlast()
            ip[1].insert(0,ip[1].pop())
            score += 1
        elif sort[-1]+1 == ip[1][-1]:
            remlast()
            score += 1
        else:
            ip[1].insert(0,ip[1].pop())
    else:
        ip[1].insert(0,ip[1].pop())
    score += 1
    print(ip[1],sort)
