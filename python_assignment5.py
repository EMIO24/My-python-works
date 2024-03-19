'''Develop a python script that asks for a user to enter a number,
if the number is even, print it's square; if it's odd,
print it's cube. Repeat this process until the user enters 0 to exit
the program. Use while loop and conditionals'''
while True:
    x = int(input('input a number (type 0 to quit): '))
    if x == 0:
        break
    if x % 2 == 0:
        print("it's square")
    if x % 2 != 0:
        print("it's cube")
print("Done")