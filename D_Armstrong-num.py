n = int(input('Enter a 3-digit Armstrong number: '))
Sum = 0
temp = n
while temp > 0:
    digit = temp % 10
    Sum = Sum + digit ** 3
    temp = temp // 10
if n == Sum:
    print(f"{Sum} is an Armstrong number")
else:
    print(f"{n} is not an Armstrong number")