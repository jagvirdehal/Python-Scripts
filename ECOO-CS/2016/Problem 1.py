line = 0
with open ("DATA11.txt", "r") as data:
    marks = data.read()
msplit = marks.splitlines()
line = 0
for s in range(0,10):
    w = msplit[line].split()
    line+=1
    for i in range(0,int(msplit[line])):
        line+=1
        if i == 0:
            classgrade = 0
        gradetest = msplit[line].split()
        mark = int(gradetest[0]) * int(w[0]) + int(gradetest[1]) * int(w[1]) + int(gradetest[2]) * int(w[2]) + int(gradetest[3]) * int(w[3])
        if mark/100 >= 50:
            classgrade+=1
    print(classgrade)
    line+=1
##weight = msplit[line].split()
##line+=1
##for i in range(0,int(msplit[line])):
##    line+=1
##    if i == 0:
##        classgrade = 0
##    gradetest = msplit[line].split()
##    mark = int(gradetest[0]) * int(weight[0]) + int(gradetest[1]) * int(weight[1]) + int(gradetest[2]) * int(weight[2]) + int(gradetest[3]) * int(weight[3])
##    if mark/100 >= 50:
##        classgrade+=1
##print(classgrade)
input()
