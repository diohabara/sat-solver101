from __future__ import print_function

import logging
from sys import stderr
from typing import Any


def eprint(*args: Any, **kwargs: Any) -> None:
    logging.basicConfig(filename="example.log", encoding="utf-8", level=logging.DEBUG)
    logging.warning(*args, **kwargs)
