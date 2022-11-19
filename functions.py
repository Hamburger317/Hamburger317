# Functions are reusable pieces of code
# Many developers use them to divide a bigger program into much smaller pieces

def print_hello():
    print("Hello!!")


print_hello()  # Output: Hello!!


# Functions can use parameters, which act like inputs

def greet(name):
    print(f"Hello, {name}!!")


greet("Amber")  # Output: Hello, Amber


# But functions are at their most useful when they return values
# The return statement exits and returns the functions value


def add(a, b):
    return a + b


print(add(10, 15))  # Output: 25


# Params act like variables that the developer or user supplies
# Of course there is more advanced features of functions like
# keyword arguments. But those are pretty complex for someone at your level

# Functions can have almost anything, but they cannot use variables defined in a function
# outside the function
# Keep scope in mind when making programs!


def def_var():
    var = 15


try:
    def_var()
    print(var)
except NameError as e:
    print(f"{e}: Using local variable from def_var "
          f"leads to an error due to scope")


# You can avoid this by returning the variable or using a...
# GLOBAL VARIABLE........

def def_var_glob():
    global glob_var
    glob_var = 15


def_var_glob()
print(glob_var)


# this is very discouraged throughout the community
# do NOT use globals unless you really have to.
# Ralsei uses globals, don't be a Ralsei!

# You can make any program without globals, use params and return statements!
# functions can also be annotated which helps IDEs alot.
# functions can also have optional values

# Here we can see that this function takes param with int type and returns an int
def func_with_annotations(param: int) -> int:
    print(param)
    return param


# by default this function squares a
def exp(a: float or int, power=2):
    return a ** power


print(exp(2))  # squares 2
print(exp(2, power=3))  # raises 2 to the power of 3
print(exp(2, power=4))  # raises 2 to the power of 4

# TL;DR, functions are a powerful tool that lets us divide a program into smaller programs
# they can contain hundreds of lines of instructions or a simple one liner
# they allow us to reuse code and build libs
# they can take params and return values

# Of course there is way more to like about these guys, like Lambdas and keyword args,
# but they are really useful. Most programs are made up of hundreds of them.
