class Node:
    def __init__(self, data):
        self.data = data # data to be stored in the node
        self.next = None # pointer to the next node in the list

class LinkedList:
    def __init__(self, lst=None):
        self.head = None # pointer to the first node in the list
        self.tail = None # pointer to the last node in the list
        if lst is not None:
            for item in lst:
                self.append(item)

    def append(self, data):
        new_node = Node(data) # create a new node with the given data
        if self.head is None: # if the list is empty, make the new node the head
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node 

    def insert(self, data, position, head=None):
        if head is None:
            head = self.head
        if position == 0:
            new_node = Node(data)
            new_node.next = head
            head = new_node
        else:
            head.next = self.insert(data, position-1, head.next)
        return head
    
    def remove(self, position, head=None):
        if head is None:
            head = self.head
        if position == 0:
            head = head.next
        else:
            head.next = self.remove(position-1, head.next)
        return head

    def __str__(self): # string representation of the list
        current_node = self.head
        string = ""
        while True:
            string += str(current_node.data)
            current_node = current_node.next
            if current_node is None:
                return string
            string += ' → '

amtrak_stations = ['Union Station', 'New Carrollton', 'BWI', 'Baltimore', 'Wilmington Delaware', 'Philadelphia']
amtrak = LinkedList(amtrak_stations)
print(amtrak)
amtrak.insert('Aberdeen', 4) # insert between Baltimore and Wilmington
print(amtrak)
amtrak.remove(4) # remove Aberdeen
print(amtrak)