'''i want to write a program to determine if a worker is entitled to overtime pay in the week'''
print("Input your work day to know if you are entitled to overtime pay")
w_d = input('the weekday you worked: ')
if w_d == 'saturday' or w_d == 'sunday':
    print("you are entitled to overtime pay")
elif w_d == 'friday' or w_d == 'wednesday':
    print("your expected work hour is incomplete, so you are not entitled to overtime pay")
else:
    print("you are not entitled to overtime pay")

print("Thank you for understanding")