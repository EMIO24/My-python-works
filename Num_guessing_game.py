import random
num = random.randint(1, 15)
guess = int(input('Guess a number between 1 and 15: '))
i = 1
while guess != num:
    if guess < num:
        print('Your guess is too low')
    elif guess > num:  
        print('Your guess is too high')
    guess = int(input('Guess again: '))
    i += 1
print('You guessed it right')
print('Total attempts: ', i)
# end while