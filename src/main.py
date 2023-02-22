"""Descripción breve del módulo.

Este módulo contiene los métodos necesarios para ejecutar la aplicación.

Métodos:
    - main(): Ejecuta el mainloop de la aplicación.
    - screen(): Imprime la pantalla principal de la aplicación.
"""
from src import dictionaries as DB
from src import utilities as util
from src.functions import App_options as Options


def main() -> None:
    """Descripción breve del método.

    Función principal del programa. Ejecuta la aplicación.

    Args:
        None.

    Returns:
        None.
    """
    screen()
    while True:  # Mainloop
        try:
            selection()

            # Reinicia la pantalla con la información nueva
            util.clean_window()
            screen()

        except ValueError:
            print("Opción inválida, intente de nuevo.")

        except KeyboardInterrupt:
            print("\nSaliendo...")
            break


def selection() -> None:
    """Descripción breve del método.

    Función que ejecuta la opción seleccionada por el usuario.

    Args:
        None.

    Returns:
        None.
    """
    option: int = int(input("Elija opción: "))

    if option not in Options.keys():
        raise ValueError

    Options[option]()


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
