#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

"""
**Created:**    ??.??.2022
**Modified:**   ??.??.2022

**Authors:**    [Tobias Rosskopf](mailto:tobirosskopf@gmail.com)

<module_name>'s docstring
"""


class ClassName:
    """
    Class for <ClassName>
    """

    def __init__(self, name: str = "") -> None:
        """
        <ClassName> constructor

        Args:
            name (str): Name of instance
        """
        self.name: str = name

    def __repr__(self) -> str:
        """
        Generates REPL representation for <ClassName>

        Returns:
            str: REPL representation
        """
        return f"{self.__class__.__name__}({self.name})"

    def __str__(self) -> str:
        """
        Generates string representation for <ClassName>

        Returns:
            str: String representation
        """
        return f"{self.name}"

    def __eq__(self, other: object) -> bool:
        """
        Checks if <ClassName> instance is equal to other

        Args:
            other (object): Other object

        Returns:
            bool: True if equal, False otherwise
        """
        if isinstance(other, ClassName):
            return self.name == other.name
        return False
