import sys

class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
    
    def pop(self):
        temp = self.head
        self.head = self.head.next
        temp = None
    
    def clear(self):
        while self.head:
            self.pop()

    def print(self):
        self.__print__(self.head)
    
    def __print__(self, node):
        if node:
            if node.next:
                self.__print__(node.next)
            if node == self.head:
                print(node.data)
            else:
                print(node.data, end='')
        else:
            return

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

string = sys.argv[1]
stack = LinkedList()

for char in string:
    if char == '#':
        stack.pop()
    elif char == '@':
        stack.clear()
    else:
        stack.push(char)

stack.print()