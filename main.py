class Estado:
    contador_edos = 0

    def __init__(self):
        self.id_edo = Estado.contador_edos
        Estado.contador_edos += 1

        self.edo_acept = False
        self.transiciones = []

    def __repr__(self):
        return f"Estado({self.id_edo})"

class Transicion:
    def __init__(self, simb_inf, edo_dest, simb_sup=None):
        self.simb_inf = simb_inf

        # Si solo manda un simbolo
        # Entonces el limite superior sera el mismo 
        if simb_sup is None:
            self.simb_sup = simb_inf
        else:
            self.simb_sup = simb_sup

        self.edo_dest = edo_dest

    def acepta(self, simbolo):
        return self.simb_inf <= simbolo <= self.simb_sup

    def __repr__(self):
        if self.simb_inf == self.simb_sup:
            simbolo = self.simb_inf
        else:
            simbolo = f"{self.simb_inf}-{self.simb_sup}"

        return f"--{simbolo}--> Estado({self.edo_dest.id_edo})"

class AFN:
    EPSILON = "ε"

    def __init__(self):
        self.alfabeto = set()
        self.edo_ini = None
        self.edos_acept = set()
        self.edos_afn = set()

    def crear_basico(self, simb1, simb2=None):
        # Si no se manda simb2, entonces se creara
        # Un AFN de un solo simbolo
        if simb2 is None:
            simb2 = simb1

        # Validaciones 
        if len(simb1) != 1 or len(simb2) != 1:
            raise ValueError(
                "Los simbolos deben ser de un solo caracter."
            )

        if ord(simb1) > ord(simb2):
            raise ValueError(
                "El simbolo inferior no puede ser mayor al superior."
            )

        # Aqui se creara el AFN nuevo
        f = AFN()

        # Aquie creamos sus dos estados
        e1 = Estado()
        e2 = Estado()

        # Aqui es donde se crea la transicion
        t = Transicion(simb1, e2, simb2)

        # La transicion sale del estado 1 e1
        e1.transiciones.append(t)

        # El 2 sera estado de aceptacion e2
        e2.edo_acept = True

        # Aqui se configura el AFN
        f.edo_ini = e1
        f.edos_acept.add(e2)

        f.edos_afn.add(e1)
        f.edos_afn.add(e2)

        # Por ultimo agregamos los simbolos del alfabeto
        #La funcion ord() nos devuelve el valor numerico del caracter, y la funcion chr() nos devuelve el caracter a partir de su valor numerico
        for codigo in range(ord(simb1), ord(simb2) + 1):
            f.alfabeto.add(chr(codigo))

        return f

# a partir de aqui es como el test bench, la parte de pruebas

if __name__ == "__main__":

    afn1 = AFN().crear_basico("a")

    print("AFN 1")
    print("Estado inicial:", afn1.edo_ini)
    print("Estados: ", afn1.edos_afn) 
    print("Estados de aceptacion: ", afn1.edos_acept)
    print("Alfabeto: ", afn1.alfabeto)

    print("\nTransiciones")

    for estado in afn1.edos_afn:
        for transicion in estado.transiciones:
            print(
                estado,
                transicion
            )

    print()

    afn2 = AFN().crear_basico("a", "z")

    print("AFN 2")
    print("Estado inicial:", afn2.edo_ini)
    print("Estados:", afn2.edos_afn)
    print("Estados de aceptacion:", afn2.edos_acept)
    print("Alfabeto:", afn2.alfabeto)

    print("\nTransiciones:")

    for estado in afn2.edos_afn:
        for transicion in estado.transiciones:
            print(
                estado,
                transicion
            )