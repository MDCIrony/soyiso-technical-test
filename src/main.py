"""Descripción breve del módulo.

Este módulo contiene los métodos necesarios para ejecutar la aplicación.

Funciones:
    - main(): Ejecuta el mainloop de la aplicación.
    - screen(): Imprime la pantalla principal de la aplicación.
"""
from src import dictionaries as DB


def main() -> None:
    """Descripción breve del método.

    Función principal del programa. Ejecuta la aplicación.

    Args:
        None.

    Returns:
        None.
    """
    screen()


def screen() -> None:
    """Descripción breve del método.

    Imprime en pantalla la lista de productos actualizada y.
    las opciones disponibles.

    Args:
        None.

    Returns:
        None.

    Ejemplo:
        >>> screen()
        ========================================
        Lista de Productos:
        ========================================
        1 Pantalones 200.0 50
        2 Camisas 120.0 45
        3 Corbatas 50.0 30
        4 Casacas 350.0 15
        ========================================
        [1] Agregar, [2] Eliminar, [3] Actualizar, [4] Salir
    """
    print("========================================")
    print("Lista de Productos:")
    print("========================================")

    for key in DB.Productos.keys():
        print(f"{key} {DB.Productos[key]} {DB.Precios[key]} {DB.Stock[key]}")

    print("========================================")
    print("[1] Agregar, [2] Eliminar, [3] Actualizar, [4] Salir")
