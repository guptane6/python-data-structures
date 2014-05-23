########################################################################
#   Neha Gupta
#   Map.py
#   Google Jump
#   Under supervision of Laura Beth Lincoln
#   Implementation of the map data structure from a python list, and
#   assuming that we only have array index access.
#########################################################################

class Map:
    def __init__(self):
        '''
        Define a node for the linked list, with just a data item and a pointer
        to the next node
        '''
        self.keys = list()
        self.numkeys = 0
        self.values = list()
    def __str__(self):
        '''Print the items in the set'''
        thestring = ""
        x = 0
        for x in range(self.numkeys):
            thestring = thestring + "|" + str(self.keys[x]) + ":" + str(self.values[x]) + "| "
        return thestring
    def __repr__(self):
        '''Display the items in the set'''
        thestring = ""
        x = 0
        for x in range(self.numkeys):
            thestring = thestring + "|" + str(self.keys[x]) + ":" + str(self.values[x]) + "| "
        return thestring
    def insert(self, key, value):
        self.numkeys += 1
        keyindex = 0
        for items in self.keys:
            if key == items:
                oldvalue = value
                if type(oldvalue) != list:
                    newvalue = list()
                    newvalue.append(oldvalue)
                    newvalue.append(value)
                    self.values[keyindex] = newvalue
                    return
                else:
                    newvalue = list()
                    for item in oldvalue:
                        newvalue.append(item)
                    newvalue.append(value)
                    self.values[keyindex] = newvalue
                    return
            keyindex += 1
        self.keys.append(key)
        self.values.append(value)
    def remove(self, key):
        
