'''Write a python script that determines the season
based on the month entered by the user. use if=elif-else statements to cover 
different seasons (e.g, winter, spring, summer, fall)'''
x = input("input the month to be checked: ")
if x == "December" or x == "January" or x == "february":
    print("Winter")
elif x == "june" or x == "july" or x == "august":
    print("Summer")
elif x == "march" or x == "april" or x == "may":
    print("Spring")
else:
    print("Fall (Autumn)")
print("Done.")