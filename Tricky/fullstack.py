def make_counter():
    count =0
    def counter():
        nonlocal count
        count=count+1
        return count
    return counter

def decorator_fn(func):
    def wrapper():
        print("Inside Wrapper")
    return wrapper
def simple_function():
    print("simple function")
simple_function_result = simple_function(decorator_fn)


def make_pretty(func):

    def inner():
        print("I got decorated")
        func()
    return inner

@make_pretty
def ordinary():
    print("I am ordinary")

ordinary()  


def make_pretty(func):
    # define the inner function 
    def inner():
        # add some additional behavior to decorated function
        print("I got decorated")

        # call original function
        func()
    # return the inner function
    return inner

# define ordinary function
def ordinary():
    print("I am ordinary")
    
# decorate the ordinary function
decorated_func = make_pretty(ordinary)

# call the decorated function
decorated_func()