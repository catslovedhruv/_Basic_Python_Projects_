#Hangman:-a game where the user guesses letters to reveal a hidden word. You'll need to use lists to store the word and the guessed letters, and loops to manage turns.
import random
import time
word_list=["Kabul", "Algiers", "Buenosaires", "Canberra", "Vienna", "Nassau", "Dhaka", "Bridgetown", "Brussels", "Belmopan", "Brasilia", "Ottawa", "Santiago", "Beijing", "Bogota", "Havana", "Copenhagen", "Cairo", "Helsinki", "Paris", "Berlin", "Athens", "Newdelhi", "Jakarta", "Tehran", "Baghdad", "Dublin", "Rome", "Tokyo", "Mexicocity", "Amsterdam", "Wellington", "Pyongyang", "Oslo", "Islamabad", "Panamacity", "Lima", "Manila", "Warsaw", "Lisbon", "Doha", "Moscow", "Riyadh", "Singapore", "Bloemfontein", "Capetown", "Seoul", "Madrid", "Stockholm", "Bern", "Damascus", "Bangkok", "Ankara", "Kyiv", "Abudhabi", "London", "Washingtondc", "Caracas", "Hanoi"]
tries=0

hidden_word=random.choice(word_list)
#print(hidden_word)#Temporary: remove after testing
print('Welcome to Hangman! :\n a game where you get turns to guess letters to reveal a hidden word! ')
time.sleep(1)
print('You get 7 guesses in total.(a correct guess does not decrease your number of guesses left.)')
time.sleep(1)
print("the genre is: 'capital cities'. \n The program will think of a capital city across the world and you have to guess it!")
time.sleep(1)
print("The program is thinking of a city ⌛⏳")
time.sleep(3)
print("The program has selected a city")
time.sleep(1)
print("To save this man you need to guess the hidden word within 7 tries!")
print("__________ ")
print("    || ")
print("    ||   ")
print("    😨  " )
print(" ---||--- ")
print("    ||     ")
print("    /\   ")
print("   /  \  ")
time.sleep(1)
print(f'The length of the hidden word is {hidden_word.__len__()}')



#first letter:
while True:
 try:
      first_letter=input("Enter the first letter")
      if len(first_letter)!=1 or not first_letter.isalpha():
         print("Enter a single letter")
         first_letter=input("Enter the first letter")


 except ValueError:
     first_letter=input("Enter the first letter")
     print("Enter a letter and try again")

 if first_letter.lower()==hidden_word[0].lower():
  hidden_word_list=[first_letter.upper()]
  print(hidden_word_list)


#conditions for the first letter:
 if first_letter.lower()==hidden_word[0].lower():
   print(f"Correct! the first letter of the word is: {first_letter} ")
   break #breaks the inner while loop
  

 else:
   tries+=1
   print(f"Incorrect! the first letter of the word is not {first_letter}")
   print(f"You have {7-tries} tries left")

#to check if player ran out of tries
 if tries>=7:
   print("You ran out of tries.")
   print(f"The hidden word was {hidden_word}")
   game_over=True
 else:
   game_over=False

 if game_over:
   print("To play again,run the program once more.")
   break #breaks the outer while loop



#second letter:
if tries<7:
 while True:
  try:
     second_letter=input("Enter the second letter")
     if len(second_letter)!=1 or not second_letter.isalpha():
        print("Enter a single letter")
        second_letter=input("Enter the second letter")


  except ValueError:
    print("Enter a letter and try again")
    second_letter =input("Enter the second letter")

  if second_letter.lower()==hidden_word[1].lower():
   hidden_word_list.append(second_letter.upper())
   print(hidden_word_list)
  else:
    print(hidden_word_list)


#conditions for the second letter:
  if second_letter.lower()==hidden_word[1].lower():
     print(f"Correct! the second letter of the word is: {second_letter} ")
     break #breaks the inner while loop

  else:
     tries+=1
     print(f"Incorrect! the second letter of the word is not {second_letter}")
     print(f"You have {7-tries} tries left")

#to check if player ran out of tries
  if tries>=7:
     print("You ran out of tries.")
     print(f"The hidden word was {hidden_word}")
     game_over=True
  else:
     game_over=False




  if game_over:
   print("To play again,run the program once more.")
   break #breaks the outer while loop


#third letter:
if tries<7:
 while True:
  try:
     third_letter=input("Enter the third letter")
     if len(third_letter)!=1 or not third_letter.isalpha():
        print("Enter a single letter")
        third_letter=input("Enter the third letter")


  except ValueError:
     print("Enter a letter and try again")
     third_letter=input("Enter the third letter")


  if third_letter.lower()==hidden_word[2].lower():
   hidden_word_list.append(third_letter.upper())
   print(hidden_word_list)
  else:
    print(hidden_word_list)

#conditions for the third letter:
  if third_letter.lower()==hidden_word[2].lower():
     print(f"Correct! the third letter of the word is: {third_letter} ")
     break #breaks the while loop
  

  else:
     tries+=1
     print(f"Incorrect! the third letter of the word is not {third_letter}")
     print(f"You have {7-tries} tries left")

#to check if player ran out of tries
  if tries>=7:
     print("You ran out of tries.")
     print(f"The hidden word was {hidden_word}")
     game_over=True
  else:
     game_over=False


  if game_over:
   print("To play again,run the program once more.")
   break #breaks the outer while loop

#fourth letter:
if tries<7:
 while True: 
  try:
     fourth_letter=input("Enter the fourth letter")
     if len(fourth_letter)!=1 or not fourth_letter.isalpha():
        print("Enter a single letter")
        fourth_letter=input("Enter the fourth letter")


  except ValueError:
    print("Enter a letter and try again")
    fourth_letter=input("Enter the fourth letter")

  if fourth_letter.lower()==hidden_word[3].lower():
   hidden_word_list.append(fourth_letter.upper())
   print(hidden_word_list)
  else:
    print(hidden_word_list)

#conditions for the fourth letter:
  if fourth_letter.lower()==hidden_word[3].lower():
   print(f"Correct! the fourth letter of the word is: {fourth_letter} ")
   break#breaks the inner while loop


  else:
     tries+=1
     print(f"Incorrect! the fourth letter of the word is not {fourth_letter}")
     print(f"You have {7-tries} tries left")

#to check if player ran out of tries
  if tries>=7:
   print("You ran out of tries.")
   print(f"The hidden word was {hidden_word}")
   game_over=True
  else:
   game_over=False
  if game_over:
   print("To play again,run the program once more.")
   break #breaks the while loop


#to check if the guessed word = hidden word:
if tries<7:
 guessed_word=first_letter+second_letter+third_letter+fourth_letter
 if guessed_word.lower()==hidden_word.lower():
  game_won=True
 else:
   game_won=False
 if game_won==True:
  print(f"You got it! The hidden word was: {guessed_word}")
  print("You won the game and thus saved the man!!!")
  print("To play again,run the program once more")


#fifth letter:
if tries<7 and len(hidden_word)>4:
 while True: 
  try:
     fifth_letter=input("Enter the fifth letter")
     if len(fifth_letter)!=1 or not fifth_letter.isalpha():
        print("Enter a single letter")
        fifth_letter=input("Enter the fifth letter")


  except ValueError:
    print("Enter a letter and try again")
    fifth_letter=input("Enter the fifth letter")

  if fifth_letter.lower()==hidden_word[4].lower():
   hidden_word_list.append(fifth_letter.upper())
   print(hidden_word_list)
  else:
    print(hidden_word_list)

#conditions for the fifth letter:
  if fifth_letter.lower()==hidden_word[4].lower():
   print(f"Correct! the fifth letter of the word is: {fifth_letter} ")
   break#breaks the inner while loop


  else:
     tries+=1
     print(f"Incorrect! the fifth letter of the word is not {fifth_letter}")
     print(f"You have {7-tries} tries left")

#to check if player ran out of tries
  if tries>=7:
   print("You ran out of tries.")
   print(f"The hidden word was {hidden_word}")
   game_over=True
  else:
   game_over=False
  if game_over:
   print("To play again,run the program once more.")
   break #breaks the while loop


#to check if the guessed word = hidden word:
if tries<7 and len(hidden_word)>4:
 guessed_word=first_letter+second_letter+third_letter+fourth_letter+fifth_letter
 if guessed_word.lower()==hidden_word.lower():
  game_won=True
 else:
   game_won=False
 if game_won==True:
  print(f"You got it! The hidden word was: {guessed_word}")
  print("You won the game and thus saved the man!!!")
  print("To play again,run the program once more")


#sixth letter:
if tries<7 and len(hidden_word)>5:
 while True: 
  try:
     sixth_letter=input("Enter the sixth letter")
     if len(sixth_letter)!=1 or not sixth_letter.isalpha():
        print("Enter a single letter")
        sixth_letter=input("Enter the sixth letter")


  except ValueError:
    print("Enter a letter and try again")
    sixth_letter=input("Enter the sixth letter")

  if sixth_letter.lower()==hidden_word[5].lower():
   hidden_word_list.append(sixth_letter.upper())
   print(hidden_word_list)
  else:
    print(hidden_word_list)

#conditions for the sixth letter:
  if sixth_letter.lower()==hidden_word[5].lower():
   print(f"Correct! the sixth letter of the word is: {sixth_letter} ")
   break#breaks the inner while loop


  else:
     tries+=1
     print(f"Incorrect! the sixth letter of the word is not {sixth_letter}")
     print(f"You have {7-tries} tries left")

#to check if player ran out of tries
  if tries>=7:
   print("You ran out of tries.")
   print(f"The hidden word was {hidden_word}")
   game_over=True
  else:
   game_over=False
  if game_over:
   print("To play again,run the program once more.")
   break #breaks the while loop


#to check if the guessed word = hidden word:
if tries<7 and len(hidden_word)>5:
 guessed_word=first_letter+second_letter+third_letter+fourth_letter+fifth_letter+sixth_letter
 if guessed_word.lower()==hidden_word.lower():
  game_won=True
 else:
   game_won=False
 if game_won==True:
  print(f"You got it! The hidden word was: {guessed_word}")
  print("You won the game and thus saved the man!!!")
  print("To play again,run the program once more")


#seventh letter:
if tries<7 and len(hidden_word)>6:
 while True: 
  try:
     seventh_letter=input("Enter the seventh letter")
     if len(seventh_letter)!=1 or not seventh_letter.isalpha():
        print("Enter a single letter")
        seventh_letter=input("Enter the seventh letter")


  except ValueError:
    print("Enter a letter and try again")
    seventh_letter=input("Enter the seventh letter")

  if seventh_letter.lower()==hidden_word[6].lower():
   hidden_word_list.append(seventh_letter.upper())
   print(hidden_word_list)
  else:
    print(hidden_word_list)


#conditions for the seventh letter:
  if seventh_letter.lower()==hidden_word[6].lower():
   print(f"Correct! the seventh letter of the word is: {seventh_letter} ")
   break#breaks the inner while loop


  else:
     tries+=1
     print(f"Incorrect! the seventh letter of the word is not {seventh_letter}")
     print(f"You have {7-tries} tries left")

#to check if player ran out of tries
  if tries>=7:
   print("You ran out of tries.")
   print(f"The hidden word was {hidden_word}")
   game_over=True
  else:
   game_over=False
  if game_over:
   print("To play again,run the program once more.")
   break #breaks the while loop


#to check if the guessed word = hidden word:
if tries<7 and len(hidden_word)>6:
 guessed_word=first_letter+second_letter+third_letter+fourth_letter+fifth_letter+sixth_letter+seventh_letter
 if guessed_word.lower()==hidden_word.lower():
  game_won=True
 else:
   game_won=False
 if game_won==True:
  print(f"You got it! The hidden word was: {guessed_word}")
  print("You won the game and thus saved the man!!!")
  print("To play again,run the program once more")


#eighth letter:
if tries<7 and len(hidden_word)>7:
 while True: 
  try:
     eighth_letter=input("Enter the eighth letter")
     if len(eighth_letter)!=1 or not eighth_letter.isalpha():
        print("Enter a single letter")
        eighth_letter=input("Enter the eighth letter")


  except ValueError:
    print("Enter a letter and try again")
    eighth_letter=input("Enter the eighth letter")

  if eighth_letter.lower()==hidden_word[7].lower():
   hidden_word_list.append(eighth_letter.upper())
   print(hidden_word_list)
  else:
    print(hidden_word_list)


#conditions for the eighth letter:
  if eighth_letter.lower()==hidden_word[7].lower():
   print(f"Correct! the eighth letter of the word is: {eighth_letter} ")
   break#breaks the inner while loop


  else:
     tries+=1
     print(f"Incorrect! the eighth letter of the word is not {eighth_letter}")
     print(f"You have {7-tries} tries left")

#to check if player ran out of tries
  if tries>=7:
   print("You ran out of tries.")
   print(f"The hidden word was {hidden_word}")
   game_over=True
  else:
   game_over=False
  if game_over:
   print("To play again,run the program once more.")
   break #breaks the while loop


#to check if the guessed word = hidden word:
if tries<7 and len(hidden_word)>7:
 guessed_word=first_letter+second_letter+third_letter+fourth_letter+fifth_letter+sixth_letter+seventh_letter+eighth_letter
 if guessed_word.lower()==hidden_word.lower():
  game_won=True
 else:
   game_won=False
 if game_won==True:
  print(f"You got it! The hidden word was: {guessed_word}")
  print("You won the game and thus saved the man!!!")
  print("To play again,run the program once more")


#ninth letter:
if tries<7 and len(hidden_word)>8:
 while True: 
  try:
     ninth_letter=input("Enter the ninth letter")
     if len(ninth_letter)!=1 or not ninth_letter.isalpha():
        print("Enter a single letter")
        ninth_letter=input("Enter the ninth letter")


  except ValueError:
    print("Enter a letter and try again")
    ninth_letter=input("Enter the ninth letter")

  if ninth_letter.lower()==hidden_word[8].lower():
   hidden_word_list.append(ninth_letter.upper())
   print(hidden_word_list)
  else:
    print(hidden_word_list)


#conditions for the ninth letter:
  if ninth_letter.lower()==hidden_word[8].lower():
   print(f"Correct! the ninth letter of the word is: {ninth_letter} ")
   break#breaks the inner while loop


  else:
     tries+=1
     print(f"Incorrect! the ninth letter of the word is not {ninth_letter}")
     print(f"You have {7-tries} tries left")

#to check if player ran out of tries
  if tries>=7:
   print("You ran out of tries.")
   print(f"The hidden word was {hidden_word}")
   game_over=True
  else:
   game_over=False
  if game_over:
   print("To play again,run the program once more.")
   break #breaks the while loop


#to check if the guessed word = hidden word:
if tries<7 and len(hidden_word)>8:
 guessed_word=first_letter+second_letter+third_letter+fourth_letter+fifth_letter+sixth_letter+seventh_letter+eighth_letter+ninth_letter
 if guessed_word.lower()==hidden_word.lower():
  game_won=True
 else:
   game_won=False
 if game_won==True:
  print(f"You got it! The hidden word was: {guessed_word}")
  print("You won the game and thus saved the man!!!")
  print("To play again,run the program once more")


#tenth letter:
if tries<7 and len(hidden_word)>9:
 while True: 
  try:
     tenth_letter=input("Enter the tenth letter")
     if len(tenth_letter)!=1 or not tenth_letter.isalpha():
        print("Enter a single letter")
        tenth_letter=input("Enter the tenth letter")


  except ValueError:
    print("Enter a letter and try again")
    tenth_letter=input("Enter the tenth letter")

  if tenth_letter.lower()==hidden_word[9].lower():
   hidden_word_list.append(tenth_letter.upper())
   print(hidden_word_list)
  else:
    print(hidden_word_list)


#conditions for the tenth letter:
  if tenth_letter.lower()==hidden_word[9].lower():
   print(f"Correct! the tenth letter of the word is: {tenth_letter} ")
   break#breaks the inner while loop


  else:
     tries+=1
     print(f"Incorrect! the tenth letter of the word is not {tenth_letter}")
     print(f"You have {7-tries} tries left")

#to check if player ran out of tries
  if tries>=7:
   print("You ran out of tries.")
   print(f"The hidden word was {hidden_word}")
   game_over=True
  else:
   game_over=False
  if game_over:
   print("To play again,run the program once more.")
   break #breaks the while loop


#to check if the guessed word = hidden word:
if tries<7 and len(hidden_word)>9:
 guessed_word=first_letter+second_letter+third_letter+fourth_letter+fifth_letter+sixth_letter+seventh_letter+eighth_letter+ninth_letter+tenth_letter
 if guessed_word.lower()==hidden_word.lower():
  game_won=True
 else:
   game_won=False
 if game_won==True:
  print(f"You got it! The hidden word was: {guessed_word}")
  print("You won the game and thus saved the man!!!")
  print("To play again,run the program once more")


#eleventh letter:
if tries<7 and len(hidden_word)>10:
 while True: 
  try:
     eleventh_letter=input("Enter the eleventh letter")
     if len(eleventh_letter)!=1 or not eleventh_letter.isalpha():
        print("Enter a single letter")
        eleventh_letter=input("Enter the eleventh letter")


  except ValueError:
    print("Enter a letter and try again")
    eleventh_letter=input("Enter the eleventh letter")

  if eleventh_letter.lower()==hidden_word[10].lower():
   hidden_word_list.append(eleventh_letter.upper())
   print(hidden_word_list)
  else:
    print(hidden_word_list)


#conditions for the eleventh letter:
  if eleventh_letter.lower()==hidden_word[10].lower():
   print(f"Correct! the eleventh letter of the word is: {eleventh_letter} ")
   break#breaks the inner while loop


  else:
     tries+=1
     print(f"Incorrect! the eleventh letter of the word is not {eleventh_letter}")
     print(f"You have {7-tries} tries left")

#to check if player ran out of tries
  if tries>=7:
   print("You ran out of tries.")
   print(f"The hidden word was {hidden_word}")
   game_over=True
  else:
   game_over=False
  if game_over:
   print("To play again,run the program once more.")
   break #breaks the while loop


#to check if the guessed word = hidden word:
if tries<7 and len(hidden_word)>10:
 guessed_word=first_letter+second_letter+third_letter+fourth_letter+fifth_letter+sixth_letter+seventh_letter+eighth_letter+ninth_letter+tenth_letter+eleventh_letter
 if guessed_word.lower()==hidden_word.lower():
  game_won=True
 else:
   game_won=False
 if game_won==True:
  print(f"You got it! The hidden word was: {guessed_word}")
  print("You won the game and thus saved the man!!!")
  print("To play again,run the program once more")


#twelfth letter:
if tries<7 and len(hidden_word)>11:
 while True: 
  try:
     twelfth_letter=input("Enter the twelfth letter")
     if len(twelfth_letter)!=1 or not twelfth_letter.isalpha():
        print("Enter a single letter")
        twelfth_letter=input("Enter the twelfth letter")


  except ValueError:
    print("Enter a letter and try again")
    twelfth_letter=input("Enter the twelfth letter")

  if twelfth_letter.lower()==hidden_word[11].lower():
   hidden_word_list.append(twelfth_letter.upper())
   print(hidden_word_list)
  else:
    print(hidden_word_list)


#conditions for the twelfth letter:
  if twelfth_letter.lower()==hidden_word[11].lower():
   print(f"Correct! the twelfth letter of the word is: {twelfth_letter} ")
   break#breaks the inner while loop


  else:
     tries+=1
     print(f"Incorrect! the twelfth letter of the word is not {twelfth_letter}")
     print(f"You have {7-tries} tries left")

#to check if player ran out of tries
  if tries>=7:
   print("You ran out of tries.")
   print(f"The hidden word was {hidden_word}")
   game_over=True
  else:
   game_over=False
  if game_over:
   print("To play again,run the program once more.")
   break #breaks the while loop


#to check if the guessed word = hidden word:
if tries<7 and len(hidden_word)>11:
 guessed_word=first_letter+second_letter+third_letter+fourth_letter+fifth_letter+sixth_letter+seventh_letter+eighth_letter+ninth_letter+tenth_letter+eleventh_letter+twelfth_letter
 if guessed_word.lower()==hidden_word.lower():
  game_won=True
 else:
   game_won=False
 if game_won==True:
  print(f"You got it! The hidden word was: {guessed_word}")
  print("You won the game and thus saved the man!!!")
  print("To play again,run the program once more")





