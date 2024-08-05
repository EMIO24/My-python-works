from math import factorial

row = int(input('Enter the row number: '))

for n in range(row):
    for space in range(1, row-n):
        print(end=' ')
        
    for r in range(n+1):
        ncr = factorial(n) // (factorial(r) * factorial(n-r))
        print(ncr, end=' ')
    print("")