#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-

"""
**Created:**    ??.??.2022
**Modified:**   ??.??.2022

**Authors:**    [Tobias Rosskopf](mailto:tobirosskopf@gmail.com)

Module for the command line interface
"""

import click
from colorama import init as colorama_init
from colorama import Fore

from .module_name import ClassName


@click.command()
@click.argument("input_path", type=click.Path(exists=True))
def main(input_path: str) -> None:
    """
    Main method

    Args:
        input_path (str): Path to input file
    """
    # Initialize colorama
    colorama_init()

    instance = ClassName(input_path)
    print(f"{Fore.GREEN}{instance}{Fore.RESET}")

    print(f"{Fore.GREEN}Erfolgreich ausgeführt!{Fore.RESET}")
