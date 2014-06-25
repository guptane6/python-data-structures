##############################################
#   Binary Search Tree Python Implementation
#   Neha Gupta
#   Google Jump
#   Under direction of Laura Beth Lincoln
##############################################

class node:
    def __init__(self, data = None, is_root = False):
        self.data = data
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.data)
    def __repr__(self):
        return str(self.data)

    
########################################################################
#   Some random recursive functions that wouldn't go in the actual class
#########################################################################
def insert_recursive(newData, parent):
    if parent == None:
        parent = node(newData)
    elif (newData < parent.data):
        if parent.left == None:
            parent.left = node(newData)
        else:
            insert_recursive(newData, parent.left)
    else:
        if parent.right == None:
            parent.right = node(newData)
        else:
            insert_recursive(newData, parent.right)

def search_recursive(data, parent):
    print("data: ", data)
    print("parent: ", parent.data)
    if data < parent.data:
        print(parent.data)
        if parent.left == None:
            return "Node not found"
        elif parent.left.data == data:
            print(parent.left.data)
            return parent
        else:
            parent = search_recursive(data, parent.left)
            print("here")
            return parent
    else:
        if parent.right.data == None:
            return "Node not found"
        elif parent.right.data == data:
            return parent
        else:
            parent = search_recursive(data, parent.right)
            return parent
    print("uhoh")
            
def preorder_recursive(root):
    if (root != None):
        print(str(root) + " ")
        preorder_recursive( root.left)
        preorder_recursive(root.right)

def inorder_recursive(root):
    if (root != None):
        inorder_recursive(root.left)
        print(str(root.data) + " ")
        inorder_recursive(root.right)
        
def postorder_recursive(root):
    if (root != None):
        postorder_recursive(root.left)
        postorder_recursive(root.right)
        print(str(root) + " ")

######################################################################
#   Class BST
#######################################################################
class BST:
    def __init__(self, array = None):
        print(array)
        self.root = node(None, True)
        if type(array) == list:
            for i in array:
                #print("i:",i)
                #print("array:",array[i])
                if i == 0:
                    self.root = node(i, True)
                else:
                    self.insert(i)
                
    def __str__(self):
        return str(self.root.data) + " " + str(self.root.left) + " " + str(self.root.right)
    def __repr__(self):
        return str(self.root.data) + " " + str(self.root.left) + " " + str(self.root.right)

    def insert(self, newData):
        if self.root.data == None:  #The tree is currently empty, adding root
            self.root = node(newData, True)
        else:
            parent = self.root
            insert_recursive(newData, parent)
            
    def preorder(self):
        preorder_recursive(self.root)
            
    def inorder(self):
        inorder_recursive(self.root)

    def postorder(self):
        postorder_recursive(self.root)
        
    def search(self, data):
        root = self.root
        while (root != None):
            if (root.data == data):
                return root
            else:
                if root.data < data:
                    root = root.right
                else:
                    root = root.left
        return "Node does not exist"

    def delete(self, data):
        #TODO: fix 2 leaf delete, root deletion, and tree with 1 or 2 leaves only
        # this code confused me: http://en.wikipedia.org/wiki/Binary_search_tree
        print("in delete")
        if data != self.root.data:
            parent = search_recursive(data, self.root)
            print("parent: ", parent)

        if (parent.left != None and parent.left.data == data):
            found = parent.left
            print("found the 1")
        else:
            found = parent.right

        if found.left == None:
            if found.right == None:     #deleting a node with no children
                if parent.left is found:
                    parent.left = None
                else:
                    parent.right = None
                del found
            else:
                if parent.left is found:        #deleting node with right children
                    parent.left = found.right
                else:
                    parent.right = found.right
                del found
        else:
            if found.right == None:     #deleting a node with left children
                if parent.left is found:
                    parent.left = found.left
                else:
                    parent.right = found.left
                del found
            else:                       #deleting a node with 2 children
                maxNode = found.left
                maxParent = found
                while (True):
                    if (maxNode.right != None):
                        maxParent = maxNode
                        maxNode = maxNode.right
                    else:
                        break
                found.data = maxNode.data
                if maxNode.left != None:
                    maxParent.right = maxNode.left  #but this would only copy one node, not subtree
                    self.delete(maxNode.left)       #uhh why doesn't this call go?                    
                    print("here")
                del maxNode
        return "Node deleted"
