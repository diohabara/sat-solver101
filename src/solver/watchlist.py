from typing import List

from libs.error import eprint

from .satinstance import SATInstance


def dump_watchlist(instance: SATInstance, watchlist: List[List[List[int]]]) -> None:
    eprint("Current watchlist:")
    for literal, _watchlist in enumerate(watchlist):
        literal_string = instance.literal_to_string(literal)
        clauses_string = ", ".join(
            instance.clause_to_string(_clause) for _clause in _watchlist
        )
        eprint(f"{literal_string}: {clauses_string}")


def setup_watchlist(instance: SATInstance) -> List[List[List[int]]]:
    """
    Each variables(0, 1, ..., n-1) has two state, that is x(positive) and ~x(negative).
    watchlist has each variables' clause
    watchlist[variable] = clauses
    """
    watchlist: List[List[List[int]]] = [[] for _ in range(2 * len(instance.variables))]
    for clause in instance.clauses:
        watchlist[clause[0]].append(clause)
    return watchlist


def update_watchlist(
    instance: SATInstance,
    watchlist: List[List[List[int]]],
    false_literal: int,
    assignment: List[int],
) -> bool:
    """
    Updates the watch list after literal `false_literal` was just assigned False.
    By making any clause watching, `false_literal` watch something else.
    Return False if it is impossible to do so,
        meaning a clause is contradicted by the current assignment.
    """
    while watchlist[false_literal]:
        clause: List[int] = watchlist[false_literal][0]
        found_alternative = False  # if this value is True, then false_literal is True
        for alternative in clause:  # each variables
            v = alternative >> 1  # True version of false_literal
            a = alternative & 1  # negated or not
            """
            assignment is a list of each variables' value, which is TRUE or FALSE
            If x is TRUE, assignment[x] is 1.
            If FALSE, assignment[x] is 0.
            """
            if not assignment[v] or assignment[v] == a ^ 1:
                found_alternative = True
                del watchlist[false_literal][0]
                watchlist[alternative].append(clause)
                break

        if not found_alternative:
            dump_watchlist(instance, watchlist)
            eprint(f"Current assignment: {instance.assignment_to_string(assignment)}")
            eprint(f"Clause {instance.clause_to_string(clause)} contradicted.")
            return False
    return True
