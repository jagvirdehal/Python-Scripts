while True:
    vts = 0
    dv = 0
    nw = input().split()
    nw[0] = int(nw[0])
    nw[1] = int(nw[1])
    inp = []
    for i in range(100):
        inp.append(input().split())
        inp[-1][0] = int(inp[-1][0])
        inp[-1][1] = int(inp[-1][1])
    points = []
    for x in range(nw[0]-60,nw[0]+60):
        for y in range(nw[1]-60,nw[1]+60):
            if ((x-nw[0])**2+(y-nw[1])**2) <= 2500:
                points.append([x,y])

    for i in points:
        dist = []
        for w in inp:
            if i[0:2] == w[0:2]:
                points.remove(i)
                break
            dist.append([((i[0]-w[0])**2 + (i[1]-w[1])**2),w[2]])
        else:
            dist = sorted(dist)
            ndst = []
            for i in range(3):
                ndst.append(dist[0])
                dist.pop(0)
            for i in dist:
                if dist[0][0] == ndst[-1][0]:
                    ndst.append(dist[0])
                    dist.pop(0)
                else:
                    break
            dvote = 0
            for i in ndst:
                if i[1] == 'R':
                    dvote -= 1
                elif i[1] == 'D':
                    dvote += 1
            if dvote >= 0:
                dv += 1
            vts += 1
            continue
    print("{0:.1f}".format(dv/vts*100))
