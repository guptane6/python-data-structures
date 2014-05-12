########################################################################
#   Neha Gupta
#   Set.py
#   Google Jump
#   Under supervision of Laura Beth Lincoln
#   Implementation of the set data structure from a python list, and
#   assuming that we only have array index access. A collection of values that's
#   undordered and has no repeats
#########################################################################

from set import Set

x = Set()
x.insert(1)
x.insert(2)
x.insert(3)
x.insert(1)
print(x)

y = Set()
y.insert(1)
y.insert(10)
y.insert(11)

print(x.intersection(y))
print(x.union(y))
