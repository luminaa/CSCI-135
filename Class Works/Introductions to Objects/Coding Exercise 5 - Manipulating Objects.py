class Subway:
    fare = 2.4
    def __init__(self):
        self.stops = ["Alewife", "Davis", "Porter", "Harvard", "Central", "Kendall"]
        self.current_stop= "Alewife"
        self.direction = "south"
        self.passengers = 0
        self.total_fares = 0

    @classmethod
    def change_fare(cls, new_fare):
        """Change fare for all instances of Subway class"""
        Subway.fare = new_fare
    
    def board(self, new_passengers):
        """Adds the number of people boarding the subway.
        Also adds to total_fares for the new passengers"""
        self.passengers += new_passengers
        self.total_fares += new_passengers * Subway.fare

    def disembark(self, passengers_leaving):
        """Subtracts the number of people exiting the subway"""
        if passengers_leaving > self.passengers:
            self.passengers = 0
        else:
            self.passengers -= passengers_leaving


    def advance(self):
        """Advances the subway to the next stop"""
        current_index = self.stops.index(self.current_stop)
        if self.direction == "south":
            if self.current_stop == "Kendall":
                self.current_stop = "Central"
                self.direction = "north"
            else:
                self.current_stop = self.stops[current_index + 1]
        else:
            if self.current_stop == "Alewife":
                self.current_stop = "Davis"
                self.direction = "south"
            else:
                self.current_stop = self.stops[current_index - 1]

    def distance(self, desired_stop):
        """Returns the number of stops between the
        current location and the desired stop"""
        current_index = self.stops.index(self.current_stop)
        desired_index = self.stops.index(desired_stop)
        return abs(current_index - desired_index)



# Create a new subway instance
subway = Subway()

# Check the current stop and passengers on the subway
print("Current stop:", subway.current_stop)
print("Passengers:", subway.passengers)

# Board 10 passengers
subway.board(10)

# Check the total fares
print("Total fares:", subway.total_fares)

# Advance the subway to the next stop
subway.advance()

# Check the current stop
print("Current stop:", subway.current_stop)

# Disembark 5 passengers
subway.disembark(5)

# Check the number of passengers
print("Passengers:", subway.passengers)

# Change the fare to 2.6
Subway.change_fare(2.6)

# Check the new fare
print("New fare:", Subway.fare)

# Board 10 passengers
subway.board(10)

# Check the total fares
print("Total fares:", subway.total_fares)

# Get the distance between the current stop and Kendall
print("Distance to Kendall:", subway.distance("Kendall"))
