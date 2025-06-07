"""
Example just for package template. Replace with your own code.
"""

import sys
from pathlib import Path
from typing import Tuple

import numpy as np
from munch import Munch
from scapy.all import conf

if sys.version_info < (3, 8):
    from importlib_metadata import version
else:
    from importlib.metadata import version

if sys.version_info < (3, 10):
    import importlib_resources as ilr  # type: ignore[import-not-found]
else:
    import importlib.resources as ilr

__version__ = version('ds2mermaid')

