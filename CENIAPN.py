#!/bin/python
# i want to write a code that will collect the user phone number and print out the even number in it
num = input('the user phone number: ')
even_num = []
for t_num in num:
    if int(t_num) % 2 == 0:
        even_num.append(t_num)
    else:
        print('odd num')
print(even_num)
