from pprint import pprint as pp
sum_trasitions = {
    "q_0": {
        "0": {"write": "0", "move": "R", "next_state": "q_0"},
        "c": {"write": "0", "move": "R", "next_state": "q_1"},
    },
    "q_1": {
        "0": {"write": "0", "move": "R", "next_state": "q_1"},
        "ε": {"write": "ε", "move": "L", "next_state": "q_2"},
    },
    "q_2": {"0": {"write": "ε", "move": "L", "next_state": "q_3"}},
    "q_3": {
        "0": {"write": "0", "move": "L", "next_state": "q_3"},
        "ε": {"write": "ε", "move": "R", "next_state": "q_4"},
    },
}


sum_config_tm = {
    "initial_state": "q_0",
    "accept_states": "q_4",
    "symbols": ["0"],
    "blank_symbol": "ε",
    "transitions": sum_trasitions,
}

sub_transitions = {
    "q_0": {
        "0": {"write": "ε", "move": "R", "next_state": "q_1"},
    },
    "q_1": {
        "c": {"write": "c", "move": "R", "next_state": "q_1"},
        "0": {"write": "0", "move": "R", "next_state": "q_1"},
        "ε": {"write": "ε", "move": "L", "next_state": "q_2"},
    },
    "q_2": {
        "0": {"write": "ε", "move": "L", "next_state": "q_3"},
        "c": {"write": "0", "move": "L", "next_state": "q_4"},
    },
    "q_3": {
        "c": {"write": "c", "move": "L", "next_state": "q_3"},
        "0": {"write": "0", "move": "L", "next_state": "q_3"},
        "ε": {"write": "ε", "move": "R", "next_state": "q_0"},
    },
}

sub_config_tm = {
    "initial_state": "q_0",
    "accept_states": "q_4",
    "symbols": ["0", "c"],
    "blank_symbol": "ε",
    "transitions": sub_transitions,
}

mult_transitions = {
    "q_0": {
        "0": {"write": "ε", "move": "R", "next_state": "q_1"},
        "c": {"write": "ε", "move": "R", "next_state": "q_9"},
    },
    "q_1": {
        "0": {"write": "0", "move": "R", "next_state": "q_1"},
        "c": {"write": "c", "move": "R", "next_state": "q_2"},
    },
    "q_2": {
        "0": {"write": "X", "move": "R", "next_state": "q_3"},
        "c": {"write": "c", "move": "L", "next_state": "q_7"},
    },
    "q_3": {
        "0": {"write": "0", "move": "R", "next_state": "q_3"},
        "c": {"write": "c", "move": "R", "next_state": "q_4"},
    },
    "q_4": {
        "ε": {"write": "0", "move": "L", "next_state": "q_5"},
        "0": {"write": "0", "move": "R", "next_state": "q_4"},
    },
    "q_5": {
        "c": {"write": "c", "move": "L", "next_state": "q_6"},
        "0": {"write": "0", "move": "L", "next_state": "q_5"},
    },
    "q_6": {
        "0": {"write": "0", "move": "L", "next_state": "q_6"},
        "X": {"write": "X", "move": "R", "next_state": "q_2"},
    },
    "q_7": {
        "X": {"write": "0", "move": "L", "next_state": "q_7"},
        "c": {"write": "c", "move": "L", "next_state": "q_8"},
    },
    "q_8": {
        "0": {"write": "0", "move": "L", "next_state": "q_8"},
        "ε": {"write": "ε", "move": "R", "next_state": "q_0"},
    },
    "q_9": {
        "0": {"write": "ε", "move": "R", "next_state": "q_9"},
        "c": {"write": "ε", "move": "R", "next_state": "q_10"},
    },
}

mult_config_tm = {
    "initial_state": "q_0",
    "accept_states": "q_10",
    "symbols": ["0", "c", "x"],
    "blank_symbol": "ε",
    "transitions": mult_transitions,
}

div_transitions = {
    "q_0": {
        "0": {"write": "ε", "move": "R", "next_state": "q_1"},
        "c": {"write": "c", "move": "R", "next_state": "q_4"},
    },
    "q_1": {
        "0": {"write": "0", "move": "R", "next_state": "q_1"},
        "c": {"write": "c", "move": "R", "next_state": "q_2"},
    },
    "q_2": {
        "0": {"write": "X", "move": "L", "next_state": "q_3"},
        "X": {"write": "X", "move": "R", "next_state": "q_2"},
        "c": {"write": "ε", "move": "L", "next_state": "q_6"},
        "ε": {"write": "ε", "move": "R", "next_state": "q_5"},
    },
    "q_3": {
        "c": {"write": "c", "move": "L", "next_state": "q_3"},
        "0": {"write": "0", "move": "L", "next_state": "q_3"},
        "ε": {"write": "0", "move": "R", "next_state": "q_0"},
        "X": {"write": "X", "move": "L", "next_state": "q_3"},
    },
    "q_4": {
        "X": {"write": "X", "move": "R", "next_state": "q_4"},
        "0": {"write": "0", "move": "R", "next_state": "q_4"},
        "c": {"write": "c", "move": "R", "next_state": "q_4"},
        "ε": {"write": "0", "move": "L", "next_state": "q_5"},
    },
    "q_5": {
        "0": {"write": "0", "move": "R", "next_state": "q_5"},
        "c": {"write": "c", "move": "R", "next_state": "q_5"},
        "ε": {"write": "ε", "move": "R", "next_state": "q_6"},
    },
    "q_6": {
        "X": {"write": "ε", "move": "L", "next_state": "q_6"},
        "c": {"write": "ε", "move": "L", "next_state": "q_6"},
        "0": {"write": "ε", "move": "L", "next_state": "q_6"},
        "ε": {"write": "ε", "move": "R", "next_state": "q_7"},
    },
    "q_7": {
        "ε": {"write": "ε", "move": "R", "next_state": "q_7"},
        "0": {"write": "0", "move": "L", "next_state": "q_8"},
    },
}

div_config_tm = {
    "initial_state": "q_0",
    "accept_states": "q_8",
    "symbols": ["0", "c", "X"],
    "blank_symbol": "ε",
    "transitions": div_transitions,
}

mod_transitions = {
    "q_0": {
        "0": {"write": "ε", "move": "R", "next_state": "q_1"},
    },
    "q_1": {
        "c": {"write": "c", "move": "R", "next_state": "q_1"},
        "0": {"write": "0", "move": "R", "next_state": "q_1"},
        "ε": {"write": "ε", "move": "L", "next_state": "q_2"},
    },
    "q_2": {
        "0": {"write": "ε", "move": "L", "next_state": "q_3"},
        "c": {"write": "0", "move": "L", "next_state": "q_4"},
        "ε": {"write": "ε", "move": "R", "next_state": "q_5"},
    },
    "q_3": {
        "c": {"write": "c", "move": "L", "next_state": "q_3"},
        "0": {"write": "0", "move": "L", "next_state": "q_3"},
        "ε": {"write": "ε", "move": "R", "next_state": "q_0"},
    },
    "q_4": {
        "X": {"write": "X", "move": "R", "next_state": "q_4"},
        "0": {"write": "0", "move": "R", "next_state": "q_4"},
        "c": {"write": "c", "move": "R", "next_state": "q_4"},
        "ε": {"write": "0", "move": "L", "next_state": "q_5"},
    },
    "q_5": {
        "0": {"write": "0", "move": "R", "next_state": "q_5"},
        "c": {"write": "c", "move": "R", "next_state": "q_5"},
        "ε": {"write": "ε", "move": "R", "next_state": "q_6"},
    },
    "q_6": {
        "0": {"write": "ε", "move": "R", "next_state": "q_6"},
        "c": {"write": "c", "move": "R", "next_state": "q_6"},
        "ε": {"write": "ε", "move": "L", "next_state": "q_4"},
    },
}

mod_config_tm = {
    "initial_state": "q_0",
    "accept_states": "q_4",
    "symbols": ["0", "c"],
    "blank_symbol": "ε",
    "transitions": mod_transitions,
}

pow_transitions = {
    "q_0": {
        "0": {"write": "0", "move": "R", "next_state": "q_0"},
        "c": {"write": "c", "move": "R", "next_state": "q_1"},
    },
    "q_1": {
        "0": {"write": "X", "move": "R", "next_state": "q_2"},
        "ε": {"write": "0", "move": "L", "next_state": "q_a"},
    },
    "q_2": {
        "0": {"write": "0", "move": "R", "next_state": "q_2"},
        "ε": {"write": "ε", "move": "L", "next_state": "q_3"},
    },
    "q_3": {
        "0": {"write": "0", "move": "L", "next_state": "q_3"},
        "X": {"write": "X", "move": "R", "next_state": "q_4"},
    },
    "q_4": {
        "0": {"write": "0", "move": "R", "next_state": "q_4"},
        "c": {"write": "c", "move": "R", "next_state": "q_5"},
    },
    "q_5": {
        "0": {"write": "0", "move": "R", "next_state": "q_5"},
        "ε": {"write": "c", "move": "L", "next_state": "q_6"},
    },
    "q_6": {
        "0": {"write": "0", "move": "L", "next_state": "q_6"},
        "c": {"write": "c", "move": "L", "next_state": "q_7"},
    },
    "q_7": {
        "X": {"write": "ε", "move": "R", "next_state": "q_1"},
        "ε": {"write": "ε", "move": "R", "next_state": "q_a"},
    },
}

pow_config_tm = {
    "initial_state": "q_0",
    "accept_states": "q_a",
    "symbols": ["0", "c"],
    "blank_symbol": "ε",
    "transitions": pow_transitions,
}

sqrt_transitions = {
    "q_0": {
        "0": {"write": "X", "move": "R", "next_state": "q_1"},
        "ε": {"write": "ε", "move": "R", "next_state": "q_a"},
    },
    "q_1": {
        "0": {"write": "0", "move": "R", "next_state": "q_1"},
        "c": {"write": "c", "move": "L", "next_state": "q_2"},
    },
    "q_2": {
        "0": {"write": "X", "move": "L", "next_state": "q_3"},
        "c": {"write": "c", "move": "L", "next_state": "q_3"},
        "ε": {"write": "ε", "move": "R", "next_state": "q_a"},
    },
    "q_3": {
        "0": {"write": "0", "move": "L", "next_state": "q_3"},
        "X": {"write": "X", "move": "R", "next_state": "q_4"},
        "ε": {"write": "ε", "move": "R", "next_state": "q_a"},
    },
    "q_4": {
        "0": {"write": "0", "move": "R", "next_state": "q_4"},
        "ε": {"write": "c", "move": "R", "next_state": "q_0"},
    },
}

sqrt_config_tm = {
    "initial_state": "q_0",
    "accept_states": "q_a",
    "symbols": ["0", "c"],
    "blank_symbol": "ε",
    "transitions": sqrt_transitions,
}


def parse_input(cadena):
    if "+" in cadena:  # Suma
        a, b = map(int, cadena.split("+"))
        return f"ε{'0' * a}c{'0' * b}ε"

    elif "-" in cadena and cadena.count("-") == 1:  # Resta
        a, b = map(int, cadena.split("-"))
        if a >= b:
            return f"ε{'0' * a}c{'0' * b}ε"
        else:
            return "Error: No se soportan resultados negativos."

    elif "*" in cadena and cadena.count("*") == 1:  # Multiplicación
        a, b = map(int, cadena.split("*"))
        mult = a * b
        if a < 0 or b < 0:
            return "Error: No se permiten números negativos."
        return f"ε{'0' * b}c{'0' * a}c{'ε' * mult}"

    elif "/" in cadena and cadena.count("/") == 1:  # División
        a, b = map(int, cadena.split("/"))
        div = int(a / b)
        if b == 0:
            return "Error: No se permite la división por cero."
        return f"ε{'0' * b}c{'0' * a}c{'ε' * div}"

    elif "%" in cadena and cadena.count("%") == 1:  # Módulo
        a, b = map(int, cadena.split("%"))
        if b == 0:
            return "Error: No se permite el módulo por cero."
        return f"ε{'0' * a}c{'0' * b}ε"

    elif "pow(" in cadena and cadena.endswith(")"):  # Potenciación
        try:
            a, b = map(int, cadena[4:-1].split(","))
            if a < 0 or b < 0:
                return "Error: No se permiten exponentes negativos."
            return f"ε{'0' * (a ** b)}ε"
        except Exception as e:
            return f"Error: Formato incorrecto para potenciación. Error msg: {e}"

    elif "sqrt(" in cadena and cadena.endswith(")"):  # Raíz cuadrada
        try:
            a = int(cadena[5:-1])
            if a < 0:
                return "Error: No se permite la raíz cuadrada de números negativos."
            return f"ε{'0' * a}ε"
        except Exception as e:
            return f"Error: Formato incorrecto para raíz cuadrada. Error msg {e}"

    return "Error: Operación no válida."


class TuringMachine:
    def __init__(self, config):
        self.initial_state = config["initial_state"]
        self.accept_states = config["accept_states"]
        self.symbols = config["symbols"]
        self.blank_symbol = config["blank_symbol"]
        self.transitions = config["transitions"]
        self.tape = []
        self.tape_status = []
        self.head_position = 1

    def init_tape(self, entry):
        self.tape = list(entry)

    def run(self, entry):
        self.init_tape(entry)
        current_state = self.initial_state
        while current_state != self.accept_states:
            current_symbol = self.tape[self.head_position]
            # Verifica si la transición existe para el símbolo actual
            if current_symbol in self.transitions[current_state]:
                transition = self.transitions[current_state][current_symbol]
            else:
                # Si no hay transición definida, detiene la ejecución
                break
            # Aplica la transición
            self.tape[self.head_position] = transition["write"]
            # Mueve el cabezal
            if transition["move"] == "R":
                self.head_position += 1
            elif transition["move"] == "L":
                self.head_position -= 1
            # Actualiza el estado
            current_state = transition["next_state"]
            # Guarda el estado de la cinta
            self.tape_status.append(self.tape.copy())
        return self.tape


if __name__ == "__main__":
    cadena = input(
        "Ingrese una operacion aritmetica (+, -, *, /, %, pow(x,y), sqrt(x)): "
    )
    cadena_parseada = parse_input(cadena)
    print(cadena_parseada)

    if "Error" in cadena_parseada:
        print(cadena_parseada)
    else:
        if "+" in cadena:
            tm = TuringMachine(sum_config_tm)
        elif "-" in cadena:
            tm = TuringMachine(sub_config_tm)
        elif "*" in cadena:
            tm = TuringMachine(mult_config_tm)
        elif "/" in cadena:
            tm = TuringMachine(div_config_tm)
        elif "%" in cadena:
            tm = TuringMachine(mod_config_tm)
        elif "pow(" in cadena:
            tm = TuringMachine(pow_config_tm)
        elif "sqrt(" in cadena:
            tm = TuringMachine(sqrt_config_tm)
        else:
            print("Error: Operación no válida.")
            exit()

        result = tm.run(cadena_parseada)
        '''print("Pasos de la cinta:")
        pp(tm.tape_status)
        print("=" * 20)'''
        print(f"Resultado: {result}")
        print(f"Resultado como entero: {result.count('0')}")
        print("=" * 20)

