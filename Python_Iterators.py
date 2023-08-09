
#Python Iterators (with 70s show)

'''
Python Iterators
An iterator is an object that contains a countable number of values.

An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.

Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().
'''

'''
Iterator vs Iterable
Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.

All these objects have a iter() method which is used to get an iterator:
'''

mytuple = ("red", "bob", "pam", "kitty", "midiz")

miit = iter(mytuple)

print(next(miit))
print(next(miit))
print(next(miit))
print(next(miit))
print(next(miit))

#Even strings are iterable objects, and can return an iterator:

#Example
#Strings are also iterable objects, containing a sequence of characters:
print("#Strings are also iterable objects, containing a sequence of characters:")
mystr = "bananan"

miit = iter(mystr)

print(next(miit))
print(next(miit))
print(next(miit))
print(next(miit))
print(next(miit))
print(next(miit))
print(next(miit))

'''
Looping Through an Iterator
We can also use a for loop to iterate through an iterable object:
'''

mytuple = ("pam", "bob", "red","hyde")

for x in mytuple:
    print(x)

'''
Example
Iterate the characters of a string:'''

mystr = "hi boys"

for x in mystr:
    print(x)

#The for loop actually creates an iterator object and executes the next() method for each loop.    

'''
Create an Iterator
To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.

As you have learned in the Python Classes/Objects chapter, all classes have a function called __init__(), which allows you to do some initializing when the object is being created.

The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.

The __next__() method also allows you to do operations, and must return the next item in the sequence.
'''

'''
Example
Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.):
'''

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x    

myclass = MyNumbers()

myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

'''
StopIteration
The example above would continue forever if you had enough next() statements, or if it was used in a for loop.

To prevent the iteration from going on forever, we can use the StopIteration statement.

In the __next__() method, we can add a terminating condition to raise an error if the iteration is done a specified number of times:
'''

class MyNumbers_001:
    def ___iter__(self):
        self.a = 1
        return self
        
    def __next__(self):
        if self.a <= 5:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass_001 = MyNumbers_001()
myiter_001 = iter(myclass) 

for x in myiter_001:
    print(x)