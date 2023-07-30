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
    res = ''
    for i in range(len(regex)):
        c1 = regex[i]

        if i + 1 < len(regex):
            c2 = regex[i + 1]

            res += c1

            if (c1 != '(' and c2 != ')' and
                    (c2 != '?' and c2 != '*' and c2 != '+') and
                    (c1 != '?' and c1 != '*' and c1 != '+')):
                res += '.'

    res += regex[-1]
    return res

def infix_to_postfix(regex):
    postfix = ''
    stack = []
    formatted_regex = format_regex(regex)

    for c in formatted_regex:
        if c == '(':
            stack.append(c)

        elif c == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()

            if stack and stack[-1] == '(':
                stack.pop()
            else:
                postfix += '?'  # Agregar carácter de apertura para corregir desbalance

        else:
            while stack and get_precedence(stack[-1]) >= get_precedence(c):
                postfix += stack.pop()
            stack.append(c)

    while stack:
        if stack[-1] == '(':
            postfix += '+'  # Agregar carácter de cierre para corregir desbalance
            stack.pop()
        else:
            postfix += stack.pop()

    return postfix

# Test con las expresiones regulares proporcionadas
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
