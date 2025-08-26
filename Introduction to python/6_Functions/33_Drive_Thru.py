def get_item(number):
  if number == 1:
    print('🍔 Cheeseburger')
  elif number == 2:
    print('🍟 Fries')
  elif number == 3:
    print('🥤 Soda')
  elif number == 4:
    print('🍦 Ice Cream')
  elif number == 5:
    print('🍪 Cookie')
  else:
    print("Not in the menu")
def welcome():
  print("Welcome!")
  print("Here's the menu:")
  print('1. 🍔 Cheeseburger')
  print('2. 🍟 Fries')
  print('3. 🥤 Soda')
  print('4. 🍦 Ice Cream')
  print('5. 🍪 Cookie')
welcome()
number = int(input("What do you want to order?"))
get_item(number)