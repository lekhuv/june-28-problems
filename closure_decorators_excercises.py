#Closures-Decorators Excercises

#Closure Excercise
#Using a closure, create a function, multiples_of(n) which we can use to
#create generators that generate multiples of n less than a given number.

# Multiplier of 3
from ast import arg
from msilib.schema import Class


def multiples_of(n):   
    def multiplier(i):
        j = 1        
        while ((j * n)< i):        
            yield j * n
            j+=1                         
    return multiplier
m3 = multiples_of(3)
print(*m3(7))

m3_under30 = m3(30)
m7_under30 = multiples_of(7)(30)

print(type(m3_under30))
# output: <class 'generator'>

print(*m3_under30)
# output: 3 6 9 12 15 18 21 24 27

print(*m7_under30)
# output: 7 14 21 28
#----------------------------------------------------------------------

#Decorators Excercise 1
#@make_upper – make every letter of a string returned from the decorated
#function uppercase.

class upper_case:

  def __init__(self, original_function):
    self.original_function = original_function


  def __call__(self):
    # Code can be executed before the original function
    # print(f"'{self.original_function.__name__}' function execution will start now.")

    # Original function call with the upper cased argument
    result = self.original_function()

    # Code can be executed after the original function
    result = result.upper()
    return result

@upper_case
def hello_world():
    return 'hello young, good day!!'

print(hello_world()) # output: HELLO YOUNG, GOOD DAY!!
#-----------------------------------------------------------------------

#Decorators Excercise 2
#@print_func_name – print the name of the decorated function before
#executing the function.

class myfunction_decorator:

  def __init__(self, original_function):
    self.original_function = original_function


  def __call__(self):
    # Code can be executed before the original function
    print(f"{self.original_function.__name__} is running...")

    # Original function call with the upper cased argument
    result = self.original_function()

    # Code can be executed after the original function
    #result = result.replace("!","")
    return result

@myfunction_decorator
def my_func():
    print('Python is fun')

my_func() # output: my_func is running...
            #Python is fun
#----------------------------------------------------------------------
class myfunction_decoratorwithargs:
    def __init__(self, arg1):
        self.arg1 = arg1
    
    def __call__(self, foo, *args):
        def inner_func(*args,):
            return foo(*args)
        return inner_func

#Decoratos Excercise 3
#@give_name(name) – concatenate the given name at the end of a string
#returned from the decorated function.
@myfunction_decoratorwithargs("Theresa")
def greeting(*args):
    for arg in args:
        print(arg)
    return 'Hello'

print(greeting()) # output: Hello Theresa
#---------------------------------------------------------------------

#Decorators Excercise 4
#@print_input_type – print a data type of the input argument before
#executing the decorated function.
def computesquare(str_param):
    def inner_deco(func):
        def inner(x):
            print (str_param, ' of ', x)
            print ('The input data type of ', x ,' is ', type(x))
            return func(x)
        return inner
    return inner_deco

@computesquare('Find the Square')
def square(n):
    return n ** 2
  
print(square(3.5)) # output: The input data type is <class 'float'>
                    #12.25
#-------------------------------------------------------------------

#Decorators Excercise 5
#@check_return_type(return_type) – check if the return type of the
#decorated function is return_type and print the result before executing
#the function.

#pass in a string
def computesquare(str_param):
    def inner_deco(func):
        def inner(x):
            print (str_param, ' of ', x)
            print ('The result data type of ', x ,' is ', type(x ** 2))
            return func(x)
        return inner
    return inner_deco

@computesquare('Find the Square')
def square(n):
    return n ** 2

print(square(6)) # output: =========Error!!
                    #The return type is NOT <class 'str'>
                    #36

#pass in a float
@computesquare('Find the Square')
def square(n):
    return n ** 2

print(square(2.9)) # output: The return type is <class 'float'>
                    #8.41
#------------------------------------------------------------------------

#Decorators Excercise 6
#@execute_log – write a function execution log on the log file. (log below)

from datetime import datetime
def execute_log(func):
    def inner(*args):
        print(f"{str(datetime.now())}  {func.__name__}")
        return func(*args)
    return inner
    

@execute_log
def multiply(*nums):
    mult = 1
    for n in nums:
        mult *= n
    return mult

@execute_log
def hello_world():
    return 'hello world!!'

print(multiply(6, 2, 3)) # 36
print(hello_world()) # hello world!!
print(multiply(2.2, 4)) # 8.8
print(hello_world()) # hello world!!


#function_execution.log
#2020-05-01 13:55:53.059315 multiply
#2020-05-01 13:55:53.060312 hello_world
#2020-05-01 13:55:53.060314 multiply
#2020-05-01 13:55:53.060323 hello_world