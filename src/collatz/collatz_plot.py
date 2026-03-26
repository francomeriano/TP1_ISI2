"""
Módulo: collatz_plot.py
Descripción: Calcula la cantidad de iteraciones de la conjetura de Collatz
para números del 1 al 10000 y genera un gráfico.
Autor: Franco Meriano
Materia: Ingeniería de Software II
"""

import matplotlib.pyplot as plt


def collatz_iteraciones(n):
    """
    Calcula la cantidad de iteraciones que tarda un número en converger
    a la secuencia repetitiva de la conjetura de Collatz.
    
    Reglas de Collatz:
    - Si n es par: n = n / 2
    - Si n es impar: n = 3n + 1
    
    Parámetros:
        n (int): Número de inicio de la secuencia
        
    Retorna:
        int: Cantidad de iteraciones hasta llegar a 1
    """
    iteraciones = 0
    
    while n != 1:
        if n % 2 == 0:
            # Si es par, dividir por 2
            n = n // 2
        else:
            # Si es impar, multiplicar por 3 y sumar 1
            n = 3 * n + 1
        iteraciones += 1
    
    return iteraciones


def main():
    """
    Función principal: calcula iteraciones para números 1..10000
    y genera un gráfico.
    """
    print("Calculando iteraciones de Collatz para números del 1 al 10000...")
    
    # Listas para almacenar datos
    numeros = []
    iteraciones = []
    
    # Calcular iteraciones para cada número
    for n in range(1, 10001):
        numeros.append(n)
        iteraciones.append(collatz_iteraciones(n))
        
        # Mostrar progreso cada 1000 números
        if n % 1000 == 0:
            print(f"Procesados {n} números...")
    
    # Crear el gráfico
    plt.figure(figsize=(12, 6))
    plt.scatter(numeros, iteraciones, s=1, c='blue', alpha=0.5)
    
    # Configurar el gráfico
    plt.title("Conjetura de Collatz - Iteraciones por número", fontsize=16)
    plt.xlabel("Número de inicio (n)", fontsize=12)
    plt.ylabel("Número de iteraciones hasta converger", fontsize=12)
    plt.grid(True, alpha=0.3)
    
    # Agregar anotaciones
    max_iter = max(iteraciones)
    max_num = numeros[iteraciones.index(max_iter)]
    plt.annotate(f'Máximo: {max_iter} iteraciones\nNúmero: {max_num}',
                 xy=(max_num, max_iter),
                 xytext=(max_num + 1000, max_iter - 20),
                 arrowprops=dict(facecolor='red', shrink=0.05),
                 fontsize=10,
                 bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.7))
    
    # Mostrar estadísticas
    print("\n" + "="*50)
    print("ESTADÍSTICAS DE COLLATZ (1 al 10000)")
    print("="*50)
    print(f"Números procesados: {len(numeros)}")
    print(f"Promedio de iteraciones: {sum(iteraciones)/len(iteraciones):.2f}")
    print(f"Máximo de iteraciones: {max_iter} (número {max_num})")
    print(f"Mínimo de iteraciones: {min(iteraciones)} (número {numeros[iteraciones.index(min(iteraciones))]})")
    print("="*50)
    
    # Mostrar el gráfico
    plt.tight_layout()
    plt.show()
    
    print("\nGráfico generado correctamente.")


if __name__ == "__main__":
    main()