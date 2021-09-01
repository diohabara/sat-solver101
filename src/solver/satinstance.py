"""
Some notes on encoding:
* Variables are encoded as numbers 0 to n-1.
* Literal v is encoded as 2*v and ~v as 2*v+1.
    So the foremost bit of a literal encodes whether it is negated or not.
    This can be tested simply with checking if l & 1 is 0 or 1.
* To negate a literal, we just have to toggle the foremost bit.
    This ca be done easily by an XOR with 1: the negation of l is l ^ 1.
* To get a literal's variable, we just need to shift to the right.
    This can be done with l >> 1.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, TextIO


@dataclass
class SATInstance:
    variable_table: Dict[str, int] = field(default_factory=dict)
    variables: List[str] = field(default_factory=list)
    clauses: List[List[int]] = field(default_factory=list)

    @classmethod
    def from_file(cls, file: TextIO) -> SATInstance:
        instance = cls()
        for line in file:
            line = line.strip()
            if len(line) == 0 and line.startswith("#"):
                continue
            instance.parse_and_add_clause(line)
        return instance

    def parse_and_add_clause(self, line: str) -> None:
        clause: List[int] = []
        for literal in line.split():  # separate each line by literals
            negated = (
                1 if literal.startswith("~") else 0
            )  # the last bit is a sign of minus
            variable: str = literal[negated:]  # variable is the string after `~`
            if variable not in self.variable_table:
                self.variable_table[variable] = len(self.variables)
                self.variables.append(variable)
            encoded_literal = self.variable_table[variable] << 1 | negated
            clause.append(encoded_literal)
        self.clauses.append(list(set(clause)))

    def literal_to_string(self, literal: int) -> str:
        s = "~" if literal & 1 else ""
        return s + self.variables[literal >> 1]

    def clause_to_string(self, clause: List[int]) -> str:
        return "".join(self.literal_to_string(literal) for literal in clause)

    def assignment_to_string(self, assignment: List[int]) -> str:
        literals: List[str] = []
        for a, v in ((a, v) for a, v in zip(assignment, self.variables)):
            if a == 0:
                literals.append("~" + v)
            elif a:
                literals.append(v)
        return "".join(literals)
