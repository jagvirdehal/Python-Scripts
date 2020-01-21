while True:
    inp = [int(input()),input().split()]
    sort = []
    score = 0
    for i in range(len(inp[1])):
        inp[1][i] = int(inp[1][i])
    checker = sorted(inp[1][:])
    for i in range(-inp[0]+1,0):
        i = abs(i)
        if inp[1].index(i) > inp[1].index(i+1):
            score += inp[1].index(i)
            inp[1].pop(inp[1].index(i))
            inp[1].insert(0,i)
        if inp[1] == checker:
            break
    print(score)
