'''Writing a code to collect input to determine if the user is elligible to cast a vote based on the programmed data'''
age = int(input('how old are you: '))
nat = input('which country are you from: ')
if age > 18 and age < 80 and nat == 'nigeria':
    print("you are eligible to cast a vote")
elif age > 18 and age < 80 and nat == 'south_africa':
    print("you are eligible to cast a vote")
else:
    print("you are not eligible to cast a vote")