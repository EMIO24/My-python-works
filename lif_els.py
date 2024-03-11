Age = int(input('how old are you?: '))
if Age < 18:
    print('you are not eligible to vote')
else:
    print('you are eligible to vote')
    
print("thank you for stepping forward")

print('you are not eligible to vote') if Age < 18 else print('you are eligible to vote')
print("Done")