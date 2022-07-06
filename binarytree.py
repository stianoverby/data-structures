class Binarytree:

    def __init__(self, data, parent=None):

        self.data = data
        self.parent = parent

        self.left_child = None
        self.right_child = None


    '''
    Accesor methods
    ''' 
    def get_value(self):
        return self.data
    
    def get_parent(self):
        return self.parent
    
    def get_left(self):
        return self.left_child
    
    def get_right(self):
        return self.right_child

    def get_children(self):
        children = []

        if self.get_left():
            children.append(self.get_left())

        if self.get_right():
            children.append(self.get_right())
    
        return children

    '''
    Query methods
    '''
    # Test wether node v is internal
    def is_internal(self):
        return (self.get_left() is not None) or (self.get_right() is not None)

    # Test wether node v is a leaf
    def is_external(self):
        return not self.get_left() and not self.get_right()

    # Test wether node v is the main root
    def is_root(self):
        return self.get_parent() is None

    
    '''
    Generic methods
    '''

    def insert(self, data):

        # If data is smaller than current node, insert to left
        if data < self.get_value():

            # Left node exists, make new call on left node
            if self.get_left():
                self.get_left().insert(data)

            # Left node does not exist, create new node
            else:
                self.left_child = Binarytree(data, self)

        # If data is larger than or equal to current node, insert to right
        else:
            # Right node exists, make new call on right node
            if self.get_right():
                self.get_right().insert(data)
            # Right node does not exist, create new node
            else:
                self.right_child = Binarytree(data, self)

    def size(self):
        return 1 + sum([child.size() for child in self.get_children()]) 

    # Return a list of all elements in the tree    
    def elements(self):
        lst = [self.get_value()]

        for child in self.get_children():
            lst.extend(child.elements())

        return lst

    # Returns a set of all the nodes in the tree
    def positions(self):

        S = {self}
        children = self.get_children()

        if children:
            for child in children:
                S = S.union(child.positions())

        return S