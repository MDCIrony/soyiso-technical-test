"""Descripción breve del módulo.

Este módulo contiene los métodos necesarios para ejecutar la aplicación.

Métodos:
    - main(): Ejecuta el mainloop de la aplicación.
    - screen(): Imprime la pantalla principal de la aplicación.
"""
from typing import List

from src import utilities as util
from src.functions import DDBB


def main() -> None:
    """Mainloop principal.

    Función principal del programa. Ejecuta la aplicación.

    Args:
        None.

    Returns:
        None.
    """
    util.clean_window()

    # Instancia de la clase DDBB
    Store = DDBB()

    # Mostramos la pantalla principal de la aplicación
    screen(Store)

    while True:  # Mainloop
        try:
            # Solicitamos la opción a ejecutar con la base de datos instanciada
            selection(Store)

            # Reinicia la pantalla con la información nueva
            util.clean_window()
            screen(Store)

        except ValueError:
            input("Opción inválida, presiona enter para intentar de nuevo.")
            util.clean_window()
            screen(Store)

        except KeyboardInterrupt:
            print("\nSaliendo...")
            break


def selection(Store: DDBB) -> None:
    """Solicita al usuario la opción a ejecutar.

    Función que solicita al usuario la opción a ejecutar, y
        la ejecuta llamando a los métodos de la clase DDBB.

    Args:
        - Store: Instancia de la clase DDBB.

    Returns:
        None.
    """
    option: int = int(input("Elija opción: "))

    if option not in Store.Options.keys():
        raise ValueError

    if option == 1:
        Store.Add(
            product_name=input("Nombre del producto: "),
            product_price=float(input("Precio del producto: ")),
            product_stock=int(input("Stock del producto: ")),
        )
    elif option == 2:
        for i in range(3, 0, -1):
            try:
                Store.Delete(id=int(input("ID del producto a eliminar: ")))
                break
            except ValueError:
                print(f"El id no existe. Intentos restantes: {i - 1}")
    elif option == 3:
        pass
    elif option == 4:
        Store.Exit()


def screen(Store: DDBB) -> None:
    """Imprime la pantalla principal.

    Imprime en pantalla la lista de productos actualizada y.
    las opciones disponibles.

    Args:
        - Store: Instancia de la clase DDBB.

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

    # Ordenamos las keys del diccionario
    ordered_keys: List[int] = sorted(Store.Productos.keys())

    for key in ordered_keys:
        print(
            f"{key} \
      {Store.Productos[key]} \
      {Store.Precios[key]} \
      {Store.Stock[key]}"
        )

    print("========================================")

    for key, options in Store.Options.items():
        if key < len(Store.Options):
            print(f"[{key}] {options}", end=", ")
        else:  # Last option
            print(f"[{key}] {options}")
