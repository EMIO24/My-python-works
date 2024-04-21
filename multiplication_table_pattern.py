row = int(input('The maximum number of rows: '))
for i in range(1, row + 1):
    for j in range(1, i + 1):
        square = i * j
        print(square, end= ' ')
    print("")