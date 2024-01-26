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
        current = LinkedList.Node(color) # declare a new node
        current.prev = self.tail # set the tail of list to the prev of new node
        self.tail.next = current # set the next of the old tail to be the new node
        self.tail = current # now make the tail the new node
        return

    #2. write a function to print the data of the 3rd node in the list
    def print_third(self):
        i = 1 # incramenter
        current = self.head
        while(i < 3): # when the incramenter hits 3 then stop
            current = current.next # move on to the next node
            i += 1 # incrament it
        print(current.data) # print the node we end on

    # 3. write a function that can add to the middle of a function after the target
    def add_middle(self, color, target):
        current = self.head
        while(current):
            if(current.data == target):
                if(self.tail == current):
                    self.addColor_tail(color)
                else:
                    newNode = LinkedList.Node(color) #new node
                    newNode.prev = current # set the prev and next of the new node
                    newNode.next = current.next
                    current.next.prev = newNode # change the old prev of the forward node to the new node
                    current.next = newNode# change the old next of the current node to point to the new node

                return #end the function after the color is added in
            current = current.next # if you have not added the color go to the next node

    # 4. write a function that will remove a desired color from the list
    def removeValue(self, value):
        current = self.head
        while(current):
            if (current.data == value):
                if(current == self.head):
                    current.next.prev = None
                if(current == self.tail):
                    current.prev.next = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                return
            current = current.next
            

    
    
    """
    END OF PROBLEMS
    """
    
    def print_list(self):
        current = self.head
        while(current):
            print(" ")
            print(current.data)
            current = current.next
            


######## ANSWERS ###########
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