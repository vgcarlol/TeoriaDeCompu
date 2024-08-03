import re
from graphviz import Digraph
import os

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def get_precedence(c):
    precedences = {
        '(': 1,
        '|': 2,
        '.': 3,
        '?': 4,
        '*': 4,
        '+': 4,
    }
    return precedences.get(c, 6)

def format_regex(regex):
    formatted = []
    operators = set(['|', '?', '+', '*', '(', ')'])
    length = len(regex)
    
    i = 0
    while i < length:
        c1 = regex[i]
        if c1 == '+':
            if len(formatted) > 0:
                formatted.append(formatted[-1])
                formatted.append('*')
        elif c1 == '?':
            if len(formatted) > 0:
                formatted.append('|')
                formatted.append('ε')
        else:
            formatted.append(c1)
            if c1 == '\\':
                i += 1
                formatted.append(regex[i])
            elif c1 not in operators and i + 1 < length:
                c2 = regex[i + 1]
                if c2 not in operators and c2 != '\\' and c2 != '(' and c2 != ')':
                    formatted.append('.')
        i += 1
    
    return ''.join(formatted)

def infix_to_postfix(regex):
    postfix = []
    stack = []
    formatted_regex = format_regex(regex)

    for c in formatted_regex:
        if c.isalnum() or c == '\\' or c == 'ε':
            postfix.append(c)
        elif c == '(':
            stack.append(c)
        elif c == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            if stack:
                stack.pop()  # Pop the '('
            else:
                raise ValueError("Mismatched parentheses in expression")
        else:
            while stack and get_precedence(stack[-1]) >= get_precedence(c):
                postfix.append(stack.pop())
            stack.append(c)

    while stack:
        if stack[-1] == '(':
            raise ValueError("Mismatched parentheses in expression")
        postfix.append(stack.pop())

    return ''.join(postfix)

def postfix_to_ast(postfix):
    stack = []
    operators = set(['|', '*', '+', '?', '.'])
    for char in postfix:
        if char in operators:
            if char in ['*', '+', '?']:
                node = Node(char)
                node.left = stack.pop()
            else:
                node = Node(char)
                node.right = stack.pop()
                node.left = stack.pop()
            stack.append(node)
        else:
            stack.append(Node(char))
    return stack.pop()

def draw_ast(root):
    dot = Digraph()
    def add_nodes_edges(root, parent=None, label=''):
        node_id = id(root)
        if parent:
            dot.edge(str(id(parent)), str(node_id), label=label)
        dot.node(str(node_id), root.value)
        if root.left:
            add_nodes_edges(root.left, root, 'l') # l = left (izquierda)
        if root.right:
            add_nodes_edges(root.right, root, 'r') # r = right (derecha)
    add_nodes_edges(root)
    return dot

def process_file(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    for line in lines:
        clean_line = re.sub(r'[^\w\s]', '', line.strip())  # Elimina caracteres especiales
        try:
            postfix = infix_to_postfix(line.strip())
            print(f"Postfix para '{line.strip()}': {postfix}")
            ast_root = postfix_to_ast(postfix)
            dot = draw_ast(ast_root)
            filename = f'ast_{clean_line}'
            dot.render(filename, view=True)  # Usa el nombre limpio para el archivo
            print(f"AST para '{line.strip()}' Guardado como '{filename}.pdf'")
        except ValueError as e:
            print(f"Error processing line '{line.strip()}': {e}")

# Configurar Graphviz para usar una ruta específica
os.environ["PATH"] += os.pathsep + r'C:/Users/user/Desktop/Github/TeoriaDeCompu/lab3/Graphviz/bin'

# Llamada al proceso
input_file = 'C:/Users/user/Desktop/Github/TeoriaDeCompu/lab3/Ejercicio 1/expressions.txt'
process_file(input_file)
