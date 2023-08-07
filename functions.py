'''
Python Functions

A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result.
'''

#creating my_function with def keyword:
'''
def my_function():
    print("hello its fucking function")

my_function()
'''
'''
def my_function(fname):
    print(fname + " ref")

my_function("a0")
my_function("s1")
my_function("z1")    
'''

'''def my_function(x, y):
    print(x + " fuck " + y)

my_function("q1", "r1")
'''

'''def my_function(*fuck):
        print("this is a new fucking object " + fuck[2])

my_function("q1", "q2", "q3")'''

#Keyword Arguments

'''def my_function(q1, q2, q3):
    print("last fucking token " + q3 )

my_function(q1 = "penis", q2 = "bikini", q3 = "topless")'''

#Arbitrary Keyword Arguments, **kwargs

'''def my_function(**tv):
    print("this tv name " + tv['tv_name'])

my_function(tv_model = "lg", tv_name = "lg100101010")'''

#Default Parameter Value

'''def my_function(fifa_country = "USA"):
    print("world cup winner " + fifa_country)

my_function("Sweden")
my_function("India")
my_function()
print("If we call the function without argument, it uses the default value:")
my_function("Brazil") 
'''

#Passing a List as an Argument

'''def my_function(food):
    for x in food:
        print(x)
        #return x

arr = ["apple", "banana", "cherry"]

my_function(arr)
'''

'''#Return Values
#To let a function return a value, use the return statement:

def my_function(x):
    return 2 * x

The pass Statement
function definitions cannot be empty,
but if you for some reason have a function definition with no content,
put in the pass statement to avoid getting an error.

def my_function_pass():
    pass

print(my_function(4))
print(my_function(6))
print(my_function(8))
'''

'''
Recursion
Python also accepts function recursion, which means a defined function can call itself.

Recursion is a common mathematical and programming concept. It means that a function calls itself. 
This has the benefit of meaning that you can loop through data to reach a result.

The developer should be very careful with recursion as it can be quite easy to slip into writing a function 
which never terminates, or one that uses excess amounts of memory or processor power. However,
 when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.

In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). 
We use the k variable as the data, which decrements (-1) every time we recurse. 
The recursion ends when the condition is not greater than 0 (i.e. when it is 0).

To a new developer it can take some time to work out how exactly this works,
best way to find out is by testing and modifying it.
'''

'''def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)'''


def my_function(k):
    count = 0
    for x in range(k):
       result = k + my_function(k-1)
       print(result)
       count += 1
    else:
       result = 0
    print("count")
    print(count)
    return result

print("\n\nRecursion myfunction Example Results")

my_function(5)

       

    
  


