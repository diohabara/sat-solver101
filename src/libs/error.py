from __future__ import print_function

from sys import stderr
from typing import Any


def eprint(*args: Any, **kwargs: Any) -> None:
    print(*args, **kwargs, file=stderr)
