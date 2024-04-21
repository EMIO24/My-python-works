Rows = int(input('Number of rows: '))
for i in range(1, Rows+1):
    for j in range(1, i+1):
        print('*', end=' ')
    print("")
for b in range(Rows-1, 0, -1):
    for c in range(1, b+1):
        print('*', end=' ')
    print("")