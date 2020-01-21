tests = int(input())
nums = []
primes = {2}

for i in range(tests):
    nums.append(int(input()))

def isPrime(num):
    if num in primes:
        return True

    for x in range(2,num):
        if num % x == 0:
            return False
    else:
        primes.add(num)
        return True

for i in nums:
    for j in range(i):
        num1 = i + j
        num2 = i - j
        if isPrime(num1) and isPrime(num2):
            print(str(num1) + ' ' + str(num2))
            break
