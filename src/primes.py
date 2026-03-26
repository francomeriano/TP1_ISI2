# ============================================
# Programa: primes.py
# Descripción: Determina si un número ingresado es primo
# Autor: Franco Meriano
# Materia: Ingeniería de Software II
# Fecha: Marzo 2026
# ============================================

def es_primo(n):
    """
    Función que verifica si un número es primo.
    
    Parámetros:
    n (int): Número a verificar
    
    Retorna:
    bool: True si es primo, False si no lo es
    """
    # Caso especial: números menores o iguales a 1 no son primos
    if n <= 1:
        return False
    
    # Se verifica divisibilidad desde 2 hasta la raíz cuadrada de n
    # Si se encuentra un divisor, el número no es primo
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    # Si no se encontró ningún divisor, el número es primo
    return True


# ============================================
# Programa principal
# ============================================

# Solicita el número al usuario
numero = int(input("Ingrese un número entero: "))

# Verifica si es primo y muestra el resultado
if es_primo(numero):
    print(f"El número {numero} ES primo")
else:
    print(f"El número {numero} NO es primo")