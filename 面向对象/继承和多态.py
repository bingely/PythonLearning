
class Animal(object):
    def run(self):
        print('i am running ')


class Dog(Animal):
    pass;


d = Dog();
d.run();


print(isinstance(d, Dog))
print(isinstance(d, Animal))
