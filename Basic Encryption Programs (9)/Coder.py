import subprocess
CODEint = input('''Enter the Message you wish to CODE (NO NUMBERS):
''')
CODEin = ''.join([i for i in CODEint if not i.isdigit()])
CODE = ''.join([ CODEin[x:x+2][::-1] for x in range(0, len(CODEin), 2) ])
def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)
print()
print('=='+CODE.lower().replace('q','1').replace('w','2').replace('r','4').replace('t','5').replace('y','6').replace('u','7').replace('a','a').replace('v','m').replace('e','3').replace('p','0').replace('i','8').replace('l','i').replace('c','l').replace('d','c').replace('f','d').replace('h','f').replace('k','h').replace('x','k').replace('o','9').replace('n','o').replace('b','n').replace('s','b').replace('m','p').replace('g','e').replace('j','g').replace('z','j').replace(' ','z')[::-1])
print()
copy2clip('=='+CODE.lower().replace('q','1').replace('w','2').replace('r','4').replace('t','5').replace('y','6').replace('u','7').replace('a','a').replace('p','0').replace('m','p').replace('v','m').replace('e','3').replace('i','8').replace('l','i').replace('c','l').replace('d','c').replace('f','d').replace('h','f').replace('k','h').replace('x','k').replace('o','9').replace('n','o').replace('b','n').replace('s','b').replace('g','e').replace('j','g').replace('z','j').replace(' ','z')[::-1])
print('Copied to Clipboard (May not work on Linux or Mac)')
input()
