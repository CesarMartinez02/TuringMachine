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
    """Máquina de Turing que suma dos números y devuelve el resultado en decimal."""
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
    
    resultado = tm.tape.count("1")
    return str(resultado)

def execute_operation(expression):
    match = re.match(r"(\d+)\s*([\+\-\*/%])\s*(\d+)", expression)
    if match:
        a, op, b = match.groups()
        a, b = int(a), int(b)

        if op == "+":
            return add_turing("1" * a, "1" * b)
        elif op == "-":
            return str(a - b if a >= b else "Error: Resta negativa")
        elif op == "*":
            return str(a * b)
        elif op == "/":
            return str(a // b if b != 0 else "Error: División por cero")
        elif op == "%":
            return str(a % b if b != 0 else "Error: División por cero")

    match_pow = re.match(r"pow\((\d+),\s*(\d+)\)", expression)
    if match_pow:
        x, y = map(int, match_pow.groups())
        return str(x ** y)

    match_sqrt = re.match(r"sqrt\((\d+),\s*(\d+)\)", expression)
    if match_sqrt:
        x, y = map(int, match_sqrt.groups())
        return str(int(x ** (1/y))) if y != 0 else "Error: División por cero"

    return "Operación no válida"

def main():
    print("Máquina de Turing")
    print("Operaciones: +, -, *, /, %, pow(x,y), sqrt(x,y)")
    print("Escribe 'cerrar' para salir.")

    while True:
        expr = input("Ingresa operación: ").strip()
        if expr.lower() == "cerrar":
            print("chao...")
            break

        resultado = execute_operation(expr)
        print(f"Resultado: {resultado}")

if __name__ == "__main__":
    main()
