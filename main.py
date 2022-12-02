responses = {}

polling_active = True

while polling_active:
    name = input("What is your name? ")
    response = input('What career do you want to have? ')
    responses[name] = response
    repeat = input("Do you want to be asked again? (yes/no) ")
    if(repeat == 'no'):
        polling_active = False


print(responses)