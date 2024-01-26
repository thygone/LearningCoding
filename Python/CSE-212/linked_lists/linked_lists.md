# **Linked Lists**
## what is it?
A linked lists, like a regular list, consists of a head and a tail,
but unlike other lists, it is made up of NODES instead of indexes.

## What is a Node?    
Each node has three parts consisting of the addresses of the 
previous and next nodes, as well as the value held at the current 
node.

## How is it organized in memory?
With each of the nodes pointing to the previous and the next part
of the list, a linked list is able to be stored randomly within the 
memory of the computer. The benifit of this is that the size of a 
linked list becomes dynamic, meaning it can grow and shrink as 
needed
![a picture of nodes strung together](../images\linked_list_double.jpeg)

## Transversing a Linked List
without an index, it can be hard to know how pick out a value from 
the middle. The trick is that you need to start at one point and 
follow the addresses. Think of a choose your own adventure book.
If you read it from front to back, it will be all jumbled together 
and will not make any sence. But, thanks to the notes that say 
"turn to page 6," you know that the story continues on page 6. It
is the same with a linked list. in memory everything appears 
jumbled, but by following the addresses you can get to your destination.

## Adding to a Linked List
There are three options here. the first is to change the head, 
tail, or a middle value.  (I will use examples of the code with 
each of the steps inside brackets)
### To add to the Head: 
1.  Create a new node
(new_node)
2. set the "next" of the new nod to the current head
(new_node.next = self.head)
3. set the "prev" of the current head to the new node
(self.head.prev = new_node)
4. set the head equal to the new node
(self.head = new_node)
### Add to Tail:
1. create a new node
(new_node)
2. set "prev" node of the new noe to the current tail    
(new_node.prev = self.tail)
3. set the "next" of the current tail to the new node
(self.tail.next = new_node)
4. set the tail equal to the new node
(self.tail = new_node new node)
### Add to Middle:
1. create a new node2 set the "prev" of new node to the current node
(new_node.prev = current)
2. set the next of new node to the next nod after current
(new_node.next = current.next) 
3. set the "next" of the new node to the next node after current
(new_node.next = current.next)
4. set the "prev" of the "next" node after current to the new node
(current.next.prev = new_node)
5. set the current node to the next node
(current.next = new_node)
![adding to the middle of a list](../images/linked_list_insert_middle.jpeg)
## Removing from a list
This is similar to the adding section but we are deleting addresses 
instead of adding them. 

removing from head
1. Set the "prev" of the second node (self.head.next) to nothing 
(self.head.next.prev = None)
2. Set the head to be the second node 
(self.head = self.head.next)
    
remove from tail
1. set next of prev node (self.tail.prev) to None
(self.tail.prev.next = None)
2. set the tail to the "prev" node
(self.tail = self.tail.prev)

remove from middle
1. Set the prev of the node after current to the node before current 
(current.next.prev = current.prev)

2. Set the next of the node before current to the node after current 
(current.prev.next = current.next)



## list of helpful commands
| command | definition | BigO notation |
| -------------------- | ------------------------------ | ---------------- |
| insert_head(value) |	Adds "value" before the head | O(1) - one loop to adjust the pointer |
| insert_tail(value)	| Adds "value" after the tail | O(1) - one loop to adjust the pointer |
| insert(i, value) | Adds "value" after node "i". | O(n) Takes a number of loops to find the desired value |
| remove_head() | Removes the first item (the head) | O(1) - one loop to adjust the pointer |
| remove_tail(index) | Removes the last item (the tail) | O(1) - one loop to adjust the pointer |
| remove(i) | Removes node "i". |  O(n) Takes a number of loops to find the desired value |
| size() | Return the size of the linked list | O(1) - one loop to adjust the pointer |
| empty() | Returns true if the length of the linked list is zero. | O(1) - one loop to adjust the pointer |

## Performance
the performance of these functions depend on where you are trying to change the linked list. When adding or removing from the head or foot of the list requires only a change in the pointer after one iteration of the function
When you are trying to edit the information from a specific value, you will have to iterate through an unknown number of values to find the desired location.

[example problem](example.py)

[solution](solution.py)

[Back](../welcome.md)