class City:
  def __init__(self,name,country,population,landmarks):
    self.name=name
    self.country=country
    self.population=population
    self.landmarks=landmarks
Hometown=City('Kerala','India',999 , ['Boating','Kathakali'])
print(vars(Hometown))