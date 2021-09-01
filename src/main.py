"""
Solves SAT instance by reading from stdin using a recursive
    watchlist-base backtracking algorithm.
Empty lines adn lines starting with a # will be ignored.
"""
from argparse import ArgumentParser, FileType
from sys import stdin, stdout
from typing import Any, TextIO

from libs.error import eprint
from solver import recursive_sat
from solver.satinstance import SATInstance
from solver.watchlist import setup_watchlist


def generate_assignments(instance: SATInstance) -> Any:
    """
    Returns a generator that generates all the satisfying assignments
        for a given SAT instance, using algorithm given by alg.
    """
    n = len(instance.variables)
    watchlist = setup_watchlist(instance)
    if not watchlist:
        return ""
    assignment = [-1] * n
    return recursive_sat.solve(instance, watchlist, assignment, 0)


def run_solver(
    input_file: TextIO,
    output_file: TextIO,
) -> Any:
    """
    run the given solver fo the given file-like input object
        and write the output to the given output file-like object.
    """
    instance = SATInstance.from_file(input_file)
    assignments = generate_assignments(instance)
    count = 0
    for assignment in assignments:
        count += 1
        eprint(f"Found satisfying assignment: #{count}")
        assignment_str = instance.assignment_to_string(assignment)
        output_file.write(assignment_str + "\n")
    if count == 0:
        eprint("No satisfying assignment exists.")


def sat_parser() -> ArgumentParser:
    parser = ArgumentParser(description=__doc__)
    parser.add_argument(
        "-i",
        "--input",
        help="read from the given file.",
        type=FileType("r"),
        default=stdin,
    )
    parser.add_argument(
        "-o",
        "--output",
        help="output to the given file.",
        type=FileType("w"),
        default=stdout,
    )
    return parser


def main() -> Any:
    """
    execute code.
    input and output files are defined by standard input.
    """
    args = sat_parser().parse_args()
    with args.input:
        with args.output:
            run_solver(input_file=args.input, output_file=args.output)


if __name__ == "__main__":
    main()
