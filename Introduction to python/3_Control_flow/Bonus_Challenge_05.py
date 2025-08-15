Weight = float(input("What is the Earth's weight? "))
Number = int(input("Planet Number: "))
Relative_Gravity = 0
if Number == 1:
  Relative_Gravity = 0.38
  User_weight = Weight * Relative_Gravity
  print  (User_weight )
elif Number == 2:
  Relative_Gravity = 0.91
  User_weight = Weight * Relative_Gravity
  print (User_weight )
elif Number == 3:
  Relative_Gravity = 0.38
  User_weight = Weight * Relative_Gravity
  print(User_weight )
elif Number == 4:
  Relative_Gravity = 2.53
  User_weight = Weight * Relative_Gravity
  print(User_weight )
elif Number == 5:
  Relative_Gravity = 1.07
  User_weight = Weight * Relative_Gravity
  print(User_weight )
elif Number == 6:
  Relative_Gravity = 0.89
  User_weight = Weight * Relative_Gravity
  print(User_weight )
elif Number == 7:
  Relative_Gravity = 1.14
  User_weight = Weight * Relative_Gravity
  print(User_weight )
else:
  print("Invalid planet number")
