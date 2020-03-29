class AircraftInterface:
    def getType(self):
        pass


class Plane(AircraftInterface):
    def getType(self):
        print("Plane")


class Helicopter(AircraftInterface):
    def getType(self):
        print("Helicopter")


class VehicleInterface:
    def getType(self):
        print("Helicopter")


class Car(VehicleInterface):
    def getType(self):
        print("Car")


class Truck(VehicleInterface):
    def getType(self):
        print("Truck")


class TransportInterface:
    def getTransport(self, type):
        pass


class VehicleFactory(TransportInterface):
    @staticmethod
    def getTransport(type):
        if type == "car":
            return Car()
        if type == "truck":
            return Truck()
        assert 0, "No transport"


class AircraftFactory(TransportInterface):
    @staticmethod
    def getTransport(type):
        if type == "plane":
            return Plane()
        if type == "helicopter":
            return Helicopter()
        assert 0, "No transport"


class CarrierFactory:
    @staticmethod
    def getCarrier(type):
        if type == "vehicle":
            return VehicleFactory()
        if type == "aircraft":
            return AircraftFactory()
        assert 0, "No transport"


aircraft = CarrierFactory.getCarrier("aircraft")
plane = aircraft.getTransport("plane")
plane.getType()

vehicle = CarrierFactory.getCarrier("vehicle")
car = vehicle.getTransport("car")
car.getType()
