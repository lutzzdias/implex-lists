import sys

def add(stack, letter):
    stack.append(letter)

def clear(stack):
    for i in range(len(stack)):
        stack.pop()

def pop(stack):
    stack.pop()


stack = []
condition = True

while condition:
    print('Pilha = ' + ''.join(stack))
    char = input('Insira um caracter:\n\n  # - Apaga o último caracter inserido\n  @ - Apaga tudo o que foi inserido anteriormente\n  ENTER - Termina o programa\n\n> ')

    if char == '':
        condition = False
    elif char == '#':
        pop(stack)
    elif char == '@':
        clear(stack)
    else:
        add(stack, char)

print(''.join(stack))