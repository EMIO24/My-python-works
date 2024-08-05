import re
pwd = input('Enter your password: ')
pwd_len = len(pwd)
is_valid = False
while True:
    if pwd_len < 8:
        print("password must be at least 8 characters long")
        break
    elif pwd_len > 25:
        print("Password must not be more than 25 characters")
        break
    elif not re.search('[A-Z]', pwd):
        print("Password must contain at least one upper case character")
        break
    elif not re.search('[a-z]', pwd):
        print("Password must contain at least one lower case character")
        break
    elif not re.search('[0-9]', pwd):
        print("Password must contain at least one number")
        break
    else:
        is_valid = True
        break
if is_valid == True:
    print("Password accepted!")
else:
    print("Invalid Password")