"""Clase con métodos CRUD para interactuar con la db (diccionarios).

Este módulo contiene la clase maestra con los atributos
    y métodos principales para interactuar con la base
    de datos manejada en la aplicación Stock_manager.
    Para el ejemplo esta consiste en una serie de
    diccionarios predefinidos en el archivo dictionaries.py.
"""
from typing import Dict, List, Union

from src import dictionaries as DB


class DDBB:
    """Descripción breve de la clase.

    Clase que contiene los métodos para interactuar con la base de datos.

    Atributos:
        - Productos: Diccionario que contiene los nombres de los productos.
        - Precios: Diccionario que contiene los precios de los productos.
        - Stock: Diccionario que contiene el stock de los productos.
    """

    # Class constructor
    def __init__(self) -> None:
        """Método que inicializa la db.

        Este método inicializa la base de datos con los
            valores definidos en dictionaries.py. Al
            estarse utilizando un diccionario y no una
            db permanente, estos valores serán reiniciados
            cada vez que se ejecute la aplicación
            y cualquier modificación será borrada.

        Args:
            None

        Atributos:
            - Productos: Diccionario que contiene
                los nombres de los productos.
            - Precios: Diccionario que contiene los
                precios de los productos.
            - Stock: Diccionario que contiene el stock
                de los productos.
            - Options: Diccionario que contiene las
                opciones del menú principal.
            - next_id: Variable que contiene el valor
                de la siguiente llave auto_incremental.
        """
        # self.Productos: Dict[int, str] = DB.Productos
        # self.Precios: Dict[int, float] = DB.Precios
        # self.Stock: Dict[int, int] = DB.Stock
        self.Products: Dict[int, Dict[str, Union[str, float, int]]] = {
            key: {
                "Name": DB.Productos[key],
                "Price": DB.Precios[key],
                "Stock": DB.Stock[key],
            }
            for key in DB.Productos.keys()
        }

        self.Options: Dict[int, str] = {
            1: "Agregar",
            2: "Eliminar",
            3: "Actualizar",
            4: "Salir",
        }
        # Auto_incremental key
        self.next_id: int = len(self.Products) + 1
        self.cache_id: List[int] = []

    def Add(self, product_name: str, product_price: float, product_stock: int) -> None:
        """Añade un nuevo producto a la base de datos.

        Args:
            - product_name: Nombre del producto.
            - product_price: Precio del producto.
            - product_stock: Stock del producto.

        Returns:
            None.
        """
        self.Products[self.next_id] = {
            "Name": product_name,
            "Price": product_price,
            "Stock": product_stock,
        }            

        # Incrementamos el siguiente id evaluando si no quedan más en caché
        if self.cache_id == []:
            self.next_id = len(self.Products) + 1
        else:
            # Eliminamos el id utilizado de caché
            self.cache_id.remove(self.next_id)

            # Si no quedan más ids en caché, se asigna el siguiente id
            # como la longitud de la db + 1
            # De lo contrario, se asigna el mínimo de los ids en caché
            if self.cache_id == []:
                self.next_id = len(self.Products) + 1
            else:
                self.next_id = min(self.cache_id)

    def Delete(self, id: int) -> None:
        """Elimina un producto de la db.

        Elimina un producto de la base de datos
            consultando al usuario el id, luego
            se actualiza el siguiente id con el
            valor del id eliminado.

        Args:
            - id: ID del producto a eliminar.

        Returns:
            None.
        """
        if id in self.Products.keys():
            self.cache_id.append(id)
            self.next_id = min(self.cache_id)
        else:
            raise KeyError(f"El id {id} no existe en la base de datos.")
        
        self.Products.pop(id)

    def Update(self, id: int, new_name: str, new_price: float, new_stock: int) -> None:
        """Actualiza un producto de la db.

        Actualiza un producto de la base de datos
            consultando al usuario el id y los nuevos datos
            [nombre, precio y stock].

        Args:
            None

        Returns:
            None.
        """
        self.Products[id] = {
            "Name": new_name,
            "Price": new_price,
            "Stock": new_stock,
        }


    def Exit(self) -> None:
        """Cierra la aplicación.

        Cierra la aplicación forzando un error de tipo
            KeyboardInterrupt, el cual debe ser interceptado
            en el mainloop.

        Args:
            None

        Returns:
            None.
        """
        raise KeyboardInterrupt
    
    def get_ordered_products(self) -> Dict[int, Dict[str, Union[str, float, int]]]:
        """Obtiene los productos de la db.

        Obtiene los productos de la base de datos.

        Args:
            None

        Returns:
            - ordered_products: Diccionario que contiene
                los productos de la base de datos ordenados por clave.
        """
        ordered_products = {}
        for key in sorted(self.Products.keys()):
            ordered_products[key] = {
                "Name": self.Products[key]["Name"],
                "Price": self.Products[key]["Price"],
                "Stock": self.Products[key]["Stock"]
            }
        return ordered_products

    def get_options(self) -> Dict[int, str]:
        """Obtiene las opciones del menú principal.

        Obtiene las opciones del menú principal.

        Args:
            None

        Returns:
            - options: Diccionario que contiene las opciones
                del menú principal.
        """
        return self.Options