# Conversión de Expresiones Regulares de Notación Infix a Postfix

Este proyecto implementa el algoritmo de Shunting Yard para convertir expresiones regulares de notación infix a notación postfix. El programa procesa un archivo de texto con expresiones regulares, convierte cada expresión a notación postfix y genera un archivo de salida con los resultados y los pasos realizados durante la conversión.

## Algoritmo de Shunting Yard

El algoritmo de Shunting Yard fue desarrollado por Edsger Dijkstra y se utiliza para convertir una expresión en notación infija (donde los operadores se encuentran entre los operandos) a notación posfija (donde los operadores se encuentran después de sus operandos). Este algoritmo maneja la precedencia de los operadores y los paréntesis para asegurar que la expresión posfija resultante sea evaluada correctamente.

El algoritmo utiliza una pila para mantener los operadores y paréntesis mientras se recorre la expresión infija. Los operandos se agregan directamente a la salida. Cuando se encuentra un operador, se compara su precedencia con el operador en la cima de la pila, y dependiendo de esta comparación, el operador puede ser apilado o puede hacer que los operadores de la pila se muevan a la salida. Los paréntesis se manejan específicamente para asegurar que las operaciones dentro de los paréntesis se evalúen correctamente.

### Pasos del algoritmo:

1. Inicializar una pila vacía para los operadores y una lista para la salida.
2. Recorrer cada token de la expresión infija:
   - Si el token es un operando, agregarlo a la salida.
   - Si el token es un paréntesis de apertura, apilarlo.
   - Si el token es un paréntesis de cierre, desapilar operadores hasta encontrar un paréntesis de apertura.
   - Si el token es un operador, desapilar operadores de mayor o igual precedencia y luego apilar el operador actual.
3. Al final de la expresión, mover cualquier operador restante en la pila a la salida.

## Uso del Código

### Requisitos

- Python 3.x

### Instrucciones

1. Coloca tus expresiones regulares en un archivo de texto, una por línea. Por ejemplo, `input_expressions.txt`.
2. Asegúrate de que el archivo de entrada esté en la ruta especificada en el código.
3. Ejecuta el script para procesar las expresiones y generar el archivo de salida con los resultados y los pasos realizados durante la conversión.
