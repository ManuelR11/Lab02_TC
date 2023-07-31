def is_operator(c):
    return c in ['|', '?', '+', '*', '^']

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

def format_regex(regex):
    res = regex[0]
    for i in range(1, len(regex)):
        c1 = regex[i-1]
        c2 = regex[i]

        if c2 == '(' or c1 == ')' or c1 not in '|(' and c2 not in '|)?*':
            res += '.'

        res += c2

    return res

def convert_extension(c):
    if c == '?':
        return '|ε|'
    elif c == '+':
        return '|ε|' + '*'
    return c

def infix_to_postfix(regex):
    postfix = []
    stack = []
    formatted_regex = format_regex(regex)

    i = 0
    while i < len(formatted_regex):
        c = formatted_regex[i]

        if c == '\\':
            # Manejar el caracter escapado, agregar el siguiente carácter tal cual
            postfix.append(formatted_regex[i+1])
            i += 2
            continue

        if c == '(':
            stack.append(c)

        elif c == ')':
            while stack and stack[-1] != '(':
                postfix.append(convert_extension(stack.pop()))

            if stack and stack[-1] == '(':
                stack.pop()
            else:
                postfix.append('?')  # Agregar carácter de apertura para corregir desbalance

        elif is_operator(c):
            while stack and get_precedence(stack[-1]) >= get_precedence(c):
                postfix.append(convert_extension(stack.pop()))
            stack.append(c)

        else:
            postfix.append(c)

        i += 1

    while stack:
        postfix.append(convert_extension(stack.pop()))

    return ''.join(postfix)

# Prueba con las expresiones regulares proporcionadas
expressions = [
    "(a|t)c",
    "(a|b)*",
    "(a*|b*)*",
    "((E|a)|b*)*",
    "(a|b)*abb(a|b)*",
    "0?(1?)?0*",
    "if\\([ae]+\\)\\{[ei]+\\}(\\n(else\\{[jl]+\\}))?",
    "[ae03]+@[ae03]+.(com|net|org)(.(gt|cr|co))?"
]

for expr in expressions:
    postfix_expression = infix_to_postfix(expr)
    print(f"Expresión original: {expr}")
    print(f"Expresión en formato postfix: {postfix_expression}")
    print()
