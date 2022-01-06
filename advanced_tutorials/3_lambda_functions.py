# Write a program using lambda functions to check if a number in the given list is odd.
# Print "True" if the number is odd or "False" if not for each element.

l = [2, 4, 7, 3, 14, 19]
lam = lambda i: True if (i % 2) == 0 else False

for i in l:
    print(lam(i))
