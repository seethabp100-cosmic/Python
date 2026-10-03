class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def sound(self,sound):
        print(self.name+" make sound as "+sound)

class Cat(Animal):
    def __init__(self, name, isIndoor):
        
        self.name = name
        self.isIndoor = isIndoor

    def makesSound(self):
        return "meow"

cat = Cat("Lynx", False);
print(cat.name+" is_indoor:",cat.isIndoor)
print(cat.sound("meow"))


class Add:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return Add(self.a + other.a,self.b + other.b)

    def __repr__(self):
        return f"Add({self.a},{self.b})"

add1 = Add(2,2)
add2 = Add(5,2)
print(add1+add2)