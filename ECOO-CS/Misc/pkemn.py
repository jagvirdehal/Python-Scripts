#740652
with open('DATA21.txt') as myfile:
    myfile = myfile.read().split("\n")
for wwwwwwwwww in range(10):
    ip = [myfile[0],myfile[1],myfile[2]] #Takes the first 3 lines of the data
    ip[1] = list(set(ip[1].split())) #Removes duplicates from the spinner, and splits each spinner number into a list
    ip[2] = ip[2].split() #Splits the results into a list
    for n in range(2): #Converts all items of all lists into integers
        for i in range(len(ip[n+1])):
            ip[n+1][i] = int(ip[n+1][i])

    def ww(result):
        for i in ip[1]: #Goes through every spinner number subtracting from the result
            result -= i
            for i2 in ip[1]: #Subtracts again
                result -= i2
                for i3 in ip[1]: #Checks if the result is equal to any of the options
                    if result == i3:
                        return "T"
                result += i2
            result += i
            
        for i in ip[1]:
            result -= i
            for i2 in ip[1]:
                if result % i2 == 0:
                    result //= i2
                    for i3 in ip[1]:
                        if result == i3:
                            return "T"
                    result *= i2
            result += i
            
        for i in ip[1]:
            if result % i == 0:
                result //= i
                for i2 in ip[1]:
                    result -= i2
                    for i3 in ip[1]:
                        if result == i3:
                            return "T"
                    result += i2
                result *= i
        
        for i in ip[1]:
            if result % i == 0:
                result //= i
                for i2 in ip[1]:
                    if result % i2 == 0:
                        result //= i2
                        for i3 in ip[1]:
                            if result == i3:
                                return "T"
                        result *= i2
                result *= i
        return "F"

    ans = []
    for i in ip[2]:
        ans.append(ww(i))
    print(''.join(ans))
    myfile.pop(0)
    myfile.pop(0)
    myfile.pop(0)
