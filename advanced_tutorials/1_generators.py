# Write a generator function which returns the Fibonacci series.
# They are calculated using the following formula:
# The first two numbers of the series is always equal to 1,
# and each consecutive number returned is the sum of the last two numbers.
# Hint: Can you use only two variables in the generator function?
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...


# import random
#
#
# def lottery():
#     # returns 6 numbers between 1 and 40
#     for i in range(6):
#         yield random.randint(1, 40)
#
#     # returns a 7th number between 1 and 15
#     yield random.randint(1, 15)
#
#
# for random_number in lottery():
#     print("And the next number is... %d!" % (random_number))


# fill in this function
# def fib():
#     pass
# this is a null statement which does nothing when executed, useful as a placeholder.

def fib():
    seq = [0, 1]
    while True:
        yield seq[-1]
        seq.append(sum(seq[-2:]))


# def fib():
#     a, b = 1, 1
#     while 1:
#         yield a
#         a, b = b, a + b


# testing code
import types

if isinstance(fib(), types.GeneratorType):
    print(type(fib))
    print("Good, The fib function is a generator.")
    print(fib())

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break
