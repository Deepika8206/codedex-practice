Grffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0
question1 = int(input('Do you like 1)Dawn or 2)Dusk? '))
if question1 == 1:
  Grffindor += 1
  Ravenclaw += 1
elif question1 == 2:
  Hufflepuff += 1
  Slytherin += 1
else:
  print('Wrong input')
print ('Grffindor points is: '+ str(Grffindor))
print ( 'Ravenclaw points is: '+ str(Ravenclaw))
print ( 'Hufflepuff points is: '+ str(Hufflepuff))
print ( 'Slytherin points is: '+ str(Slytherin))
print(' ')
print("1) The Good  2) The Great 3) The Wise 4) the Bold")
question2 = int(input("When I'm dead,I want people to rember me as: "))
if question2 == 1:
  Hufflepuff +=2
elif question2 == 2:
  Slytherin +=2
elif question2 == 3:
  Ravenclaw += 2
elif question2 == 4:
  Grffindor +=2 
else:
  print ('Wrong input')
print ('Grffindor points is: '+ str(Grffindor))
print ( 'Ravenclaw points is: '+ str(Ravenclaw))
print ( 'Hufflepuff points is: '+ str(Hufflepuff))
print ( 'Slytherin points is: '+ str(Slytherin))
print(' ')
print ('1) The Violin 2) The Trumpet 3) The Piano 4) The Drum')
question3 = int(input('Which kind of instrument most pleases you ear? '))
if question3 == 1:
  Slytherin +=4
elif question3 == 2:
  Hufflepuff +=4
elif question3 == 3:
  Ravenclaw += 4
elif question3 == 4:
  Grffindor += 4 
else:
  print ('Wrong input')
print ('Grffindor points is: '+ str(Grffindor))
print ( 'Ravenclaw points is: '+ str(Ravenclaw))
print ( 'Hufflepuff points is: '+ str(Hufflepuff))
print ( 'Slytherin points is: '+ str(Slytherin))
print(' ')
if ( Grffindor >= Hufflepuff and Grffindor >= Ravenclaw and Grffindor >= Slytherin):
  print ( 'Grffindor Wins!!!!')
elif ( Hufflepuff >= Grffindor and Hufflepuff >= Ravenclaw and Hufflepuff >= Slytherin):
  print ('Hufflepuff Wins!!!!')
elif ( Slytherin >= Hufflepuff and Slytherin >= Ravenclaw and  Slytherin>= Grffindor):
  print ('Slytherin Wins!!!!')
else:
  print ('Ravenclaw Wins!!!!')