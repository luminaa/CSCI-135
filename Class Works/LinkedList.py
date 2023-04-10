class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    def __str__(self):
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

print(days)
