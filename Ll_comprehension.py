#!/bin/python3
list1 = ['emma', 'ruth', 'happy', 'enoch', 'eggs']
list2 = []
for i in list1:
    if 'e' in i:
       list2.append(i)
print(list2)
list3 = ['indomie', 'osas', 'petri', 'pauli', 'emma', 'zebra']
list4 = [i for i in list3 if 'i' in i]
print(list4)
# the syntax is[expression for item in iterable if condition == true

