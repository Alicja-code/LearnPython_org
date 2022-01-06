# Fill in the foo and bar functions so they can receive a variable amount of arguments (3 or more)
# The foo function must return the amount of extra arguments received.
# The bar must return True if the argument with the keyword magicnumber is worth 7, and False otherwise.

# edit the functions prototype and implementation
def foo(a, b, c, *args):
    print(type(args))
    return len(args)


def bar(a, b, c, **kwargs):
    print(type(kwargs))
    if kwargs.get("magicnumber") == 7:
        # kwargs["magicnumber"] == 7
        result = True
    else:
        result = False
    return result


# test code
if foo(1, 2, 3, 4) == 1:
    print("Good.")
if foo(1, 2, 3, 4, 5) == 2:
    print("Better.")
if bar(1, 2, 3, magicnumber=6) == False:
    print("Great.")
if bar(1, 2, 3, magicnumber=7) == True:
    print("Awesome!")
