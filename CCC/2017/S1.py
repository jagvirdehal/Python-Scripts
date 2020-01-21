input()
i = [input().split(),input().split()]
for x in range(len(i)):
    for w in range(len(i[x])):
        i[x][w] = int(i[x][w])
for s in range(len(i[0])):
    if sum(i[0][:s+1]) == sum(i[1][:s+1]):
        k = s+1
print(k)
