class Bus:
    """ This class describes how a bus may look like"""

    # for class variables, to be explained in slide 19
    numberOfBusses = 0

    # Now we access a class variable, to be explained in slide 19
    @classmethod
    def bus_count(cls):
        return cls.numberOfBusses

    def __init__(self, driverName, onDuty, cities):
        self.driverName = driverName
        self.onDuty = onDuty
        self.cities = cities
        self.numPassengers = 0  # When creating a new bus!
        Bus.numberOfBusses += Bus.numberOfBusses + 1
        # for class variables slide 19

    # Let us describe the behavior of the class using methods
    def changeDriverName(self, newDriverName):
        """ A method to change the driver name """
        self.driverName = newDriverName

    # Let is update the number of passengers using another method
    def pickUpPassengers(self, numOfPickedPassengers):
        """" Increase the number of passengers """
        self.numPassengers += numOfPickedPassengers



# The below line calls __init__ and sets the attribute values
newBus = Bus("Ahmed", True, ['Muscat', 'Mutrah'])
print(newBus.cities)

newBus.changeDriverName("Sami")
print(newBus.driverName)

newBus.pickUpPassengers(4)
print(newBus.numPassengers)

# for class variable, to be explained in slide 19
print("we currently have ", Bus.bus_count(), " busses!")
