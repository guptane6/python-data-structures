###########################################################################
#   Neha Gupta
#   Implementation of Linked List in Python
#   Google Jump
#   Supervised by: Laura Beth Lincoln
###########################################################################

from linkedList import node
from linkedList import linked_list

x = linked_list()
x.insert(1)
x.insert("2")
print("Our initial list, after inserting 2 things")
print(x)

x.insert(5.0, 1)
print("Now the list after inserting 5.0 at the first spot")
print(x)

x.insert(3, 2)
print("Now the list after inserting 3 at the 2nd spot")
print(x)

y = node(3)
x.insert(y)
print("Now the list after inserting a node, {}, at the end".format(y))
print(x)

x.delete("2")
print("The list after deleting 2:")
print(x)

x.delete(2, True)
print("The list after deleting the second thing in it:")
print(x)

y = x.search(5.0)
print("Can 5.0 be found in the list?")
print(y, "(So yes. That is the node.)")

y = x.search(99)
print("Can 99 be found in the list?")
print(y)

y = x.search(2, True)
print("What is the second thing in the list?")
print(y)
