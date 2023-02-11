class Observation:
  def __init__(self, date, temperature, elevation, penguins, precipitation=0):
    self.date = date
    self.temperature = temperature
    self.elevation = elevation
    self.penguins = penguins
    self.precipitation = precipitation

class BigCat:
  genus = "panthera"
  def __init__(self, species, common_name, habitat):
    self.species = species
    self.common_name = common_name
    self.habitat = habitat