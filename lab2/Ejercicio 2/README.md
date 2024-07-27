# Ejercicio No. 2 - Balanceo de Expresiones Infix

## Descripción

Este ejercicio consiste en implementar un algoritmo que determine si las expresiones en formato infix están balanceadas. Se utiliza una pila para llevar track de los símbolos de interés, i.e., `()`, `[]`, `{}`, para definir el buen balanceo.

## Requisitos

- El programa debe leer un archivo de texto y procesar cada línea en este archivo.
- Por cada línea procesada, el programa debe indicar si la expresión regular en cuestión está bien balanceada o no.
- Debe mostrar la secuencia de pasos de la pila para validar que el algoritmo usa esta misma de forma adecuada para validar el buen balanceo de la expresión.
- En el video que se adjunte para su ejecución, se debe mostrar en pantalla el archivo a ejecutar, el resultado de la ejecución y cada uno de sus pasos, reflejando que ese archivo está siendo ejecutado y no es otro o es código hardcoded.

## Expresiones Regulares

El archivo `expresiones.txt` debe contener las siguientes expresiones regulares, una por línea:

a(a|b)b+a?
A(a|b)bB[az]b]
(abcd(a|e|i|o|u))efgh){1,2}
^[aZ].com{5,30}
([az][AZ]{10,20}))