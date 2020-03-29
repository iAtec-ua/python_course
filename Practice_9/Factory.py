class TransportInterface:
    def drive(self):
        pass


class Car(TransportInterface):
    def drive(self):
        print("Give ride by car")


class Ship(TransportInterface):
    def drive(self):
        print("Give ride by ship")


class TransportFactory:
    @staticmethod
    def getTransport(type):
        if type == "car":
            return Car()
        if type == "ship":
            return Ship()
        assert 0, "No transport"


car = TransportFactory.getTransport("car")
car.drive()

ship = TransportFactory.getTransport("ship")
ship.drive()

# plane = TransportFactory.getTransport("plane")
# plane.drive()
