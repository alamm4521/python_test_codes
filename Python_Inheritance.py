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

'''
Add the __init__() Function
So far we have created a child class that inherits the properties and methods from its parent.

We want to add the __init__() function to the child class (instead of the pass keyword).
'''

#Note: The __init__() function is called automatically every time the class is being used to create a new object.

'''
Add the __init__() Function
So far we have created a child class that inherits the properties and methods from its parent.

We want to add the __init__() function to the child class (instead of the pass keyword).

Note: The __init__() function is called automatically every time the class is being used to create a new object.

Example
Add the __init__() function to the Student class:

class Student(Person):
  def __init__(self, fname, lname):
    #add properties etc.
When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.

Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.

To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
'''

class Person008:
     def __init__(self, fname, lname):
          self.firstname = fname
          self.lastname  = lname

     def printname(self):
          print(self.firstname, self.lastname)

class Student_001:
     def __init__(self, fname, lname):
          Person008.__init__(self, fname, lname)

x = Student("Michael", "Kelso")
x.printname

'''
Now we have successfully added the __init__() function, 
and kept the inheritance of the parent class, and we are ready to 
add functionality in the __init__() function.
'''

#Example Add a year parameter, and pass the correct year when creating objects:

class Person_009:
     def __init__(self, fname, lname):
          self.firstname = fname
          self.lastname = lname

     def printname(self):
          print(self.firstname, self.lastname)
     
class Student002(Person_009):
     def __init__(self, fname, lname, year):
          super().__init__(fname, lname)
          self.graduationyear = year

print("What year did they graduate in That 70s Show?")
print("In Season 5, Episode 25 (Celebration Day), their tassels show 78 (for Class of 1978).")
x = Student002("Michael", "Kelso", 1978)  
print(x.graduationyear)

class Persion_010:
     def __init__(self, fname, lname):
          self.firstname = fname
          self.lastname  = lname
          
     def printname(self):
          print(self.firstname, self.lastname)
          
class Student_003(Persion_010):
     def __init__(self, fname, lname, year):
          super().__init__(fname, lname)
          self.graduationyear = year

     def welcome(self):
          print("Wellcome", self.firstname, self.lastname, "THAT 70S SHOW CLASS OF ", self.graduationyear)

x = Student_003("Michael", "Kelso", 1978)
x.welcome()
          

