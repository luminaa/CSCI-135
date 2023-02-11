class CelestialBody:
  """Represents a celestial body"""
  def __init__(self, name, diameter, distance, moons):
    self.name = name
    self.diameter = diameter
    self.distance = distance
    self.moons = moons
  
  @classmethod
  def make_earth(cls):
    return CelestialBody("Earth", 12756.3, 149600000, 1)

my_planet = CelestialBody.make_earth()

print(my_planet.name) # Earth
print(my_planet.distance) # 149600000
print(my_planet.diameter) # 12756.3
print(my_planet.moons) # 1