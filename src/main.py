# Description: Main file for the stock manager
from src import dictionaries as DB


def Hello():
    print("Hello World", DB.Productos, DB.Precios, DB.Stock, sep="\n")