def is_operator(c):
    return c in ['|', '.', '*', '+', '?']

def get_precedence(c):
    precedence = {
        '(': 1,
        '|': 2,
        '.': 3,
        '?': 4,
        '*': 4,
        '+': 4,
        '^': 5
    }
    return precedence.get(c, 0)

def infix_to_postfix(regex):
    postfix = []
    stack = []

    for c in regex:
        if c == '(':
            stack.append(c)

        elif c == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()  # Eliminar el '(' de la pila

        elif is_operator(c):
            while stack and get_precedence(stack[-1]) >= get_precedence(c):
                postfix.append(stack.pop())
            stack.append(c)

        else:
            postfix.append(c)

    while stack:
        postfix.append(stack.pop())

    return ''.join(postfix)

# Prueba con las expresiones regulares proporcionadas
expressions = [
    "(a|t)c",
    "(a|b)*",
    "(a*|b*)*",
    "((E|a)|b*)*",
    "(a|b)*abb(a|b)*",
    "0?(1?)?0*",
    "if\\([ae]+\\)\\{[ei]+\\}(\\n(else\\{[jl]+\\}))?"
]

for expr in expressions:
    postfix_expression = infix_to_postfix(expr)
    print(f"Expresión original: {expr}")
    print(f"Expresión en formato postfix: {postfix_expression}")
    print()
