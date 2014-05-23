########################################################################
#   Neha Gupta
#   Google Jump
#   Under supervision of Laura Beth Lincoln
#   Implementation of the Stack data structure from a python list, and
#   assuming that we only have array index access
#   Stacks are last in first out (LIFO), where the last element added is the
#   first element removed 
#########################################################################

class Stack:
    def __init__(self):
        '''
        Define a stack with only a list
        '''
        self.list = list()
        self.numitems = 0
    def __str__(self):
        '''Print one node'''
        thestring = ""
        for items in self.list:
            thestring = thestring + "|" + str(items) + "| "
        return thestring 
    def __repr__(self):
        '''Print one node'''
        thestring = ""
        for items in self.list:
            thestring = thestring + "|" + str(items) + "| "
        return thestring
    def push(self, node):
        '''Put a node into the stack'''
        self.list.append(node)
        self.numitems += 1
    def pop(self):
        '''Pop a node from the stack'''
        self.list.pop(self.numitems-1)
        self.numitems -= 1

        #Um. I guess I'm not sure what I was to do for push and pop to work
        #With array indeces instead of the built-ins...stuff like self.list[0] = node
        #errors out...
