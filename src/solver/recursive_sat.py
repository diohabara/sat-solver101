from typing import Any, List

from libs.error import eprint

from .satinstance import SATInstance
from .watchlist import update_watchlist


def solve(
    instance: SATInstance,
    watchlist: List[List[List[int]]],
    assignment: List[int],
    depth: int,
) -> Any:
    """
    Recursively solve SAT by assigning to variables d, d+1, ..., n-1.
    Assuming variables 0, 1, ..., d-1 are assigned so far.
    A generator for all the satisfying assignments is returned.
    """
    if depth == len(instance.variables):
        yield assignment
        return

    for a in [0, 1]:
        eprint(f"Trying {instance.variables[depth]} = {a}")
        assignment[depth] = a
        if update_watchlist(instance, watchlist, (depth << 1) | a, assignment):
            for a in solve(instance, watchlist, assignment, depth + 1):
                yield a

    assignment[depth] = -1
