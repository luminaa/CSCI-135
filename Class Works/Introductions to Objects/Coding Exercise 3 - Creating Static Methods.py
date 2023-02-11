class CelestialBody:
    """Represents a celestial body"""
    def __init__(self, name, diameter, distance, moons):
        self.name = name
        self.diameter = diameter
        self.distance = distance
        self.moons = moons
        
    @staticmethod
    def closer_to_sun(body1, body2):
        if body1.distance < body2.distance:
            return body1.name
        else:
            return body2.name

mercury = CelestialBody("Mercury", 4879.4, 57909000, 0)
venus = CelestialBody("Venus", 12103.6, 108160000, 0)

print(CelestialBody.closer_to_sun(mercury, venus))