import re

class TuringMachine:
    def __init__(self, tape, blank="_"):
        self.tape = list(tape)
        self.head = 0
        self.blank = blank
        self.state = "q0"
        self.transitions = {}

    def set_transitions(self, transitions):
        self.transitions = transitions

    def move_head(self, direction):
        if direction == "R":
            self.head += 1
            if self.head >= len(self.tape):
                self.tape.append(self.blank)
        elif direction == "L" and self.head > 0:
            self.head -= 1

    def read_symbol(self):
        return self.tape[self.head]

    def write_symbol(self, symbol):
        self.tape[self.head] = symbol

    def run(self):
        while self.state in self.transitions:
            symbol = self.read_symbol()
            if symbol in self.transitions[self.state]:
                new_symbol, move, new_state = self.transitions[self.state][symbol]
                self.write_symbol(new_symbol)
                self.move_head(move)
                self.state = new_state
            else:
                break

    def __str__(self):
        return "".join(self.tape).replace(self.blank, "")

def add_turing(a, b):
    tape = list(f"{a}+{b}=")
    tm = TuringMachine(tape)
    transitions = {
        "q0": {"+": ("+", "R", "q1")},
        "q1": {"1": ("X", "R", "q2"), "=": ("=", "L", "q4")},
        "q2": {"1": ("1", "R", "q2"), "=": ("=", "L", "q3")},
        "q3": {"X": ("1", "L", "q1")},
        "q4": {"X": ("1", "L", "q4"), "+": ("+", "R", "halt")}
    }
    tm.set_transitions(transitions)
    tm.run()
    return str(tm).count("1")

def subtract_turing(a, b):
    tape = list(f"{a}-{b}=")
    tm = TuringMachine(tape)
    transitions = {
        "q0": {"-": ("-", "R", "q1")},
        "q1": {"1": ("_", "R", "q2"), "=": ("=", "L", "q3")},
        "q2": {"1": ("1", "R", "q2"), "=": ("=", "L", "q3")},
        "q3": {"-": ("-", "R", "halt")}
    }
    tm.set_transitions(transitions)
    tm.run()
    return str(tm).count("1")

def multiply_turing(a, b):
    return str(a * b)

def divide_turing(a, b):
    return str(a // b if b != 0 else "Error: División por cero")

def modulo_turing(a, b):
    return str(a % b if b != 0 else "Error: División por cero")

def power_turing(a, b):
    return str(a ** b)

def sqrt_turing(a, b):
    return str(int(a ** (1/b))) if b != 0 else "Error: División por cero"

def execute_operation(expression):
    match = re.match(r"(\d+)\s*([\+\-\*/%])\s*(\d+)", expression)
    if match:
        a, op, b = match.groups()
        a, b = int(a), int(b)
        
        if op == "+":
            return add_turing("1" * a, "1" * b)
        elif op == "-":
            return subtract_turing("1" * a, "1" * b)
        elif op == "*":
            return multiply_turing(a, b)
        elif op == "/":
            return divide_turing(a, b)
        elif op == "%":
            return modulo_turing(a, b)
    
    match_pow = re.match(r"pow\((\d+),\s*(\d+)\)", expression)
    if match_pow:
        x, y = map(int, match_pow.groups())
        return power_turing(x, y)
    
    match_sqrt = re.match(r"sqrt\((\d+),\s*(\d+)\)", expression)
    if match_sqrt:
        x, y = map(int, match_sqrt.groups())
        return sqrt_turing(x, y)
    
    return "Operación no válida"

def main():
    print("Máquina de Turing - Calculadora")
    print("Operaciones: +, -, *, /, %, pow(x,y), sqrt(x,y)")
    print("Escribe 'cerrar' para salir.")
    
    while True:
        expr = input("Ingresa operación: ").strip()
        if expr.lower() == "cerrar":
            print("Adiós...")
            break

        resultado = execute_operation(expr)
        print(f"Resultado: {resultado}")

if __name__ == "__main__":
    main()
