while True:
    question = input('''Would you like to Code or Decode? (C/D)
''')
    if question.lower()[0] == 'c':
        message = input('''Enter the message:
''')
        print(message.lower().replace('a','01 ').replace('b','02 ').replace('c','03 ').replace('d','04 ').replace('e','05 ').replace('f','06 ').replace('g','07 ').replace('h','08 ').replace('i','09 ').replace('j','10 ').replace('k','11 ').replace('l','12 ').replace('m','13 ').replace('n','14 ').replace('o','15 ').replace('p','16 ').replace('q','17 ').replace('r','18 ').replace('s','19 ').replace('t','20 ').replace('u','21 ').replace('v','22 ').replace('w','23 ').replace('x','24 ').replace('y','25 ').replace('z','26 ').upper())
    elif question.lower()[0] == 'd':
        code = input('''Enter the code:
''')
        code = code+' '
        print(code.lower().replace('01 ','a').replace('02 ','b').replace('03 ','c').replace('04 ','d').replace('05 ','e').replace('06 ','f').replace('07 ','g').replace('08 ','h').replace('09 ','i').replace('10 ','j').replace('11 ','k').replace('12 ','l').replace('13 ','m').replace('14 ','n').replace('15 ','o').replace('16 ','p').replace('17 ','q').replace('18 ','r').replace('19 ','s').replace('20 ','t').replace('21 ','u').replace('22 ','v').replace('23 ','w').replace('24 ','x').replace('25 ','y').replace('26 ','z').upper())
    input('Press Enter to Continue')
