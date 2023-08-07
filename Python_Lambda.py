'''
Python Lambda

A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.

Syntax
lambda arguments : expression
The expression is executed and the result is returned:
'''

'''x = lambda a : a + 10
print(x(5))'''

#Lambda functions can take any number of arguments:

'''x = lambda a, b : a * b
print(x(5, 50))'''

#Summarize argument a, b, and c and return the result:

'''x = lambda a, b, c : a + b + c
print(x(4, 5, 7))'''

'''
Why Use Lambda Functions?
The power of lambda is better shown when you use them as an anonymous function inside another function.

Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

def myfunc(n):
  return lambda a : a * n
Use that function definition to make a function that always doubles the number you send in:'''


'''def my_function(n):
    return lambda a : a * n

mydoubler = my_function(2)

print(mydoubler(33))'''

#Or, use the same function definition to make a function that always triples the number you send in:

'''def my_function(n):
    return lambda a : a * n

mytripler = my_function(3)

print(mytripler(11))'''

#Or, use the same function definition to make both functions, in the same program:

def myfunc(n):

    return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

