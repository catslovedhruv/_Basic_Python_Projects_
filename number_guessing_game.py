#number guessing game: the user has to guess what number the program is thinking of!

import random
import time


#introduction:
print('Welcome to the number guessing game!')
time.sleep(1)
print("The program is choosing a number from 1 to 10")
time.sleep(1)
number=random.randint(1,10)
print('The program has chosen a number!')
time.sleep(1)
print('Guess what number the program has chosen! You get 3 tries(remember the program has selected a random number from one to 10!)')
time.sleep(1)

#guess counter:
guess=0


#main loop:
while guess<3:
 guess+=1 
 try:
    user_guess=int(input("Enter your guess!"))
 except ValueError:
     print("Enter an integer!")
     user_guess=int(input("Enter your guess"))
 except Exception:
     print('Something went wrong. Please run the program again')
 if user_guess>number:
   print(f"Your guess was incorrect, try again(Hint:The number chosen by the program is lesser than {user_guess})")
 elif user_guess<number:
   print(f"Your guess was incorrect, try again(Hint:The number chosen by the program is greater than {user_guess})")
#conditional statements:

 if user_guess==number:
  guess=8
  print(f"You got it!, The number the program was thinking of was {number}")
 if guess>=3 and guess!=8:
  print('You ran out of guesses!(run the program again if you want to play again)')
 elif guess==8:
  print('You won against the program by accurately guessing the number it was thinking of! run the program again if you want to keep playing :)')

















