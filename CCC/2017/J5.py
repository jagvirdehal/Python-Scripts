from collections import Counter
input()
i2 = input().split(' ')
poss = []
score = 0
for i in range(len(i2)):
    init = i2.pop()
    for i in i2:
        poss.append(str(int(init) + int(i)))
for i in range(len(Counter(poss).most_common())):
    score += 1
    if i+1 == len(Counter(poss).most_common()):
        break
    if Counter(poss).most_common()[i][1] != Counter(poss).most_common()[i+1][1]:
        break
print(Counter(poss).most_common()[0][1],score)
