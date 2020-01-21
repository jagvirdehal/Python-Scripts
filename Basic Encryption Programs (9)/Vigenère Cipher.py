while True:
    question = input('''Would you like to CODE or DECODE? (C/D)
''')
    if question.upper()[0] == 'C':
        cipher = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        message = str(input('''Enter the message:
''')).upper().replace(' ','')
        key = str(input('''Enter the key you would like to use:
''') * len(message)).upper().replace(' ','')[:len(message)]
        codeChar = list(message)
        for char in range(0,len(message)):    
            if cipher.find(key[char]) + cipher.find(message[char]) <= 25:
                codeChar[char] = str(cipher[cipher.find(key[char]) + cipher.find(message[char])])
            else:
                codeChar[char] = str(cipher[cipher.find(key[char]) + cipher.find(message[char]) - 26])
        code = ''.join(codeChar)
        print(code)
        input('Press Enter to Continue')

    elif question.upper()[0] == 'D':
        cipher = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        code = str(input('''Enter the code:
''')).upper().replace(' ','')
        key = str(input('''Enter the cipher key:
''') * len(code)).upper().replace(' ','')[:len(code)]
        messageChar = list(code)
        for char in range(0,len(code)):
            if cipher.find(code[char]) - cipher.find(key[char]) >= -1:
                messageChar[char] = str(cipher[cipher.find(code[char]) - cipher.find(key[char])])
            else:
                messageChar[char] = str(cipher[cipher.find(code[char]) - cipher.find(key[char]) + 26])
        message = ''.join(messageChar)
        print(message)
        input('Press Enter to Continue')
