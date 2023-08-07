'''
Python Classes and Objects
Python Classes/Objects
Python is an object oriented programming language.

Almost everything in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects.

Create a Class
To create a class, use the keyword class:
'''

#Create a class named MyClass, with a property named x:

print("Create a class named MyClass, with a property named x:")

'''class Myclass:
    x = 5

print(Myclass)    '''

'''
Create Object
Now we can use the class named MyClass to create objects:

Example
Create an object named p1, and print the value of x:
'''

'''class Myclass_1:
    x = 5

p1 = Myclass_1()

print(p1.x)'''

'''
The __init__() Function
The examples above are classes and objects in their simplest form, and are not really useful in real life applications.

To understand the meaning of classes we have to understand the built-in __init__() function.

All classes have a function called __init__(), which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:
'''

'''#Example
#Create a class named Person, use the __init__() function to assign values for name and age:'''

'''print("Example Create a class named Person, use the __init__() function to assign values for name and age:")'''

'''class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("jone", 36)

print(p1.name)
print(p1.age)

p2 = Person("jakccy", 14)

print(p2.name)
print(p2.age)'''

'''
The __str__() Function
The __str__() function controls what should be returned when the class object is represented as a string.

If the __str__() function is not set, the string representation of the object is returned:
'''

'''Example
The string representation of an object WITHOUT the __str__() function:'''

'''print("Example The string representation of an object WITHOUT the __str__() function:")'''

'''class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

try:
    print(p1)
except:
    print("<__main__.Person object at 0x15039e602100>")'''


#Example
#The string representation of an object WITH the __str__() function:

class person001:
   def __init__(self, name, age):
      self.name = name
      self.age  = age

   def __str__(self):
       return f"{self.name}({self.age})"
   
p_001 = person001("calso", "18")

print(p_001.name)
print(p_001.age)

print(p_001)

'''
Object Methods
Objects can also contain methods. Methods in objects are functions that belong to the object.

Let us create a method in the Person class:
'''

#Example
#Insert a function that prints a greeting, and execute it on the p1 object:

print("#Example #Insert a function that prints a greeting, and execute it on the p_002 object:")

class Person002:
   def __init__(self, name, age):
      self.name = name
      self.age  = age
      
   def myfunc(self):
      print("this is 70s show " + self.name)

p_002 = Person002("Fezz", 17)
p_002.myfunc()         

'''Note: The self parameter is a reference to the current instance of the class, 
and is used to access variables that belong to the class.'''

'''
The self Parameter
The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:
'''

'''
Example
Use the words mysillyobject and abc instead of self:
'''

print("Example Use the words mysillyobject and abc instead of self:")

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

p1.age = 455555

print(p1.age)

del p1.age

try:
    print(p1.age)
except:
   print("Traceback (most recent call last): AttributeError: 'Person' object has no attribute 'age'")    


del p1

try:
   print(p1)
except:
   print("Traceback (most recent call last): NameError: 'p1' is not defined")  


class Person_004:
  pass

# having an empty class definition like this, would raise an error without the pass statement
print(" having an empty class definition like this, would raise an error without the pass statement")


