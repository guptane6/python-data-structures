########################################################################
#   Neha Gupta
#   Set.py
#   Google Jump
#   Under supervision of Laura Beth Lincoln
#   Implementation of the set data structure from a python list, and
#   assuming that we only have array index access. A collection of values that's
#   undordered and has no repeats
#########################################################################

class Set:
    def __init__(self):
        '''
        Define a node for the linked list, with just a data item and a pointer
        to the next node
        '''
        self.list = list()
    def __str__(self):
        '''Print the items in the set'''
        thestring = ""
        for items in self.list:
            thestring = thestring + "|" + str(items) + "| "
        return thestring
    def __repr__(self):
        '''Display the items in the set'''
        thestring = ""
        for items in self.list:
            thestring = thestring + "|" + str(items) + "| "
        return thestring
    def insert(self, data):
        '''Inserts one item. Returns true for successful insert. Returns
        false if the item already exists and could not be inserted'''
        for items in self.list:
            if (items == data):
                return 0
        self.list.append(data)
        return 1
    def delete(self, data):
        '''Deletes one item your data. Returns true for successful delete.
        Returns false if the item doesn't exist in the Set'''
        for items in self.list:
            if (items == data):
                x.remove(items)
                return 1
        return 0
    def search(self, data):
        '''Looks for your data and returns true or false if found'''
        for items in self.list:
            if (items == data):
                return 1
        return 0
    def intersection(self, other):
        '''Returns stuff in both sets'''
        intersection = Set()
        for items in self.list:
            for seconditems in other.list:
                if items == seconditems:
                    intersection.insert(items)
                break
        return intersection
    def union(self, other):
        '''Returns all the stuff'''
        union = Set()
        for items in self.list:
            union.insert(items)
        for items2 in other.list:
            union.insert(items2)
        return union
    def complement(self, other):
        '''Returns stuff only in one set'''
    def subset(self, other):
        '''Returns true if one is subset of other'''
