Birthdays = { 'Garv' : '24 March', 'Apurv' : '11 July', 'Rudra' :  '23 October' }

while True:
    print('Enter a name : (Blank To Quit)')
    name = input()
    if name == ' ':
        break
    if name in Birthdays:
        print(Birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday')
        bday = input()
        Birthdays[name] = bday
        print('Birthdays base updated')