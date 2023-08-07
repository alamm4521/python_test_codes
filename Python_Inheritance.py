'''
Python Inheritance
Python Inheritance
Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.
'''

'''
Create a Parent Class
Any class can be a parent class, so the syntax is the same as creating any other class:
'''

#Example
#Create a class named Person, with firstname and lastname properties, and a printname method:

print("Create a class named Person, with firstname and lastname properties, and a printname method:")

class person_005:
    def __init__(self, fname, lname):
         self.firstname = fname
         self.lastname = lname
         
    def printname(self):
         print(self.firstname, self.lastname)

##Use the Person class to create an object, and then execute the printname method:

x = person_005("Pam", "jaccky 70s topless mother")
x.printname()

'''
Create a Child Class
To create a class that inherits the functionality from another class, 
send the parent class as a parameter when creating the child class:
'''

#example
#Create a class named Student, which will inherit the properties and methods from the Person_005 class:

class Student(person_005):
     pass

#Note: Use the pass keyword when you do not want to add any other properties or methods to the class.

#Now the Student class has the same properties and methods as the Person class.

#Example
#Use the Student class to create an object, and then execute the printname method:

class Person_007:
     def __init__(self, fname, lname):
          self.firstname = fname
          self.lastname = lname
          
     def printname(self):
          print(self.firstname, self.lastname)

class Student(Person_007):
     pass

x = Student("Michael", "Kelso")
x.printname()               

#https://www.w3schools.com/python/python_inheritance.asp

#Add the __init__() Function

