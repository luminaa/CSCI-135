from collections import deque

class Stack:
    def __init__(self):
        self.__data = deque()

    def push(self, item):
        self.__data.append(item)

    def pop(self):
        return self.__data.pop()

    def get_size(self):
        return len(self.__data)

    def print_elements(self):
        string = ""
        for item in self.__data:
            if string != "":
                string += "->"
            string += " " + str(item) + " "
        print(string)

class Queue:
    def __init__(self):
        self.__data = deque()

    def enqueue(self, item):
        self.__data.append(item)

    def dequeue(self):
        return self.__data.popleft()

    def get_size(self):
        return len(self.__data)

    def print_elements(self):
        string = ""
        for item in self.__data:
            if string != "":
                string += "->"
            string += " " + str(item) + " "
        print(string)

print(" ")

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

print("Initial Stack:")
stack.print_elements()
print(" ")

print("Element Popped from Stack:", stack.pop())
print("Stack Size after Popping:", stack.get_size())
print("Stack after Popping:")
stack.print_elements()
print(" ")

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)

print("Initial Queue:")
queue.print_elements()
print(" ")

print("Element Dequeued from Queue:", queue.dequeue())
print("Queue Size after Dequeuing:", queue.get_size())
print("Queue after Dequeuing:")
queue.print_elements()
print(" ")