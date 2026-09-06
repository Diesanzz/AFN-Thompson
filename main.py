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
        #La funcion ord() nos devuelve el valor numerico del caracter,
        # y la funcion chr() nos devuelve el caracter a partir de su valor numerico
        for codigo in range(ord(simb1), ord(simb2) + 1):
            f.alfabeto.add(chr(codigo))

        return f

    def concatenar(self, f2):

        # Cada estado del primer AFN
        for estado_acept in self.edos_acept:

            # Deajra de ser estado de aceptacion
            estado_acept.edo_acept = False

            # Luego se copian las transiciones del estado ini del f2
            for transicion in f2.edo_ini.transiciones:
                estado_acept.transiciones.append(transicion)

        # Se elimina el estado inicial de f2
        f2.edos_afn.discard(f2.edo_ini)

        # Y terminamos de juntar los estados de f2 al primer AFN
        self.edos_afn.update(f2.edos_afn)
        self.edos_acept = f2.edos_acept
        self.alfabeto.update(f2.alfabeto)

        return self

    def unir(self, f2):

        # Aqui se crean nuevos estados, tanto final como inicial
        nuevo_ini = Estado()
        nuevo_fin = Estado()

        #Ahora el nuevo fin sera de aceptacion
        nuevo_fin.edo_acept = True

        #Ponemos las transiciones del nuevo estado inicial 
        # a los estados iniciales de ambos AFN
        nuevo_ini.transiciones.append(
            Transicion(self.EPSILON, self.edo_ini)
        )

        nuevo_ini.transiciones.append(
            Transicion(self.EPSILON, f2.edo_ini)
        )

        #Eliminamos los anteriores estados de aceptacion
        for estado in self.edos_acept:
            estado.edo_acept = False
            estado.transiciones.append(
                Transicion(self.EPSILON, nuevo_fin)
            )

        for estado in f2.edos_acept:
            estado.edo_acept = False
            estado.transiciones.append(
                Transicion(self.EPSILON, nuevo_fin)
            )

        # Unimos todos los estados ahora si
        self.edos_afn.update(f2.edos_afn)

        self.edos_afn.add(nuevo_ini)
        self.edos_afn.add(nuevo_fin)

        # Actualizamos estado inicial y tambien el de aceptacion
        self.edo_ini = nuevo_ini
        self.edos_acept = {nuevo_fin}

        # Tambien se actualiza el alfabeto
        self.alfabeto.update(f2.alfabeto)

        return self

    def cerradura_pos(self):

        # Aqui vamos a crear los nuevos estados para la cerradura
        nuevo_ini = Estado()
        nuevo_fin = Estado()

        nuevo_fin.edo_acept = True

        nuevo_ini.transiciones.append(
            Transicion(self.EPSILON, self.edo_ini)
        )

        # Volvemos a hacer lo de reemplazar estados 
        # finales e iniciales
        for estado in self.edos_acept:
            estado.edo_acept = False

            estado.transiciones.append(
                Transicion(self.EPSILON, self.edo_ini)
            )

            estado.transiciones.append(
                Transicion(self.EPSILON, nuevo_fin)
            )

        self.edos_afn.add(nuevo_ini)
        self.edos_afn.add(nuevo_fin)

        self.edo_ini = nuevo_ini
        self.edos_acept = {nuevo_fin}

        return self

    def cerradura_kleene(self):

        # Aplicamos primero la cerradura positiva
        self.cerradura_pos()

        # Ahora ponemos la transicion del estado 
        # incial al final

        for estado_acept in self.edos_acept:
            self.edo_ini.transiciones.append(
                Transicion(self.EPSILON, estado_acept)
            )

        return self

    def opcional(self):

        # Nuevos estados
        nuevo_ini = Estado()
        nuevo_fin = Estado()

        nuevo_fin.edo_acept = True

        # Entrar al AFN original
        nuevo_ini.transiciones.append(
            Transicion(self.EPSILON, self.edo_ini)
        )

        # O ir directo al estado final
        nuevo_ini.transiciones.append(
            Transicion(self.EPSILON, nuevo_fin)
        )

        for estado in self.edos_acept:
            estado.edo_acept = False

            estado.transiciones.append(
                Transicion(self.EPSILON, nuevo_fin)
            )

        self.edos_afn.add(nuevo_ini)
        self.edos_afn.add(nuevo_fin)

        self.edo_ini = nuevo_ini
        self.edos_acept = {nuevo_fin}

        return self

    def obtener_transiciones(self):
        resultado = []

        for estado in sorted(self.edos_afn, key=lambda e: e.id_edo):

            for transicion in estado.transiciones:

                # Establecemos los simbolos
                if transicion.simb_inf == self.EPSILON:
                    simbolo = self.EPSILON

                elif transicion.simb_inf == transicion.simb_sup:
                    simbolo = transicion.simb_inf

                else:
                    simbolo = f"{transicion.simb_inf}-{transicion.simb_sup}"

                resultado.append(
                    (
                        estado.id_edo,
                        simbolo,
                        transicion.edo_dest.id_edo
                    )
                )

        return resultado

    def ver_afn(self):

        print("\n            AFN")

        print("Estado inicial:", self.edo_ini.id_edo)

        print(
            "Estados:",
            [e.id_edo for e in sorted(
                self.edos_afn,
                key=lambda e: e.id_edo
            )]
        )

        print(
            "Estados de aceptacion:",
            [e.id_edo for e in sorted(
                self.edos_afn,
                key=lambda e: e.id_edo
            )]
        )

        print("Alfabeto:", sorted(self.alfabeto))

        print("\nTabla de transiciones")
        print("----------------------")
        print("Edo\tSimb\tEdo")

        for origen, simbolo, destino in self.obtener_transiciones():
            print(f"{origen}\t{simbolo}\t{destino}")

        print("----------------------")
    

    
# --------
# a partir de aqui es como el test bench, la parte de pruebas
# --------


if __name__ == "__main__":

    afn1 = AFN().crear_basico("a")
    afn2 = AFN().crear_basico("b")

    afn1.unir(afn2)

    afn1.ver_afn()