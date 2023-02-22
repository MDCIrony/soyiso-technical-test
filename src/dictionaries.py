"""Descripción breve del módulo.

Este módulo contiene los diccionarios necesarios para ejecutar
    la aplicación Stock_manager.
Estos diccionarios contienen los datos de los productos
    (se emplean como base de datos).

Atributos:
    - Productos: Diccionario que contiene los nombres de los productos.
    - Precios: Diccionario que contiene los precios de los productos.
    - Stock: Diccionario que contiene el stock de los productos.
"""
from typing import Dict


Productos: Dict[int, str] = {
    1: "Pantalones",
    2: "Camisas",
    3: "Corbatas",
    4: "Casacas",
}
Precios: Dict[int, float] = {
    1: 200.00,
    2: 120.00,
    3: 50.00,
    4: 350.00,
}
Stock: Dict[int, int] = {
    1: 50,
    2: 45,
    3: 30,
    4: 15,
}
