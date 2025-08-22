#program for the Hogwarts sorting hat which sorts the user into one of 4 different houses based on responses to the given question:
Gryffindor=0
Ravenclaw=0
Hufflepuff=0
Slytherin=0
#Q1
print('Q1) Do you like dawn or dusk\n 1) Dawn\n 2) Dusk')
answer1=int(input('Enter your answer(1-2)'))
if answer1==1:
  Gryffindor+=1
  Ravenclaw+=1
elif answer1==2:
  Hufflepuff+=1
  Slytherin+=1
else:
  print('Wrong input')
#Q2      
print('Q2) When I\'m dead, I want people to remember me as:\n 1) The Good\n 2) The Great\n 3) The Wise\n 4) The Bold')
answer2=int(input('Enter your answer(1-4)'))
if answer2==1:
  Hufflepuff+=2
elif answer2==2:
  Slytherin+=2
elif answer2==3:
  Ravenclaw+=2
elif answer2==4:
  Gryffindor+=2
else:
  print('Wrong input')
#Q3
print('Q3) Which kind of instrument most pleases your ear?\n 1) The violin\n 2) The trumpet\n 3) The piano\n 4) The drum')
answer3=int(input('Enter your answer(1-4)')) 
if answer3==1:
  Slytherin+=4
elif answer3==2:
  Hufflepuff+=4
elif answer3==3:
  Ravenclaw+=4
elif answer3==4:
  Gryffindor+=4
else:
  print('Wrong input')
#Q4
print('Q4) Which quality best describes you?\n 1) Daring\n 2) Ambition\n 3) Loyalty\n 4) Curiosity')
answer4=int(input('Enter your answer(1-4)'))
if answer3==1:
  Gryffindor+=2
elif answer3==2:
  Slytherin+=2
elif answer3==3:
  Hufflepuff+=2
elif answer3==4:
  Ravenclaw+=2
else:
  print('Wrong input')
#Result:
'''print('The score for each house is:')
print('Gryffindor:'+str(Gryffindor))      
print('Hufflepuff:'+str(Hufflepuff))
print('Ravenclaw:'+str(Ravenclaw))
print('Slytherin:'+str(Slytherin))'''
most_points=max(Gryffindor,Slytherin,Hufflepuff,Ravenclaw)
print('The sorting hat has sorted you into the house:')
if Gryffindor==most_points:
  print('🦁Gryffindor:'+str(Gryffindor)+'points')
elif Ravenclaw==most_points:
  print('🦅Ravenclaw:'+str(Ravenclaw)+'points')
elif Hufflepuff==most_points:
  print('🦡Hufflepuff:'+str(Hufflepuff)+'points')
else:
  print('🐍Slytherin:'+str(Slytherin)+'points')



















