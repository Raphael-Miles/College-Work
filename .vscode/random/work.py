import random

target = random.randint(1,20)
guesses = 0

while True:
    guess = int(input('Guess the target number: '))
    guesses += 1
    if guess < target:
        print('Too low')
    elif guess > target:
        print('Too high')
    else:
        print('You guessed it right!')
        print(f'It took {guesses} number of tries.')
        if guesses > 5:
            print('OMG, you fucking suck at guessing')
        break
        
