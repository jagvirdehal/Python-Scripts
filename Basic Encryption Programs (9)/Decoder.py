import subprocess
CODEin = input('''Enter the CODE:
''')
CODE = CODEin[2::].replace('1','q').replace('2','w').replace('4','r').replace('5','t').replace('6','y').replace('7','u').replace('a','a').replace('b','s').replace('k','x').replace('m','v').replace('n','b').replace('o','n').replace('p','m').replace('z',' ').replace('j','z').replace('g','j').replace('e','g').replace('3','e').replace('0','p').replace('9','o').replace('h','k').replace('f','h').replace('d','f').replace('c','d').replace('l','c').replace('i','l').replace('8','i')[::-1]
def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)
print()
print(''.join([ CODE[x:x+2][::-1] for x in range(0, len(CODE), 2) ]))
print()
copy2clip(''.join([ CODE[x:x+2][::-1] for x in range(0, len(CODE), 2) ]))
print('Copied to Clipboard (May not work on Linux and Mac)')
input()
