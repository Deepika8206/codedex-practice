height = int(input('What is the height requirement: '))
credits = int(input('How many credits you have? '))
if height >= 137 and credits >= 10:
  print('Enjoy the ride!')
elif height < 137 and credits >= 10:
  print('You are not tall enough')
elif credits < 10 and height >= 137:
  print("You don't have enough credits")
else:
  print('Not met either of the requirements!')