class Pokemon:
  def __init__(self,entry,name,types,description,is_caught):
    self.entry=entry
    self.name=name
    self.types=types
    self.description=description
    self.is_caught=is_caught
  def speak(self):
    print(self.name +" "+ self.name + '\n')
  def display_details(self):
    print("Entry Number: " + str(self.entry) + "\n" + "Name: " + self.name + "\n" + "Type: " + str(self.types) + "\n" + "Description: " + "\n" + self.description + "\n" + "is_caught: " + str(self.is_caught) + '\n')
object1 = Pokemon(1 , 'Pikachu','Electric',"It has small electric sacs on both its cheeks. If threatened, it looses electric charges from the sacs.Pikachu has already been caught!",True)
object2 = Pokemon(2,'Bulbasaur',['Grass','Poison'],"For some time after its birth, it uses the nutrients that are packed into the seed on its back in order to grow.",False)
object3 = Pokemon(3,'Ivysaur',['Grass','Poison'],"The more sunlight Ivysaur bathes in, the more strength wells up within it, allowing the bud on its back to grow larger.",True)
object1.speak()
object2.speak()
object3.speak()
object1.display_details()
object2.display_details()
object3.display_details()
   