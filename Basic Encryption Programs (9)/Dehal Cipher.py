import subprocess
def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)
while True:
    text = input('''Enter the Text that should be encrypted or decrypted (Decryptions start with "=="):
''')
    if text[0:2] == '==':
        text = text[2::].replace('1','q').replace('2','w').replace('4','r').replace('5','t').replace('6','y').replace('7','u').replace('a','a').replace('b','s').replace('k','x').replace('m','v').replace('n','b').replace('o','n').replace('p','m').replace('z',' ').replace('j','z').replace('g','j').replace('e','g').replace('3','e').replace('0','p').replace('9','o').replace('h','k').replace('f','h').replace('d','f').replace('c','d').replace('l','c').replace('i','l').replace('8','i')[::-1]
        text = ''.join([ text[x:x+2][::-1] for x in range(0, len(text), 2) ])
        print('''
'''+text)
        copy = input('''
Would you like to copy this message? (Y/N) ''')
        if copy.lower() == 'y':
            copy2clip(text)
            print('''
Copied to Clipboard
''')
    else:
        text = text.replace(' 1 ',' one ').replace(' 2 ',' two ').replace(' 3 ',' three ').replace(' 4 ',' four ').replace(' 5 ',' five ').replace(' 6 ',' six ').replace(' 7 ',' seven ').replace(' 8 ',' eight ').replace(' 9 ',' nine ').replace(' 0 ',' zero ')
        text = ''.join([i for i in text if not i.isdigit()])
        text = ''.join([ text[x:x+2][::-1] for x in range(0, len(text), 2) ])
        text = '=='+text.lower().replace('q','1').replace('w','2').replace('r','4').replace('t','5').replace('y','6').replace('u','7').replace('a','a').replace('e','3').replace('p','0').replace('i','8').replace('l','i').replace('c','l').replace('d','c').replace('f','d').replace('h','f').replace('k','h').replace('x','k').replace('o','9').replace('n','o').replace('b','n').replace('s','b').replace('m','p').replace('v','m').replace('g','e').replace('j','g').replace('z','j').replace(' ','z')[::-1]
        print('''
'''+text)
        copy = input('''
Would you like to copy this message? (Y/N) ''')
        if copy.lower() == 'y':
            copy2clip(text)
            print('''
Copied to Clipboard
''')            
    input('Press enter to type another message')
