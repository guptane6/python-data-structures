###########################################################################
#   Neha Gupta
#   Class definition of Linked List in Python
#   Google Jump
#   Supervised by: Laura Beth Lincoln
###########################################################################

class node:
    def __init__(self, data = None, is_head = False):
        '''
        Define a node for the linked list, with just a data item and a pointer
        to the next node
        '''
        self.data = data
        self.next = None
    def __str__(self):
        '''Print one node'''
        return str(self.data)
    def __repr__(self):
        '''Print one node'''
        return str(self.data)


class linked_list:
    def __init__(self):
        '''
        Initialize a linked list with a head node, with data "head". Note that
        the initial number of nodes is 0, the header does not count as  a node
        '''
        self.head = node("Head", True)
        self.numNodes = 0

    def __str__(self):
        '''
        Creates a string form all of the nodes' data to print
        '''
        thestring = ""
        curr = self.head
        while (curr != None):
            thestring = thestring + "|" + str(curr.data) + "|" + " --> "
            curr = curr.next
        return thestring + "None"

    def __repr__(self):
        '''
        Creates a string from all of the nodes' data to print
        '''
        thestring = ""
        curr = self.head
        while (curr != None):
            thestring = thestring + "|" + str(curr.data) + "|" + " --> "
            curr = curr.next
        return thestring + "None"

    def insert(self, newNode, position = None):
        '''
        Function Insert
        Purpose: To allow inserting some data into the linked list, either
        at the end or at a specific position, or after a given node
        Parameters: data for new node, and optional position/node
        Return: boolean for successful or unsuccesful insert
                An unsuccessful insert would be an invalid integer for
                position
        '''
        newNode = node(newNode)
        curr = self.head
        if (type(position) == node):   #after an existing node, O(1)
            curr = position
            newNode.next = curr.next
            curr.next = newNode
            self.numNodes += 1
            return 1
        elif (type(position) == int):    #at a given position
            #worst case O(N)
            #best case O(1)
            counter = 1
            if position < self.numNodes and position > 0:
                while (counter != position):
                    curr = curr.next
                    counter += 1
                newNode.next = curr.next
                curr.next = newNode
                self.numNodes += 1
                return 1
                
        elif (position == None):  #default insert is at the end, O(N)
            while True:
                if curr.next == None:
                    curr.next = newNode
                    self.numNodes += 1
                    return 1
                else:
                    curr = curr.next
        else:
            return 0
                
                
    def delete(self, item, position = False):
        '''
        Function Delete
        Purpose: To allow deleting some data from the linked list
        Parameters: "position", which indicates whether "item" is a item to
                    find and delete or an integer position to delete at
        Return: boolean for successful or unsuccesful delete
                An unsuccessful delete would be data that doesn't exist in the
                linked list
        '''
        if (position == False):
            if (type(item) == node):
                item = item.data
            curr = self.head
            while (curr.next != None):      #looping to find the data
                if (curr.next.data == item):
                    curr.next = curr.next.next
                    return 1
                curr = curr.next
            return 0
        elif (position == True and type(item) == int and item <= self.numNodes\
              and item > 0):
            print("here")
            curr = self.head
            counter = 0
            while (curr.next != None):
                if (counter + 1 == item):
                    curr.next = curr.next.next
                    return 1
                counter += 1
                curr = curr.next
        else:   #so position is invalid
            return 0
            #curr = self.head
            

    def search(self, item, position = False):
        '''
        Function Search
        Purpose: To find the node which has a certain element as it's data
        Parameter: boolean "position", which indicates whether "item" is data
                    to find and delete or an int position in the list to delete at
        Return: A node, which has that item, or a string indicating that the
                node couldn't be found
        '''
        if (position == False): #Finding the node which has the data in item
            curr = self.head    
            while (curr.next != None):
                curr = curr.next
                if (curr.data == item):
                    return curr
            return "Node not found"
        elif (position == True and type(item) == int and item <= self.numNodes\
                 and item > 0):    #Finding the node at this position
            curr = self.head
            counter = 0
            while (counter < item):
                curr = curr.next
                counter += 1
            return curr
                    
        else:   #Position invalid
            return "Node not found"
