i = [int(input()),int(input())]
init = i[0]
for s in range(i[1]):
    init = init*10
    i[0] += init
print(i[0])
