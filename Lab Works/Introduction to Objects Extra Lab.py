class Zoo:
  def __init__(self, big_cats, primates, reptiles, birds):
    self.big_cats = big_cats
    self.primates = primates
    self.reptiles = reptiles
    self.birds = birds

  def total_animals(self):
    return self.big_cats + self.primates + self.reptiles + self.birds

  def total_mammals(self):
    return self.big_cats + self.primates

  def most_animals(self):
    if self.big_cats > self.primates and self.big_cats > self.reptiles and self.big_cats > self.birds:
      return "big_cats"
    elif self.primates > self.big_cats and self.primates > self.reptiles and self.primates > self.birds:
      return "primates"
    elif self.reptiles > self.big_cats and self.reptiles > self.primates and self.reptiles > self.birds:
      return "birds"
    return "birds"

my_zoo = Zoo(10, 30, 90, 120)
print(my_zoo.total_animals())
print(my_zoo.total_mammals())
print(my_zoo.most_animals())
