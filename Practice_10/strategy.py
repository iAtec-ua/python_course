class FlyWithRocket():
    def __init__(self):
        pass
    def fly(self):
        print ('FLying with rocket')

class FlyWithWings():
    def __init__(self):
        pass
    def fly(self):
        print ('FLying with wings')

class CantFly():
    def __init__(self):
        pass
    def fly(self):
        print ('I Cant fly')

class SuperDuck:
    def __init__(self):
        pass
    def setFlyingBehaviour(self, fly_strategy):
        self.fly_strategy = fly_strategy
    def perform_fly(self):
        self.fly_strategy.fly()

duck = SuperDuck()
#fly_behaviour = FlyWithRocket()
fly_behaviour = FlyWithWings()
duck.setFlyingBehaviour(fly_behaviour)
duck.perform_fly()