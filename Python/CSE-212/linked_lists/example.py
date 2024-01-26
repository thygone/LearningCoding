## Exampel created by Dane Selch
from types import NoneType, new_class
from typing import no_type_check_decorator

#This is a class for the linked list, no need to change this
class LinkedList:
    class Node:
        def __init__(self, data):
            """
            initialize the node
            """
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        """
        initialize the linked list
        """
        self.head = None
        self.tail = None
    
    def addColor(self, color):
        newNode = LinkedList.Node(color)
        if (self.head):
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        else:
            self.head = newNode
            self.tail = newNode


    ''' 
    Here is the start of the example problem
    '''
    # 1. write a function to add colors into the list at the head
    def addColor_tail(self, color):
        pass

    #2. write a function to print the data of the 3rd node in the list
    def print_third(self):
        pass

    # 3. write a function that can add to the middle of a function after the target
    def add_middle(self, color, target):
        pass

    # 4. write a function that will remove a desired color from the list
    def removeValue(self, value):
        pass
            

    
    
    """
    END OF PROBLEMS
    """
    
    def print_list(self):
        current = self.head
        while(current):
            print(" ")
            print(current.data)
            current = current.next
            

            
########## ANSWERS ############

my_colors = LinkedList()


print("\nproblem 1")
my_colors.addColor("red")
my_colors.addColor("orange")
my_colors.addColor("yellow")
my_colors.addColor("green")
my_colors.addColor_tail("brown")
my_colors.addColor_tail("blue")
my_colors.print_list() # green yellow orange red brown blue

print("\n--------------------------------")
print(" Problem 2")
my_colors.print_third() #yellow

print("\n--------------------------------")
print(" Problem 3")
my_colors.add_middle("teal", "red")
my_colors.add_middle("cat", "teal")
my_colors.print_list() # green yellow orange red teal cat brown blue

print("\n--------------------------------")
print(" Problem 4")
## HOW DID A CATS GET IN THERE!!! we need to remove it
my_colors.removeValue("cat")
my_colors.print_list() # green yellow orange red teal brown blue