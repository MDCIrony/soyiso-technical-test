"""Descripción breve del módulo.

Este módulo contiene los métodos principales para
    interactuar con la aplicación Stock_manager.

Métodos:
    - Add(): Añade un nuevo producto a la base de datos.
    - Delete(): Elimina un producto de la base de datos.
    - Update(): Actualiza la información de un producto.
    - Exit(): Cierra la aplicación.
"""
from typing import Dict, Callable

from src import dictionaries as DB


def Add() -> None:
    """Descripción breve del método.

    Añade un nuevo producto a la base de datos
        consultando al usuario el nombre, precio y stock.

    Args:
        None

    Returns:
        None.
    """
    # Solicitar datos del producto
    product_name: str = input("Nombre del producto: ")
    product_price: float = float(input("Precio del producto: "))
    product_stock: int = int(input("Stock del producto: "))

    new_key: int = len(DB.Productos) + 1

    DB.Productos[new_key] = product_name
    DB.Precios[new_key] = product_price
    DB.Stock[new_key] = product_stock


def Delete():
    """Descripción breve del método.

    Elimina un producto de la base de datos
        consultando al usuario el id.

    Args:
        None

    Returns:
        None.
    """
    pass


def Update():
    """Descripción breve del método.

    Actualiza un producto de la base de datos
        consultando al usuario el id y los nuevos datos
        [nombre, precio y stock].

    Args:
        None

    Returns:
        None.
    """
    pass


def Exit():
    """Descripción breve del método.

    Cierra la aplicación forzando un error de tipo KeyboardInterrupt.

    Args:
        None

    Returns:
        None.
    """
    raise KeyboardInterrupt


App_options: Dict[int, Callable] = {
    1: Add,
    2: Delete,
    3: Update,
    4: Exit,
}
