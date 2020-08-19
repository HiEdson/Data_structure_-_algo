"""
in this program we are going to swap to nodes in a linked list.
1 - considering Node_! and Node_2 are not the head of the list
2 - Either Node_! or Node_2 is the head of the list
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class linkedlist:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node =Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node =last_node.next
        last_node.next = new_node

    def swapNode(self, key_1, key_2):
        if key_1 == key_2:
            return "Are you serious?"
        prev_1 = None
        cur_1 = self.head


    def printNode (self):
        cur_node =self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next
        

llist1 = linkedlist()

llist1.append("A")
llist1.append("B")
llist1.append("C")
llist1.printNode()