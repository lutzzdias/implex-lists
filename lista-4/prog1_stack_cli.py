import sys
from datetime import datetime

print('Thiago Lütz Dias')
print(datetime.now())
print()

def add(stack, letter):
    stack.append(letter)

def clear(stack):
    for i in range(len(stack)):
        stack.pop()

def pop(stack):
    stack.pop()


string = sys.argv[1]
stack = []

for char in string:
    if char == '#':
        pop(stack)
    elif char == '@':
        clear(stack)
    else:
        add(stack, char)

print(''.join(stack))