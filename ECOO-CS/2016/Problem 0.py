line = 0
test = 0
with open ("DATA01.txt", "r") as data:
    soup = data.read()
ssplit = soup.lower().replace('a','1 ').replace('b','2 ').replace('c','3 ').replace('d','4 ').replace('e','5 ').replace('f','6 ').replace('g','7 ').replace('h','8 ').replace('i','9 ').replace('j','10 ').replace('k','11 ').replace('l','12 ').replace('m','13 ').replace('n','14 ').replace('o','15 ').replace('p','16 ').replace('q','17 ').replace('r','18 ').replace('s','19 ').replace('t','20 ').replace('u','21 ').replace('v','22 ').replace('w','23 ').replace('x','24 ').replace('y','25 ').replace('z','26 ').splitlines()
nsoup = ssplit
supsplit = soup.lower().replace('a','1 ').replace('b','2 ').replace('c','3 ').replace('d','4 ').replace('e','5 ').replace('f','6 ').replace('g','7 ').replace('h','8 ').replace('i','9 ').replace('j','10 ').replace('k','11 ').replace('l','12 ').replace('m','13 ').replace('n','14 ').replace('o','15 ').replace('p','16 ').replace('q','17 ').replace('r','18 ').replace('s','19 ').replace('t','20 ').replace('u','21 ').replace('v','22 ').replace('w','23 ').replace('x','24 ').replace('y','25 ').replace('z','26 ').split()
print(nsoup)
for s in range(0,5):
    test = 0
    for i in range(0,int(nsoup[line])):
        #print(int(nsoup[line+1].split()[i]),int(nsoup[line+1].split()[i-1]))
        if int(nsoup[line+1].split()[i]) >= int(nsoup[line+1].split()[i-1]):
            test+=1
    if test+1 == int(nsoup[line]):
        print(int(nsoup[line]),'IN ORDER')
    else:
        print(int(nsoup[line]),'NOT IN ORDER')
    line+=2
input()
