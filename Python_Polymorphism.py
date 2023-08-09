
#Python Polymorphism 
'''
The word "polymorphism" means "many forms", and in programming
 it refers to methods/functions/operators with the same name 
 that can be executed on many objects or classes.
'''

#Function Polymorphism
#An example of a Python function that can be used on different objects is the len() function.

#String
#For strings len() returns the number of characters:

x = "laurie 70s show"

print(len(x))

#Tuple
#For tuples len() returns the number of items in the tuple:

laurie_got = ("kalso", "unk1", "unk2", "unk3" ,"------")

print(len(laurie_got))

#Dictionary
#For dictionaries len() returns the number of key/value pairs in the dictionary:

laurie_makking_out_Dictionary = {
    "boy_name" : "kalso",
    "in_van"   : "kalso_van",
    "year"     : "1977"
}

print(len(laurie_makking_out_Dictionary))




'''
Class Polymorphism
Polymorphism is often used in Class methods,
where we can have multiple classes with the same method name.

For example, say we have three classes: 
Car, Boat, and Plane, and they all have a method called move():
'''

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def move(self):
        print("Drive! a kalso van")

class Boat:
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail! like kalso makking out")

class Plane:
    def __init__(self, brand, model):
        self.model = model
        self.brand = brand

    def move(self):
        print("Fly! sex all night")

car1 = Car("Van", "70s junk kalso van")
boat1 = Boat("Man", "its fly on water")
plane1 = Plane("ATR 72", "Crashed in katmandu")   

for x in (car1, boat1, plane1):
    x.move()

#Look at the for loop at the end. Because of polymorphism we can execute the same method for all three classes.

#Example
#Create a class called Red and make Erik, laurie child classes of RED:

class REd:
    def __init__(self, son, daughter, wife):
        self.son = son
        self.daughter = daughter
        self.wife = wife

    def workplase(self):
        print("laurie is working in another place")    
        print("Erik got girl status from his father")

class Erik(REd):
    pass

class Laurie(REd):
    def workplase(self):
        print("parrty all night, sex together")

class wife(REd):
    def workplase(self):
        print("its one man, not two!")
        
erik1 = Erik("waching what laurie do", "laughing", "what Laurie do?")     
laurie1 = Laurie("godammmed", "she is working so hard with party and sex all together at night", "father")
wife1 = wife("what Laurie do?", "Laurie got one man , not two!", "godammmed")

for x in (erik1, laurie1, wife1):
    print(x.son)
    print(x.daughter)
    x.workplase()

'''
Child classes inherits the properties and methods from the parent class.

In the example above you can see that the Car class is empty, but it inherits brand, model, and move() from Vehicle.

The Boat and Plane classes also inherit brand, model, and move() from Vehicle, but they both override the move() method.

Because of polymorphism we can execute the same method for all classes.
'''