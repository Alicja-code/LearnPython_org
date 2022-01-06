# A Nested Function is a function defined inside another function.
# Nested functions can access the variables of the enclosing scope.
# However, at least in python, they are only readonly.
# The 'data_transmitter' function can access the 'message'.

def transmit_to_space(message):
    "This is the enclosing function"

    def data_transmitter():
        "The nested function"
        print(message)

    data_transmitter()


print(transmit_to_space("Test message"))


# One can use the "nonlocal" keyword explicitly with these variables in order to modify them
# Without the nonlocal keyword, the output would be "3 9",
# however, with its usage, we get "3 3", that is the value of the "number" variable gets modified.

def print_msg(number):
    def printer():
        "Here we are using the nonlocal keyword"
        nonlocal number
        number = 3
        print(number)

    printer()
    print(number)


print_msg(9)


# return the function object rather than calling the nested function within & call the function

def transmit_to_space(message):
    "This is the enclosing function"

    def data_transmitter():
        "The nested function"
        print(message)

    return data_transmitter


fun2 = transmit_to_space("Burn the Sun!")
fun2()



# an example of a nested function accessing a non-local variable.

def print_msg(msg):
    # This is the outer enclosing function

    def printer():
        # This is the nested function
        print(msg)

    printer()


# We execute the function
# Output: Hello
print_msg("Hello")


# Defining a Closure Function
# now the last line of the function print_msg() returns the printer() function instead of calling it

def print_msg(msg):
    # This is the outer enclosing function

    def printer():
        # This is the nested function
        print(msg)

    return printer  # returns the nested function


# Now let's try calling this function.
# Output: Hello
another = print_msg("Hello")
another()


# The print_msg() function was called with the string "Hello" and the returned function was bound to the name another.
# On calling another(), the message was still remembered although we had already finished executing the print_msg() function.


# Make a nested loop and a python closure to make functions to get multiple multiplication functions using closures.
# That is using closures, one could make functions to create multiply_with_5() or multiply_with_4() functions using closures.

# your code goes here
def multiplier_of(x):
    def multi(y):
        return x * y

    return multi


multiplywith5 = multiplier_of(5)
multiplywith5(9)

print(multiplywith5(9))


# The criteria that must be met to create closure in Python
# - a nested function (function inside a function).
# The nested function must refer to a value defined in the enclosing function.
# The enclosing function must return the nested function.

# When to use closures?
# - to avoid the use of global values and provides some form of data hiding.
# - When there are few methods (one method in most cases) to be implemented in a class,
# closures can provide an alternate and more elegant solution.
# - Decorators make an extensive use of closures as well.

# The values that get enclosed in the closure function can be found out.
# All function objects have a __closure__ attribute that returns a tuple of cell objects if it is a closure function.
# The cell object has the attribute cell_contents which stores the closed value. E.g.:
# >>> times3.__closure__[0].cell_contents
# 3

