from visitor import visitor

class Animal:
  def accept(self, visitor):
    visitor.visit(self)


class Lion(Animal): pass
class Tiger(Animal): pass
class Bear(Animal): pass

class ZooVisitor(object):
    def visit(self, animal):
        if isinstance(animal, Lion):
            print("Lions")
        elif isinstance(animal, Tiger):
            print("tigers")
        elif isinstance(animal, Bear):
            print("and bears, oh my!")


visitor = ZooVisitor()

lion = Lion()
visitor.visit(lion)


tiger = Tiger()
visitor.visit(tiger)


bear = Bear()
visitor.visit(bear)
