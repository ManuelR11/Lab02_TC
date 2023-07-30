'''
Universidad del Valle de Guatemala
CC2019 Teoría de la Computación
Sección 20

Laboratorio No. 2
Ejercicio No. 2

Integrantes:
    Manuel Rodas 21509
    Jose Santisteban 21153
    Sebastian Solorzano 21826
'''

#Metodo para verificar si el stack esta vacio
def is_empty(stack):
    return len(stack) == 0

#Metodo para agregar un elemento al stack
def push(stack, item):
    stack.append(item)

#Metodo para sacar un elemento del stack
def pop(stack):
    if not is_empty(stack):
        return stack.pop()
    return None

#Metodo para ver el ultimo elemento del stack
def peek(stack):
    if not is_empty(stack):
        return stack[-1]
    return None

#Metodo para verificar si la expresion esta balanceada
def is_balanced(expression):
    stack = [] 
    opening_symbols = "({[" 
    closing_symbols = ")}]" 
    symbols_map = {')': '(', ']': '[', '}': '{'}
    steps = []

    for idx, char in enumerate(expression):
        if char in opening_symbols:
            push(stack, (char, idx)) 
        elif char in closing_symbols:
            if is_empty(stack) or symbols_map[char] != peek(stack)[0]:
                return False, steps
            else:
                opening_symbol, opening_idx = pop(stack)
                steps.append(f"{opening_symbol} coincide con {char}")

    return is_empty(stack), steps

#Inicio del programa
file_name = "Ejercicio2/expresiones_2.txt" 
try:
    with open(file_name, "r", encoding="utf-8") as file:
        lines = file.readlines()

        for idx, line in enumerate(lines):
            expression = line.strip()
            balanced, steps = is_balanced(expression)

            print(f"\nExpresión {idx+1}: {expression}")
            if balanced:
                print("La expresión está balanceada.")
            else:
                print("La expresión no está balanceada.")

            for step in steps:
                print(step)

except FileNotFoundError:
    print(f"Error: Archivo '{file_name}' no encontrado.")

