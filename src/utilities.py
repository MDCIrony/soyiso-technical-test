"""Descripción breve del módulo.

Este módulo contiene las utilities necesarias para ejecutar
    la aplicación Stock_manager.

Métodos:
    - clean_window(): Limpia la pantalla.
"""
import os


def clean_window() -> None:
    """Descripción breve del método.

    Limpia la pantalla.

    Args:
        None.

    Returns:
        None.
    """
    os.system("cls" if os.name == "nt" else "clear")
