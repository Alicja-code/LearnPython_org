# In the exercise below, use the given lists to print out a set containing all the participants from event A
# which did not attend event B.

a = ["Jake", "John", "Eric"]
b = ["John", "Jill"]

a = set(a)
b = set(b)
print(a.difference(b))
