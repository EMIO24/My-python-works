rows = int(input('How many number of rows: '))
for i in range(1, rows + 1):
    for j in range(1, rows - i +1):
        print(end=' ')
    for b in range(1, i+1):
        print('*', end=' ')
    print("")