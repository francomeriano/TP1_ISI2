"""
Módulo: factorial_OOP.py
Descripción: Calcula factoriales usando programación orientada a objetos.
Soporta números simples y rangos.
Autor: Franco Meriano
Materia: Ingeniería de Software II
"""

import sys


class Factorial:
    """
    Clase para calcular factoriales.
    
    Atributos:
        inicio (int): Límite inferior del rango
        fin (int): Límite superior del rango
    """
    
    def __init__(self, inicio=None, fin=None):
        """
        Constructor de la clase Factorial.
        
        Parámetros:
            inicio (int): Límite inferior (opcional)
            fin (int): Límite superior (opcional)
        """
        self.inicio = inicio
        self.fin = fin
    
    def calcular(self, n):
        """
        Calcula el factorial de un número de forma recursiva.
        
        Parámetros:
            n (int): Número a calcular
            
        Retorna:
            int: Factorial de n
        """
        if n <= 1:
            return 1
        return n * self.calcular(n - 1)
    
    def run(self, min_val=None, max_val=None):
        """
        Ejecuta el cálculo de factoriales para un rango.
        
        Parámetros:
            min_val (int): Límite inferior (opcional)
            max_val (int): Límite superior (opcional)
            
        Retorna:
            dict: Diccionario con los resultados {número: factorial}
        """
        # Usar valores pasados como parámetro o los del constructor
        inicio = min_val if min_val is not None else self.inicio
        fin = max_val if max_val is not None else self.fin
        
        if inicio is None or fin is None:
            raise ValueError("Debe especificar un rango válido")
        
        resultados = {}
        for i in range(inicio, fin + 1):
            resultados[i] = self.calcular(i)
        
        return resultados
    
    def mostrar(self, resultados):
        """
        Muestra los resultados de forma formateada.
        
        Parámetros:
            resultados (dict): Diccionario con resultados a mostrar
        """
        print("\n" + "="*40)
        print("RESULTADOS DE FACTORIALES")
        print("="*40)
        for numero, factorial_valor in resultados.items():
            print(f"{numero}! = {factorial_valor}")
        print("="*40)


def parsear_entrada(entrada):
    """
    Parsea la entrada del usuario.
    Soporta:
    - Número simple: "5"
    - Rango completo: "4-8"
    - Desde 1 hasta N: "-10"
    - Desde N hasta 60: "5-"
    
    Parámetros:
        entrada (str): String ingresado por el usuario
        
    Retorna:
        tuple: (inicio, fin) como enteros
    """
    entrada = entrada.strip()
    
    if '-' in entrada:
        partes = entrada.split('-')
        inicio_str = partes[0]
        fin_str = partes[1]
        
        # Caso "-10" (sin límite inferior)
        if inicio_str == "":
            return 1, int(fin_str)
        # Caso "5-" (sin límite superior)
        elif fin_str == "":
            return int(inicio_str), 60
        # Caso "4-8" (rango completo)
        else:
            return int(inicio_str), int(fin_str)
    else:
        # Número simple
        num = int(entrada)
        return num, num


def main():
    """
    Función principal del programa.
    """
    # Obtener entrada del usuario
    if len(sys.argv) > 1:
        entrada = sys.argv[1]
    else:
        entrada = input("Ingrese un número o rango (ej: 5, 4-8, -10, 5-): ")
    
    # Parsear la entrada
    inicio, fin = parsear_entrada(entrada)
    
    # Crear instancia de la clase Factorial
    calculadora = Factorial(inicio, fin)
    
    # Ejecutar el cálculo
    print(f"\nCalculando factoriales desde {inicio} hasta {fin}...")
    resultados = calculadora.run()
    
    # Mostrar resultados
    calculadora.mostrar(resultados)


if __name__ == "__main__":
    main()