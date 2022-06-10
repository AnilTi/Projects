# Decorator is a modify or enhance functions without changing their definition.
# It acts as a wrapper for your original function.

def my_decorator(func):
    def wrapper(x,y):
        print("before function calling ")
        print(func.__name__,'=',func(x,y))
        print("after function calling")
    return wrapper

@my_decorator
def add(a,b):
    return a+b

@my_decorator
def sub(a,b):
    return a-b

@my_decorator
def mul(a,b):
    return a*b

@my_decorator
def div(a,b):
    return a/b

add(10,20)
sub(30,10)
mul(10,20)
div(20,10)
