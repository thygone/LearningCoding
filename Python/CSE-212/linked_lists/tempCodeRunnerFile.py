#This is the class for a Node, no need to change this
class Node:
   def __init__(self, data=None, next=None, prev=None):
      self.data = data
      self.next = next
      self.prev = prev
#This is a class for the linked list, no need to change this
class SLinkedList:
    def __init__(self):
      self.head = None
    
    def printList(self):
        current = self.head
        while (current):
            print(current.data)
            current = current.next

            
    # Here is the start of the example problem
    # 1. write a function to add colors into the list at the head
    def addColor(self, color):
        newNode = Node(color)
        if (self.head):
            current = self.head
            while(current.next):
                current = current.next
                current.next = newNode
            else:
                self.head = newNode


    # 2. write a function that will remove a desired color from the list
    def removeColor(color):
        pass


    # 3. write a function that can add to the middle of a function after the target
    def add_middle(color, target):
        pass
    
    #4 finally write a function that can remove from the middle of a function
my_colors = SLinkedList
my_colors.head = Node("bread")

print("problem1")
my_colors.addColor("Red")
my_colors.addColor("Orange")
my_colors.addColor("Lime")
my_colors.addColor("Green")
my_colors.addColor("Teal")
my_colors.addColor("Blue")
my_colors.printList()
print(" answer ")