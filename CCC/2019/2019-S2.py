import math
tests = int(input())
ints = []
for i in range(tests):
    ints.append(int(input()))

def isPrime(num):
    for i in range(2,math.ceil(math.sqrt(num))+1):
        if num % i == 0:
            return False
    else:
        return True

for int in ints:
    num1 = int + 1
    num2 = int - 1
    while True:
        if isPrime(num1) and isPrime(num2):
            print(num1,num2)
            break
        else:
            num1 += 1
            num2 -= 1
