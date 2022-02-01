#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

"""
**Created:**    ??.??.2022
**Modified:**   ??.??.2022

**Authors:**    [Tobias Rosskopf](mailto:tobirosskopf@gmail.com)

Entry point for the package
"""

import sys
import subprocess
from pathlib import Path

# Selfinstall packages if not found
try:
    import package_name.cli
except ImportError:
    subprocess.call([sys.executable, "-m", "pip", "install", "-r", Path(__file__).parent.joinpath("requirements.txt")])
    import package_name.cli


if __name__ == "__main__":
    package_name.cli.main()
