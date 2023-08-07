
'''
Python Arrays

Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.

Arrays
Note: This page shows you how to use LISTS as ARRAYS, however, to work with arrays in Python you will have to import a library, like the NumPy library.


'''

# array example

'''safe_sex = ["condom", "sex education", "van", "healty penis"]

print(safe_sex)'''

'''What is an Array?
An array is a special variable, which can hold more than one value at a time.

If you have a list of items (a list of car names, for example), storing the cars in single variables could look like this:

car1 = "Ford"
car2 = "Volvo"
car3 = "BMW"
However, what if you want to loop through the cars and find a specific one? And what if you had not 3 cars, but 300?

The solution is an array!

An array can hold many values under a single name, and you can access the values by referring to an index number.'''


'''
Access the Elements of an Array
You refer to an array element by referring to the index number.
'''

'''safe_sex = ["condom", "sex education", "van", "healty penis"]

x = safe_sex[0]

print(x)'''

#Modify the value of the first array item:

'''safe_sex = ["condom", "sex education", "van", "healty penis"]

safe_sex[0] = "dotted condom"

print(safe_sex)'''

'''
The Length of an Array
Use the len() method to return the length of an array (the number of elements in an array).

Example
Return the number of elements in the cars array:
'''

'''safe_sex = ["condom", "sex education", "van", "healty penis"]

print(len(safe_sex))
print("Note: The length of an array is always one more than the highest array index. safe_sex[4] out of range")'''


'''
Looping Array Elements
You can use the for in loop to loop through all the elements of an array.

Example
Print each item in the cars array:
'''

'''safe_sex = ["condom", "sex education", "van", "healty penis"]

for x in safe_sex:

    print(x)'''

'''
Adding Array Elements
You can use the append() method to add an element to an array.

Example
Add one more element to the cars array:
'''    

safe_sex = ["condom", "sex education", "van", "healty penis"]

safe_sex.append("vigina")

print(safe_sex)

'''
Removing Array Elements
You can use the pop() method to remove an element from the array.

Example
Delete the second element of the cars array:
'''

#this remove vigina

safe_sex.pop(4)

print(safe_sex)

'''
You can also use the remove() method to remove an element from the array.

Example
Delete the element that has the value "Volvo":
'''
#this remove "healty penis"
safe_sex.remove("healty penis")

print(safe_sex)

#Note: The list's remove() method only removes the first occurrence of the specified value.

#Python List copy() Method

#copy safe_sex in x array

safe_sex = ["condom", "sex education", "van", "healty penis"]

x = safe_sex.copy()

print(x)

#Python List count() Method

safe_sex = ["condom", "sex education", "van", "healty penis", "van"]

x = safe_sex.count("van")

print(x)

safe_sex_male = ["condom", "sex education", "van"]
safe_sex_female = ["must condom", "sex education", "-------"]
#safe_sex = []
safe_sex.extend(safe_sex_male)
safe_sex.extend(safe_sex_female)

print(safe_sex)

#Python List index() Method

# get posison van in safe_sex array

x = safe_sex.index("van")

print(x)

#Python List insert() Method
#insert calso in safe_sex array

safe_sex.insert(2, "calso")

print(safe_sex)

'''
Definition and Usage
The insert() method inserts the specified value at the specified position.

Syntax
list.insert(pos, elmnt)
Parameter Values
Parameter	Description
pos	    Required. A number specifying in which position to insert the value
elmnt	Required. An element of any type (string, number, object etc.)
'''

#Python List reverse() Method

#Reverse the order of the safe_sex array list

print(safe_sex)
print("revarce")
safe_sex.reverse()
print(safe_sex)

#Python List sort() Method

print("Python List sort() Method")

safe_sex = ["condom", "sex education", "van", "healty penis"]

print(safe_sex)

safe_sex.sort()

print(safe_sex)

'''
Definition and Usage
The sort() method sorts the list ascending by default.

You can also make a function to decide the sorting criteria(s).

Syntax
list.sort(reverse=True|False, key=myFunc)
Parameter Values
Parameter	Description
reverse	Optional. reverse=True will sort the list descending. Default is reverse=False
key	Optional. A function to specify the sorting criteria(s)
'''

#Sort the list descending:

print("Sort the list descending:")

safe_sex = ["condom", "sex education", "van", "healty penis"]

safe_sex.sort(reverse=True)

print(safe_sex)

#Sort the list by the length of the values:

print("Sort the list by the length of the values:")

# A function that returns the length of the value:
def myFunc(e):
    return len(e)

safe_sex = ["condom", "sex education", "van", "healty penis"]

safe_sex.sort(key=myFunc)

print(safe_sex)

#Example
#Sort a list of dictionaries based on the "year" value of the dictionaries:
print("Example Sort a list of dictionaries based on the year value of the dictionaries:")

def myFunction(e):
    return e["year"]

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]    

cars.sort(key = myFunction)

print(cars)


'''
Example
Sort the list by the length of the values and reversed:
'''

# A function that returns the length of the value:

def myFunc1(e):
    return len(e)

safe_sex = ["condom", "sex education", "van", "healty penis"]

print(safe_sex)

safe_sex.sort(reverse=True, key=myFunc1)

print(safe_sex)