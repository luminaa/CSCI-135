class CelestialBody:
  """Represents a celestial body"""
  def __init__(self, name, diameter, distance, moons):
    self.name = name
    self.diameter = diameter
    self.distance = distance
    self.moons = moons
    
  def compared_to_earth(self):
    """Determines the size of a celestial
    body relative to Earth using diameter"""
    earth = 12756.3
    relative_size = self.diameter / earth
    return relative_size

planet = CelestialBody("Jupiter", 142984, 778360000, 79)
print(planet.compared_to_earth())