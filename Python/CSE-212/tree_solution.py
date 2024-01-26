from types import DynamicClassAttribute


class BST:
    """
    Implement the Binary Search Tree (BST) data structure.  The Node 
    class below is an inner class.  An inner class means that its real 
    name is related to the outer class.  To create a Node object, we will 
    need to specify BST.Node
    """

    class Node:
        """
        Each node of the BST will have data and links to the 
        left and right sub-tree. 
        """

        def __init__(self, data):
            """ 
            Initialize the node to the data provided.  Initially
            the links are unknown so they are set to None.
            """
       
            self.data = data
            self.left = None
            self.right = None

   

    def __init__(self):
        """
        Initialize an empty BST.
        """
        self.root = None

    def __iter__(self):
        """
        Perform a forward traversal (in order traversal) starting from 
	    the root of the BST.  This is called a generator function.
        This function is called when a loop	is performed:

        for value in my_bst:
            print(value)

        """
        yield from self._traverse_forward(self.root)  # Start at the root
        
    def _traverse_forward(self, node):
        """
        Does a forward traversal (in-order traversal) through the 
        BST.  If the node that we are given (which is the current
        sub-tree) exists, then we will keep traversing on the left
        side (thus getting the smaller numbers first), then we will 
        provide the data in the current node, and finally we will 
        traverse on the right side (thus getting the larger numbers last).

        The use of the 'yield' will allow this function to support loops
        like:

        for value in my_bst:
            print(value)

        The keyword 'yield' will return the value for the 'for' loop to
	    use.  When the 'for' loop wants to get the next value, the code in
	    this function will start back up where the last 'yield' returned a 
	    value.  The keyword 'yield from' is used when our generator function
        needs to call another function for which a `yield` will be called.  
        In other words, the `yield` is delegated by the generator function
        to another function.

        This function is intended to be called the first time by 
        the __iter__ function.
        """
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)
        
    def __reversed__(self):
        """
        Perform a formward traversal (in order traversal) starting from 
        the root of the BST.  This function is called when a the 
        reversed function is called and is frequently used with a for
        loop.

        for value in reversed(my_bst):
            print(value)

        """        
        yield from self._traverse_backward(self.root)  # Start at the root

    def get_height(self):
        """
        Determine the height of the BST.  Note that an empty tree
        will have a height of 0 and a tree with one item (root) will
        have a height of 1.
        
        If the tree is empty, then return 0.  Otherwise, call 
        _get_height on the root which will recursively determine the 
        height of the tree.
        """
        if self.root is None:
            return 0
        else:
            return self._get_height(self.root)  # Start at the root

    def insert(self, data):
        """
        Insert 'data' into the BST.  If the BST
        is empty, then set the root equal to the new 
        node.  Otherwise, use _insert to recursively
        find the location to insert.
        """
        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)  # Start at the root

    def _traverse_backward(self, node):
        """
        Does a backwards traversal (reverse in-order traversal) through the 
        BST.  If the node that we are given (which is the current
        sub-tree) exists, then we will keep traversing on the right
        side (thus getting the larger numbers first), then we will 
        provide the data in the current node, and finally we will 
        traverse on the left side (thus getting the smaller numbers last).

        This function is intended to be called the first time by 
        the __reversed__ function.        
        """
        
        if node.right is not None:
             yield from self._traverse_backward(node.right)
        
        yield node.data
        if node.left is not None:
             yield from self._traverse_backward(node.left)
          # Replace this when you implement your solution
    

    ####################
    ##problem 1 ##
    ## write a function that inserts data into a binary tree
    ## hint, determin if the new value is higher or lower than 
    ## the data at the current node.
    ## dont forget to check if the tree is empty
    ####################
    def _insert(self, data, node):
        if data <= node.data:
            # The data belongs on the left side.
            if node.left is None:
                # We found an empty spot
                node.left = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the left sub-tree.
                self._insert(data, node.left)
        elif data > node.data:
            # The data belongs on the right side.
            if node.right is None:
                # We found an empty spot
                node.right = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the right sub-tree.
                self._insert(data, node.right)
    
    #############################
    # end problem 1
    #############################

    
    def __reversed__(self):
        """
        Perform a formward traversal (in order traversal) starting from 
        the root of the BST.  This function is called when a the 
        reversed function is called and is frequently used with a for
        loop.

        for value in reversed(my_bst):
            print(value)

        """        
        yield from self._traverse_backward(self.root)  # Start at the root


    def getHeight(self):
        if self.root is None:
            return 0
        else:
            return self._getHeight(self.root)
    #######################
    ## problem 2
    ## write a function to get the height of a tree
    #######################
    def _getHeight(self, node):
        if node.left is not None:
            left = 1 + self._getHeight(node.left)
        else:
            left = 1
        if node.right is not None:
            right = 1 + self._getHeight(node.right)
        else: 
            right = 1

        if right > left:
            return right
        elif left > right:
            return right 
        else:
            return left

    #######################
    ## end problem 2
    #######################
    
    def getLeaves(self):
        if self.root is None:
            print("the tree is barren")
        else:
            self._getLeaves(self.root)
        
    #####################    
    ## Problem 3
    ## write a function that will print
    ## the leaves of a tree
    #####################
    def _getLeaves(self, node):
        # must be check both no matter what
        if node.left is not None: # check if left attribute
            self._getLeaves(node.left)
        if node.right is not None: # check if right exists
            self._getLeaves(node.right)
        # only print the value when both left and right
        # do not exist
        if node.left is None and node.right is None:
            print(node.data)
    
    ####################
    ## End Problem 3
    ####################
        

#####################
## SOLUTIONS ##
#####################

print(" **** answer 1 **** ")
Pine = BST()
Pine.insert(10)
Pine.insert(5)
Pine.insert(15)
Pine.insert(7)
Pine.insert(12)
Pine.insert(5)
Pine.insert(17)
Pine.insert(20)
for x in Pine:
    print(x)
# 4 5 7 10 12 15 17 20


print(" **** answer 2 **** ")
print(Pine.getHeight()) 
#4

print(" **** answer 3 **** ")
Pine.getLeaves() 
#4 7 12 20