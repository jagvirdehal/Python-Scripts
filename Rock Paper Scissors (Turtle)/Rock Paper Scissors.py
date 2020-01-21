while True:
    from random import randint
    print('Rock = 1\nPaper = 2\nScissors = 3')
    choice = int(input())
    compChoice = randint(1,3)
    print(compChoice)
    if choice > 3 or choice < 1:
        print('Choice Error')
    elif choice == compChoice:
        print('DRAW')
    elif choice+1 == compChoice or (choice-2 and compChoice == 1):
        print('LOSE')
    else:
        print('WIN')
