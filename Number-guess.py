# this is a guess the number game.
import random
from tracemalloc import take_snapshot
print('hello. whats your name,meow?')
name= input()
secretnumber= random.randint (1,20)
print('well, ' + name + ', i am thinking of a number between 1 and 20')

#ask the player to guess 6 times
for guessestaken in range(1,7):
    print ('take a guess.')
    guess = int(input())
    if guess < secretnumber:
        print('your guess is too low')
    elif guess > secretnumber:
        print('your guess is too high.')
    else:
        break #this condition is the correct guess!

if guess == secretnumber:
    print ('good job, ' + name + "!you guessed mu number in " + str(guessestaken) + ' guesses!')
else:
    print ('nope . the number i was thinking of was '+ str(secretnumber))