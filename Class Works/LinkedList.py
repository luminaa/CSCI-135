class Node:
    def __init__(self, data):
        self.data = data # data to be stored in the node
        self.next = None # pointer to the next node in the list

class LinkedList:
    def __init__(self):
        self.head = None # pointer to the first node in the list

    def append(self, data):
        new_node = Node(data) # create a new node with the given data
        if self.head is None: # if the list is empty, make the new node the head
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None: # traverse the list to the end
                current_node = current_node.next
            current_node.next = new_node # set the new node as the next node of the last node

    def insert(self, value, position, head=None):
        if head is None:
            head = self.head
        if position == 0:
            new_node = Node(value)
            new_node.next = head
            head = new_node
        else:
            head.next = self.insert(value, position-1, head.next)
        return head 

    def __str__(self): # string representation of the list
        current_node = self.head
        string = ""
        while current_node is not None:
            string += str(current_node.data) + " "
            current_node = current_node.next
        return string


days = LinkedList()
days.append("Mon")
days.append("Tue")
days.append("Wed")
days.append("Thur")
days.append("Fri")
days.append("Sat")
days.append("Sun")
days.insert("Fri", 4)

print(days)
