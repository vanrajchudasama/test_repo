# Encapsulation


class A:

    def __init__(self):
        self.name='vanraj'
        self.age=25
    def show(self):
        print('name = ',self.name)
        print('Age = ',self.age)

class Fruit:
    types = 'Fruit'
    def __init__(self,name,weight,price):
        self.name=name
        self.weight=weight
        self.price=price
    @classmethod
    def show(cls):
        print(' Type --> ',cls.types)
    def info(self):
        
        
        print(' Name --> ',self.name)
        print(' Weight --> ',self.weight)
        print(' Price --> ',self.price)

apple=Fruit('apple',20,100)
banana=Fruit('banana',50,20)

apple.show()
apple.info()
banana.info()

