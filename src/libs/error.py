from __future__ import print_function

from typing import Any

import logger


def eprint(*args: Any, **kwargs: Any) -> None:
    logger.error(*args, **kwargs)
