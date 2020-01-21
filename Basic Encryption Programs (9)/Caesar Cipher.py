def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)
while True:
    question = input('''(C/D)?
''')
    if question.lower() == 'd':
        theMessage = input('''What do you wish to Decode?
''')
        code = theMessage.lower().replace('a','**').replace('b','*+').replace('c','*-').replace('d','a').replace('e','b').replace('f','c').replace('g','d').replace('h','e').replace('i','f').replace('j','g').replace('k','h').replace('l','i').replace('m','j').replace('n','k').replace('o','l').replace('p','m').replace('q','n').replace('r','o').replace('s','p').replace('t','q').replace('u','r').replace('v','s').replace('w','t').replace('x','u').replace('y','v').replace('z','w').replace('**','x').replace('*+','y').replace('*-','z').upper()
        print(code)
        COPY = input('Do you want to copy to clip?(Y/N)')
        if COPY.lower() == 'y':
            copy2clip(code)
            print('Copied to Clipboard')
    elif question.lower() == 'c':
        theCode = input('''What do you wish to Code?
''')
        message = theCode.lower().replace('z','*-').replace('y','*+').replace('x','**').replace('w','z').replace('v','y').replace('u','x').replace('t','w').replace('s','v').replace('r','u').replace('q','t').replace('p','s').replace('o','r').replace('n','q').replace('m','p').replace('l','o').replace('k','n').replace('j','m').replace('i','l').replace('h','k').replace('g','j').replace('f','i').replace('e','h').replace('d','g').replace('c','f').replace('b','e').replace('a','d').replace('*-','c').replace('*+','b').replace('**','a')
        print(message)
        COPY = input('Do you want to copy to clip?(Y/N)')
        if COPY.lower() == 'y':
            copy2clip(message)
            print('Copied to Clipboard!')
