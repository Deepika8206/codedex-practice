pH = int(input('Enter a value between 0 and 14: ' ))
if pH > 7:
  print('Basic')
elif pH < 7:
  print('Acidic')
else:
  print('Neutral')