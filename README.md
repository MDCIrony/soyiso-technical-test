# Stock_Manager

Este programa permite agregar, eliminar y actualizar productos, precios y stocks de un inventario. El programa se ejecuta en la consola de Python.

Los datos se guardan en diccionarios predefinidos en el código fuente dentro del archivo `src/dictionaries.py` según las exigencias del ejercicio, por lo que los cambios realizados en el programa no se guardan (no hay persistencia de datos).

## Instalación

1. Clonar el repositorio
2. Crear un ambiente virtual en Python utilizando virtualenv o venv:

```bash
python3 -m venv venv
```

3. Activar el ambiente virtual:

```bash
source venv/bin/activate # Linux
venv\Scripts\activate # Windows
```

4. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

## Ejecución

```bash
python Stock_manager.py
```

## Ejercicio

```py
# Se tienen los siguientes diccionarios:
# PROGRAMA PRINCIPAL
Productos = {1:'Pantalones', 2:'Camisas', 3:'Corbatas', 4:'Casacas'}
Precios = {1:200.00, 2:120.00, 3:50.00, 4:350.00}
Stock = {1:50, 2:45, 3:30, 4:15}

# Elaborar un programa que muestre los diccionarios, y programar las siguientes acciones:
# [1] Agregar
# [2] Eliminar
# [3] Actualizar
# [4] Salir

'''
========================================
Lista de Productos:
========================================
1 	 Pantalones	 200.0 	 50
2 	 Camisas 	 120.0 	 45
3 	 Corbatas 	 50.0 	 30
4 	 Casacas 	 350.0 	 15
========================================
[1] Agregar, [2] Eliminar, [3] Actualizar, [4] Salir
Elija opción:
'''
```

## Meta-data

- Autor: [Miguel Díaz](https://github.com/MDCIrony)
- Versión: 1.0.0
- Fecha de creación: 2022-02-22
