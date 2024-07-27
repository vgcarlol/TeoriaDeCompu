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
        formatted.append(c1)
        
        if c1 == '\\':  # Escapar el siguiente carácter
            i += 1
            formatted.append(regex[i])
        elif c1 not in operators and i + 1 < length:
            c2 = regex[i + 1]
            if c2 not in operators and c2 != '\\' and c2 != '(' and c2 != ')':
                formatted.append('.')  # Insertar concatenación implícita
        
        i += 1
    
    return ''.join(formatted)

def infix_to_postfix(regex):
    postfix = []
    stack = []
    formatted_regex = format_regex(regex)
    steps = []

    i = 0
    while i < len(formatted_regex):
        c = formatted_regex[i]
        if c.isalnum() or c == '\\':
            postfix.append(c)
            if c == '\\' and i + 1 < len(formatted_regex):
                i += 1
        elif c == '(':
            stack.append(c)
        elif c == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()  # Pop the '(' from the stack
        else:
            while stack and get_precedence(stack[-1]) >= get_precedence(c):
                postfix.append(stack.pop())
            stack.append(c)
        
        steps.append(f"Token: {c}, Stack: {stack[:]}, Output: {postfix[:]}")
        i += 1

    while stack:
        postfix.append(stack.pop())
        steps.append(f"Stack emptying, Stack: {stack[:]}, Output: {postfix[:]}")

    return ''.join(postfix), steps

def process_file(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    with open(output_file, 'w') as file:
        for line in lines:
            postfix, steps = infix_to_postfix(line.strip())
            file.write(f"Postfix: {postfix}\n")
            file.write("Steps:\n")
            for step in steps:
                file.write(step + "\n")
            file.write("\n")

# Ejemplo de uso
input_file = 'C:/Users/user/Desktop/Github/TeoriaDeCompu/lab2/Ejercicio 3/input_expressions.txt'
output_file = 'C:/Users/user/Desktop/Github/TeoriaDeCompu/lab2/Ejercicio 3/output_postfix.txt'
process_file(input_file, output_file)
