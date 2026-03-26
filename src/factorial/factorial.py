#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*

"""
Módulo: factorial.py
Descripción: Calcula factoriales de números o rangos.
Soporta:
- Números simples: 5
- Rangos completos: 4-8
- Desde 1 hasta N: -10
- Desde N hasta 60: 5-
Autor: Franco Meriano
Materia: Ingeniería de Software II
"""

import sys

def factorial(n):
    """Calcula el factorial de un número n de forma recursiva"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def parsear_entrada(entrada):
    """
    Parsea la entrada del usuario.
    Soporta:
    - Número simple: "5"
    - Rango completo: "4-8"
    - Desde 1 hasta N: "-10"
    - Desde N hasta 60: "5-"
    """
    entrada = entrada.strip()
    
    if '-' in entrada:
        partes = entrada.split('-')
        inicio = partes[0]
        fin = partes[1]
        
        # Caso "-10" (sin límite inferior)
        if inicio == "":
            return 1, int(fin)
        # Caso "5-" (sin límite superior)
        elif fin == "":
            return int(inicio), 60
        # Caso "4-8" (rango completo)
        else:
            return int(inicio), int(fin)
    else:
        # Número simple
        num = int(entrada)
        return num, num

def main():
    # Verificar si se pasó un argumento
    if len(sys.argv) > 1:
        entrada = sys.argv[1]
    else:
        entrada = input("Ingrese un número o rango (ej: 5, 4-8, -10, 5-): ")
    
    # Parsear la entrada
    inicio, fin = parsear_entrada(entrada)
    
    # Calcular y mostrar factoriales
    print(f"\nCalculando factoriales desde {inicio} hasta {fin}:\n")
    for i in range(inicio, fin + 1):
        resultado = factorial(i)
        print(f"{i}! = {resultado}")

if __name__ == "__main__":
    main()