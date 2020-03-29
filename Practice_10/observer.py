class Subscriber:
    def __init__(self, name):
        self.name = name
    def update(self, message):
        print('{} got message "{}"'.format(self.name, message))
        
class MealDelivery:
    def __init__(self):
        self.subscribers = set()
    def register(self, who):
        self.subscribers.add(who)
    def unregister(self, who):
        self.subscribers.discard(who)
    def dispatch(self, message):
        for subscriber in self.subscribers:
            subscriber.update(message)

delivery = MealDelivery()

bob = Subscriber('Bob')
alice = Subscriber('Alice')
john = Subscriber('John')

delivery.register(bob)
delivery.register(alice)
delivery.register(john)

delivery.dispatch("It's lunchtime!")

delivery.unregister(john)

delivery.dispatch("Time for dinner")