Pn = int(input('Enter a number: '))

if Pn <= 1:
    print(f"{Pn} should be a number greater than 1")
    
elif Pn > 1:
    for i in range(2, Pn):
        if Pn % i == 0:
            print(f"{Pn} is not a prime number")
            print(f"{i} is a factor of {Pn}")
            break
    else:
        print(f"{Pn} is a prime number")