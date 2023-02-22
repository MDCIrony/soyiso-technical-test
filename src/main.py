"""Módulo principal de la aplicación.

Este módulo contiene los métodos necesarios para ejecutar la aplicación.

Métodos:
    - main(): Ejecuta el mainloop de la aplicación.
    - screen(): Imprime la pantalla principal de la aplicación.
"""
from typing import List

from src import utilities as util
from src.Crud_class import DDBB


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
            # Gestionamos la selección del usuario
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

    if option not in Store.get_options().keys():
        raise ValueError

    if option == 1:
        Store.Add(
            product_name=input("Nombre del producto: "),
            product_price=float(input("Precio del producto: ")),
            product_stock=int(input("Stock del producto: ")),
        )

    elif option == 2:
        if not Store.get_ordered_products().keys():
            input(
                "No hay productos en la base de datos. \
Apriete enter para continuar."
            )
        else:
            for i in range(3, 0, -1):
                try:
                    Store.Delete(id=int(input("ID del producto a eliminar: ")))
                    break
                except ValueError:
                    print(f"Valor de id inválido. Intentos restantes: {i - 1}")
                except KeyError as error:
                    print(error, f"Intentos restantes: {i - 1}")

    elif option == 3:
        if not Store.get_ordered_products().keys():
            input(
                "No hay productos en la base de datos. \
Apriete enter para continuar."
            )
        else:
            for i in range(3, 0, -1):
                try:
                    id_to_update = int(input("ID del producto a actualizar: "))
                    if id_to_update not in Store.get_ordered_products().keys():
                        raise KeyError(f"El id {id_to_update} no existe en la base de datos.")

                    new_name = input("Nuevo nombre del producto (dejar en blanco para mantener el actual): ")
                    if new_name == "":
                        new_name = Store.get_ordered_products()[id_to_update]["Name"]

                    new_price = input("Nuevo precio del producto (dejar en blanco para mantener el actual): ")
                    if new_price == "":
                        new_price = Store.get_ordered_products()[id_to_update]["Price"]
                    else:
                        try:
                            new_price = float(new_price)
                        except:
                            raise Exception("El precio debe ser un número.")

                    new_stock = input("Nuevo stock del producto (dejar en blanco para mantener el actual): ")
                    if new_stock == "":
                        new_stock = Store.get_ordered_products()[id_to_update]["Stock"]
                    else:
                        try:
                            new_stock = int(new_stock)
                        except:
                            raise Exception("El stock debe ser un número entero.")

                    Store.Update(id=id_to_update, new_name=new_name, new_price=new_price, new_stock=new_stock)
                    break

                except ValueError:
                    print(f"Valor de id inválido. Intentos restantes: {i - 1}")
                    continue
                except KeyError as error:
                    print(f"{error}. Intentos restantes: {i - 1}")
                    continue
                except Exception as error:
                    print(f"{error}. Intentos restantes: {i - 1}")

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
    
    for key, product in Store.get_ordered_products().items():
        print(f"{key} {product['Name']} {product['Price']} {product['Stock']}")


    print("========================================")

    #Opciones disponibles
    for key, options in Store.get_options().items():
        if key < len(Store.Options):
            print(f"[{key}] {options}", end=", ")
        else:  # Last option
            print(f"[{key}] {options}")
