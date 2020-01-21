binary = input()
binary = binary[:8]
binary = int()
i = 0
while i in range(0,8):
    binary[i] = binary[i]**(i+1)
    i += 1
print(''.join(binary))
