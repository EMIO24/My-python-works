row = int(input('Enter the number of rows: '))
for i in range(row, 0, -1):
    for space in range(1, row - i + 1):
        print(end=' ')
    for star in range(i):
        print('*', end=' ')
    print("")
for j in range(1, row + 1):
    for spaces in range(1, row - j + 1):
        print(end=" ")
    for stars in range(1, j + 1):
        print('*', end=' ')
    print("")
