###########################################################################
#   Neha Gupta
#   Class definition of a Doubly Linked List in Python
#   Google Jump
#   Supervised by: Laura Beth Lincoln
#   FIFO (First in, first out...the first thing you enter is the first thing
#   you take out
###########################################################################

class Queue:
    def __init__(self):
        '''
        Define a queue with only a list
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
        self.list.reverse()
        self.list.pop()
        self.list.reverse()
        self.numitems -= 1

        #Um. I guess I'm not sure what I was to do for push and pop to work
        #With array indeces instead of the built-ins...stuff like self.list[0] = node
        #errors out...
