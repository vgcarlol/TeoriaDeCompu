def es_balanceado(expresion):
    apertura = "({["
    cierre = ")}]"
    pares = {")": "(", "}": "{", "]": "["}
    pila = []
    pasos_pila = []

    for char in expresion:
        if char in apertura:
            pila.append(char)
            pasos_pila.append(f"Push {char}: {pila}")
        elif char in cierre:
            if pila and pila[-1] == pares[char]:
                pila.pop()
                pasos_pila.append(f"Pop {char}: {pila}")
            else:
                if not pila:
                    pasos_pila.append(f"Error: no hay apertura para {char}")
                else:
                    pasos_pila.append(f"Error: apertura incorrecta para {char}, se esperaba {pares[char]} pero se encontró {pila[-1]}")
                return False, pasos_pila

    if not pila:
        return True, pasos_pila
    else:
        pasos_pila.append(f"Error final: aperturas no cerradas {pila}")
        return False, pasos_pila

def procesar_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()

    for numero, linea in enumerate(lineas, start=1):
        expresion = linea.strip()
        balanceado, pasos_pila = es_balanceado(expresion)
        resultado = "balanceada" if balanceado else "no balanceada"
        print(f"Expresión en la línea {numero}: {expresion} -> {resultado}")
        print("Secuencia de pasos de la pila:")
        for paso in pasos_pila:
            print(paso)
        print("-" * 40)

if __name__ == "__main__":
    procesar_archivo('C:/Users/user/Desktop/Github/TeoriaDeCompu/lab2/Ejercicio 2/expresiones.txt')
